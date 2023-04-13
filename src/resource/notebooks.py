import numpy as np
import pandas as pd
import json
import os
from functools import reduce 
import resource.utils as utils
import resource.query as query

#define global variables
global keywords
global people_dir
global workflows
global solid

#return the list of all workflows name 
def get_all_workflows():
    global workflows
    return reduce(lambda a,b : a+b , [(list(workflows[w].keys())) for w in workflows])

#define bitmap
def setup_keywords(filepath,verbose = False):
    global keywords
    if verbose:
        print("Opening file",filepath)
    f = open(filepath, "r")
    keywords = f.read().split("\n")
    f.close()
    if verbose:
        print(keywords)
        
def setup_notebooks(nbks_dir,verbose = False):
    #initialize list of folders
    global people_dir
    people_dir = {}
    if verbose:
        print("Start scanning the folder at",nbks_dir)

    #popolate people_dir list
    for folder in os.listdir(nbks_dir):
        if folder.startswith("M") and folder not in people_dir:
            subdir = nbks_dir + os.sep + folder
            nbks = []
            for file in os.listdir(subdir):
                filepath = subdir + os.sep + file
                if filepath.endswith(".ipynb") and not file.startswith("._"):
                    nbks.append(filepath)
            people_dir[folder.replace("M","")] = nbks
    if verbose:
        print("Total people: "+str(len(people_dir)))

    #check if every folder contains 6 notebooks
    all_6 = True
    for p in people_dir:
        if len(people_dir[p]) != 6:
            all_6 = False
    if verbose:
        if all_6:
            print("All folders contains 6 notebooks")
        else:
            print("There are folder not containing 6 notebooks")
    
def setup_workflows(verbose = False):
    #workflows
    global workflows
    workflows = {}
    for p in people_dir:
        for j in people_dir[p]:
            #open the notebook
            data = json.load(open(j))
            #get the list of the cells 
            df = pd.DataFrame(data['cells'])
            #get the first line of the cells that tells me the title of the notebook
            source = df['source'][2][0].replace("\n","").replace("#","").strip()
            # marco topic
            macro_topic = utils.getMacroTopic(source)
            if macro_topic in workflows:
                # key macro topic exists
                if source in workflows[macro_topic] and not j in workflows[macro_topic][source]:
                    workflows[macro_topic][source].append(j)
                else:
                    workflows[macro_topic][source] = [j]
            else:
                # key does not exists
                workflows[macro_topic] = {}
                workflows[macro_topic][source] = [j]
                
def create_solid(verbose = False):
    global workflows
    global solid
    global keywords
    #number of macro-topic
    macro_topic = len(workflows)
    #find max number of sub-topics per macro-topic
    sub_topics = max([len(workflows[x]) for x in workflows])
    #find max number of workflows goals
    max_goals = 0
    max_student = len(people_dir.keys())
    max_queries = 0
    for i in get_all_workflows():
        #max student size
        macro = get_macro_from_sub_topic(i)
        size = len(workflows[macro][i])
        max_student = max(size,max_student)
        #max goals size
        if workflows[macro][i] is not None and len(workflows[macro][i]) > 0:
            goals = query.find_workflow_goals(workflows[macro][i][0])
            size = len(goals)
            max_goals = max(size,max_goals)
            for nb in workflows[macro][i]:
                dictionary = query.query_extractor(nb,goals)
                leng = sum(len(dictionary[g]) for g in dictionary)
                max_queries = max(max_queries,leng)
    max_goals+=1
    if verbose:
        print("Number of macro topic",macro_topic)
        print("MAX Number of sub topics",sub_topics)
        print("MAX Number of goals",max_goals)
        print("MAX Number of student",max_student)
        print("MAX Number of queries",max_queries)
    #define the big solid
    solid = np.zeros([macro_topic,sub_topics,max_student,max_goals,max_queries,len(keywords)],dtype= np.int32)
    
