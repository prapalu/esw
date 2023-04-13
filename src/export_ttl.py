# required libraries
import pandas as pd
import os
from pathlib import Path
import gc
import json
import hashlib
from jproperties import Properties
from datetime import datetime
# Load the required libraries
from rdflib import Graph, Literal, RDF,RDFS,BNode, URIRef, Namespace
# rdflib knows about some namespaces, like XSD
from rdflib.namespace import XSD

# Construct the namespaces not known by RDFlib
    ESW = Namespace("https://w3id.org/esw/ontology#")
ESWR = Namespace("https://w3id.org/esw/resource/")
LSQV = Namespace("http://lsq.aksw.org/vocab#")
SP = Namespace("http://spinrdf.org/sp#")
DCT = Namespace("http://purl.org/dc/terms/")
SD = Namespace("http://www.w3.org/ns/sparql-service-description#")

global nbks_folder
global rdf_folder


def load_json(directory,verbose = False):
    if verbose:
        print("Start to load files from:",directory)
    files={}
    for folder in os.listdir(directory):
        subdir = directory + os.sep + folder
        nbks = []
        for file in os.listdir(subdir):
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                fd = open(filepath,"r")
                tmp = json.load(fd)
                files[tmp["name"]] = tmp
                fd.close()
    if verbose:
        string = "Successfully load the json notebooks from the folder "+str(directory)+":\n"
        string += "--> Total number of files: "+str(len(files))
        print(string)
    return files

def load_workers(file,verbose = False):
    f = open(file,"r")
    lines = f.read().split("\n")[1:-1]
    f.close()
    workers = {}
    for w in lines:
        spl = w.split(",")
        name = spl[0]+"_"+spl[1]
        workers[name] = 0.0
        if int(spl[2])!=0:
            workers[name] = (float(int(spl[2])-17.0)/14.0)
    if verbose:
        print("Successfully loaded workers from",file)
    return workers

def load_gt_map(file,verbose = False):
    f = open(file,"r")
    lines = f.read().split("\n")[1:-1]
    f.close()
    gts = {}
    for w in lines:
        spl = w.split(",")
        gt = spl[0]
        topic = spl[1]
        gts[topic] = gt
    if verbose:
        print("Successfully loaded ground truths map from",file)
    return gts
    