#notebooks analisys
#w is the topic --> index_by_topic
def popolate_solid(verbose = False):
    global solid
    if verbose:
        print("-> Start to analyze all the workflows")
    iteration = 0
    for w in get_all_workflows():
        iteration+=1
        macro = get_macro_from_sub_topic(w)
        index_macro = get_index_by_macro_topic(macro)
        index_work = get_index_by_sub_topic(w)
        
        if verbose:
            str_verb = "-> Analyzing workflow "+str(iteration)+". Informations:\n"
            str_verb+="----> Macro-topic name: "+macro+" index: "+str(index_macro)
            str_verb+="\n----> Sub-topic name: "+w+" index: "+str(index_work) 
            print(str_verb)
        #find the notebook goals
        goals = query.find_workflow_goals(workflows[macro][w][0])
        if verbose:
            str_verb = "----> Number of goals: "+str(len(list(goals.keys())))
            str_verb+="\n----> Number of students who worked on this workflow: "+str(len(workflows[macro][w]))
            print(str_verb)
        #print(index_work)
        for nb in workflows[macro][w]:
            index_stud = get_index_by_student(utils.get_student_id(nb))
            #print("Reading notebook "+nb)
            dictionary = query.query_extractor(nb,goals)
            for d in dictionary:
                #goal index
                index_goal = get_index_by_goal(goals,d)
                #analyze query
                i_q = 0
                #skip if the indexes are not correct
                if not (index_work>=0 and index_stud>=0 and index_goal>=0 ):
                    continue
                #print(index_work,index_stud,index_goal)
                for q in dictionary[d]:
                    #if index_work==5 and index_stud==3 and index_goal==9 and i_q==1:
                    #    print(q)
                    solid[index_macro,index_work,index_stud,index_goal,i_q] = analyze_query(q)
                    i_q+=1
    print("-> Analysis Done")
                
def print_workflows_informations():
    #print dictionary informations
    global workflows
    print("# different macro-topic: "+str(len(workflows.keys())))
    topics = {}
    for macro in workflows:
        print(("Macro Topic "+macro),'\n'.join((str(topic)+" # different workflows "+str(len(workflows[macro][topic]))) for topic in workflows[macro]), sep='\n')
        
def analyze_query(query, verbose = False):
    query = query.strip()
    global keywords
    bitmap = np.zeros(len(keywords),dtype=np.int32)
    #create the sublist for keywords with space and keywords with no space
    space = [k for k in keywords if " " in k and not k.startswith("NESTED")]
    no_space = [k for k in keywords if " " not in k]
    
    #analyze keywords with no space
    if verbose:
        print(bitmap)
    for actual_key in no_space:
        index = 0
        while actual_key in query.upper()[index:]:
            if verbose and actual_key == "GROUP_CONCAT":
                print(query.upper()[index:].index(actual_key))
            offset = query.upper()[index:].index(actual_key)
            if query[index+offset-1] != "?":
                if verbose:
                    print(keywords.index(actual_key))
                bitmap[keywords.index(actual_key)] = 1
                break
            index = query.upper()[index:].index(actual_key)+index+len(actual_key)
    if verbose:
        print(bitmap)
           
    #nested query
    if query.upper().startswith("SELECT") or query.upper().startswith("ASK"):
        index = 6
        if query.upper().startswith("ASK"):
            index = 3
        while "SELECT" in query.upper()[index:]:
            offset = query.upper()[index:].index("SELECT")
            if query[index+offset-1] != "?":
                if verbose:
                    print(keywords.index(actual_key))
                bitmap[keywords.index("NESTED QUERY")] = 1
                break
            index = query.upper()[index:].index("SELECT")+index+6
    if verbose:
        print(bitmap)
           
    #analyze keywords with space
    for actual_key in space:
        words = actual_key.split(" ")
        if words[0] in query.upper():
            string = query.upper()
            while string.find(words[0])>=0:
                string = string[(string.index(words[0])+len(words[0])):]
                string = string.strip()
                if string.startswith(words[1]):
                    if verbose:
                        print(keywords.index(actual_key))
                    bitmap[keywords.index(actual_key)] = 1
                    break
    if verbose:
        print(bitmap)
                    
    return bitmap


        
def get_info_keywords(bitmap, tot_query = None):
    global keywords
    val_max = max(len(x) for x in keywords)
    string = ""
    if tot_query == None:
        for i in range(0,len(keywords)):
            string+= ("{0:"+str(val_max)+"}").format(keywords[i])+" - "+"{0:6}".format(str(bitmap[i]))+"\n"
    else:
        for i in range(0,len(keywords)):
            string+= ("{0:"+str(val_max)+"}").format(keywords[i])+" - "+"{0:6}".format(str(bitmap[i]))+" - "+str(format_perc(bitmap[i]/tot_query))+"%\n"
    return string[:-1]

#utility to get the name of the macro-topic given the index
def get_macro_from_sub_topic(topic):
    if type(topic)==int:
        topic = get_topic_by_index(topic)
    for w in workflows:
        if topic in list(workflows[w].keys()):
            return w
    return None

def get_macro_topic_by_index(index):
    global workflows
    return list(workflows.keys())[index]
def get_index_by_macro_topic(topic):
    global workflows
    if topic not in list(workflows.keys()):
        return -1
    return list(workflows.keys()).index(topic)



#utility to get the name of the sub-topic given the macro-topic and the index of the subtopic
def get_sub_topic_by_index(macro_topic,index):
    global workflows
    if type(macro_topic)==int:
        #translate the index to words
        macro_topic = get_macro_topic_by_index(macro_topic)
    return list(workflows[macro_topic].keys())[index]
def get_index_by_sub_topic(topic):
    global workflows
    for macro in workflows:
        if topic not in list(workflows[macro].keys()):
            continue
        return list(workflows[macro].keys()).index(topic)
    return -1

#utility to get the number of the student given workflow index and student index
def get_student_by_index(index_stud):
    global people_dir
    return list(people_dir.keys())[index_stud]
def get_index_by_student(student):
    global people_dir
    if student not in list(people_dir.keys()):
        return -1
    return list(people_dir.keys()).index(student)

#utility for the goals
def get_index_by_goal(goals,num):
    if num == "":
        return 0
    if num not in list(goals.keys()):
        return -1
    return (list(goals.keys()).index(num)+1)
def get_goal_by_index(goals,index):
    if index == 0:
        return ""
    return list(goals.keys())[index-1]

#get the query text providing index_workflow, index_student and the index_goal and the index of the query
########################################################################################
################################################# TO CHECK!!!!! ########################
########################################################################################
def get_query_by_index(index_work,index_stud,index_goal,index):
    global workflows
    #find the relative topic
    topic = get_sub_topic_by_index(workflows,index_work)
    #find the goals
    goals_work = find_workflow_goals(workflows[topic][0])

    #query
    dictionary = query_extractor(workflows[topic][index_stud],goals_work)    
    go = get_goal_by_index(goals_work,index_goal)

    return dictionary[go][index]
########################################################################################
################################################# TO CHECK!!!!! ########################
########################################################################################

############### Function to get information on workflows and students ###############
#get all student that did a workflow
def get_student_from_workflow(workflow_name):
    global workflows
    macro = get_macro_from_sub_topic(workflow_name)
    if macro is None:
        return None
    return [get_student_id(x) for x in workflows[macro][workflow_name]]
#get all workflows did by one student
def get_workflows_from_student(student_id):
    global workflows
    name = [w if student_id in ([get_student_id(x) for x in workflows[get_macro_from_sub_topic(w)][w]]) else 0 for w in get_all_workflows()]
    return list(filter(lambda val: val !=  0, name) )