def export_turtle(keyword_file,workers_file,gt_map_file,rdf_folder,files,track_type,year):
    #create the graph for the topics and tasks
    g = Graph()


    # Bind the namespaces to a prefix for more readable output
    g.bind("xsd", XSD)
    g.bind("esw", ESW)
    g.bind("eswr", ESWR)
    g.bind("lsqv", LSQV)
    g.bind("sp", SP)
    g.bind("sd",SD)

    #create the graph for the search workflows
    h = Graph()

    # Bind the namespaces to a prefix for more readable output
    h.bind("xsd", XSD)
    h.bind("esw", ESW)
    h.bind("eswr", ESWR)
    h.bind("lsqv", LSQV)
    h.bind("sp", SP)
    h.bind("dct",DCT)
    h.bind("sd",SD)
    
    # create the feature for the keywords
    f = open(keyword_file, "r")
    keywords = f.read().split("\n")
    f.close()
    for k in keywords:
        Keyword = URIRef(ESWR["".join(k.split())])
        g.add((Keyword, RDF.type, SD['Feature']))
        g.add((Keyword, RDFS.label, Literal(k, 'en')))
        
    topics=[]
    workers = []
    workers_grade = load_workers(workers_file)
    gt_map = load_gt_map(gt_map_file)

    # create the URI for the Track
    Track = URIRef(ESWR[track_type+str(year)+"Track"])
    g.add((Track, RDF.type, ESW['Track']))
    track_name = " ".join([track_type,year,"Track"])
    g.add((Track, ESW['description'], Literal(track_name, datatype=XSD.string)))
    g.add((Track, RDFS.label, Literal(track_name, 'en')))
    index=0
    executions = 0
    for filename in files:
        topic = files[filename]['topic']
        name = files[filename]['name']
        worker = files[filename]['worker']
        macro_topic = files[filename]['macro_topic']
        hash_topic = hashlib.md5(topic.encode()).hexdigest()[:10]
        # create the URI for the current topic
        Topic = URIRef(ESWR["TOPIC"+hash_topic])
        # add the topic with all the tasks to the graph G
        topics.append(topic)
        # Add triples using store's add() method.
        g.add((Topic, RDF.type, ESW['SearchTopic']))
        # add the description
        g.add((Topic, ESW['description'], Literal(topic, datatype=XSD.string)))
        g.add((Topic, RDFS.label, Literal(topic, 'en')))
        # add the macro topic
        g.add((Topic, ESW['macroTopic'], Literal(macro_topic, datatype=XSD.string)))
        # add the link to the Track
        g.add((Topic, ESW['partOf'], Track))
        
        if topic in gt_map:
            # add the link to the Ground Truth
            GroundTruth = URIRef(ESWR[gt_map[topic]])
            g.add((GroundTruth, RDF.type, ESW['GroundTruth']))
            g.add((Topic, ESW['hasGroundTruth'], GroundTruth))
        
        # add the search tasks
        goals = files[filename]['goals']
        # keep the URI of the Tasks saved to use later
        tasks = {}
        for goal in goals:
            no_hashed_goal = topic+goal
            hash_goal = hashlib.md5(no_hashed_goal.encode()).hexdigest()[:10]
            Task = URIRef(ESWR["TASK"+str(hash_goal)])
            tasks[goal] = Task
            ## add the Tasks
            g.add((Task, RDF.type, ESW['SearchTask']))
            g.add((Task, ESW['description'], Literal(goals[goal], datatype=XSD.string)))
            g.add((Task, RDFS.label, Literal(goals[goal], 'en')))
            g.add((Task, ESW['number'], Literal(str(goal), datatype=XSD.string)))
            g.add((Task, ESW['belongsTo'], Topic))


        ## add the search workflow
        Workflow = URIRef(ESWR[name])
        h.add((Workflow, RDF.type, ESW['SearchWorkflow']))
        # add the related topic
        h.add((Workflow, ESW['implements'], Topic))

        #create the Worker
        Worker = URIRef(ESWR["WORKER"+str(worker)])
        h.add((Workflow, ESW['wroteBy'], Worker))

        if worker not in workers:
            ## add the Worker
            workers.append(worker)
            h.add((Worker, RDF.type, ESW['Worker']))
            h.add((Worker, RDFS.label, Literal("WORKER"+str(worker), 'en')))
            h.add((Worker, ESW['quality'], Literal(workers_grade[worker], datatype=XSD.float)))
            ## add also the score of the worker given is exam score

        search_workflow = files[filename]['search_workflow']
        for job in search_workflow:
            # the Job's URI is the concatenation of [JOB, number of the task, W, name of the file]
            Job = URIRef(ESWR['JOB'+str(job).replace(".","")+'W'+name])
            h.add((Job, RDF.type, ESW['SearchJob']))
            # add the relation hasPart to the search workflow
            h.add((Workflow, ESW['hasPart'], Job))
            # add the relation performs to the search task
            h.add((Job, ESW['performs'], tasks[goal]))
                
            # add the information of the score of the job (fscore max and #queries)
            
            max_fscore = max([ q['fscore'] if 'fscore' in q else 0.0 for q in search_workflow[job] ])
            h.add((Job, ESW['fscore'], Literal(max_fscore, datatype=XSD.float)))
            h.add((Job, ESW['numberOfQueries'], Literal(len(search_workflow[job]), datatype=XSD.integer)))
                
                
            # add the query list
            Queries = BNode()
            h.add((Queries, RDF.type, RDF.List))
            h.add((Job, ESW['queries'], Queries))


            ## create the list of the query

            for i in range(len(search_workflow[job])):
                query = search_workflow[job][i]
                if 'narrative' in query:
                    narrative = query['narrative']
                text = query['query']
                Query = URIRef(ESWR['Q'+str(index)])
                h.add((Query, RDF.type, SP['Query']))
                h.add((Query, SP['text'], Literal(text, datatype=XSD.string)))
                # add the parse Error if it exists
                if 'parseError' in query and query['parseError'] is not None:
                    h.add((Query, LSQV['parseError'], Literal(query['parseError'], datatype=XSD.string)))
                # add the narrative if it exists
                if 'narrative' in query and query['narrative'] is not None:
                    h.add((Query, ESW['narrative'], Literal(query['narrative'], datatype=XSD.string)))
                # add the size of the result set if it exists
                if 'output' in query and query['output'] is not None:
                    h.add((Query, LSQV['resultSize'], Literal(str(len(query['output'])), datatype=XSD.long)))
                # add the index of the query if it exists
                if 'index' in query:
                    h.add((Query, ESW['index'], Literal(query['index'], datatype=XSD.integer)))
                

                # add the metrics
                metrics = ['recall','precision','accuracy','fscore']
                for m in metrics:
                    if m in query and query[m] is not None:
                        h.add((Query, ESW[m], Literal(query[m], datatype=XSD.float)))
                # add the executions
                # example: "22/Dec/2022:19:41:16"
                if 'execution' in query:
                    for ex in query['execution']:
                        t_ex = datetime.strptime(ex['datetime'],'%d/%b/%Y:%H:%M:%S',).strftime('%Y-%m-%dT%H:%M:%S')
                        Execution = URIRef(ESWR['EX'+str(executions)])
                        h.add((Execution, RDF.type, LSQV['Execution']))
                        g.add((Query, DCT['issued'], Literal(t_ex, datatype=XSD.dateTime)))
                        executions+=1
                ## add the keywords
                if 'keywords' in query:
                    for key in query['keywords']:
                        if query['keywords'][key]==1:
                            ## add the edge
                            Keyword = URIRef(ESWR["".join(key.split())])
                            h.add((Query, LSQV['usesFeature'], Keyword))

                h.add((Queries, RDF.first, Query))
                if i < len(search_workflow[job])-1:
                    Next = BNode()
                    h.add((Next, RDF.type, RDF.List))
                    h.add((Queries, RDF.rest, Next))
                    Queries = Next
                else:
                    h.add((Queries, RDF.rest, RDF.nil))
                index+=1
    # print the data for the topics in the Turtle format
    ttlname = rdf_folder+str(year)+'topics.ttl'
    print("--- saving serialization for the topics ---")
    g.serialize(destination=ttlname, format='turtle')
    
    ttlname = rdf_folder+str(year)+'workflows.ttl'
    print("--- saving serialization for the workflows ---")
    h.serialize(destination=ttlname, format='turtle')


    
def main(config_file):
    #load properties
    configs = Properties()
    with open(config_file, 'rb') as config_file:
        configs.load(config_file)
    verbose = configs.get("verbose").data
    if verbose == None:
        verbose = False
    elif verbose.lower() == 'true':
        verbose = True
    elif verbose.lower() == 'false':
        verbose = False
    print(verbose)
    files = load_json(configs.get("evaluations").data,True)
    rdf_folder = configs.get("rdf").data
    if not os.path.exists(rdf_folder):
        os.makedirs(rdf_folder)
    export_turtle(configs.get("keywords").data,configs.get("workers").data,configs.get("gt_map").data,rdf_folder,files,configs.get("track_type").data,configs.get("year").data)

if __name__ == "__main__":
    main('config.properties')