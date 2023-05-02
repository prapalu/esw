import resource.sparql_setup as sparql
import resource.keywords as keywords
from jproperties import Properties
import sys
import json
import os

def load_json(directory,verbose = False):
    if verbose:
        print("Start to load files from:",directory)
    files={}
    for folder in os.listdir(directory):
        subdir = directory + os.sep + folder
        if not os.path.isdir(subdir):
            continue
        for file in os.listdir(subdir):
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                fd = open(filepath,"r")
                tmp = json.load(fd)
                fd.close()
                if tmp['worker'] not in files:
                    files[tmp['worker']] = []
                files[tmp["worker"]].append(tmp)
                
    if verbose:
        string = "Successfully load the json notebooks from the folder "+str(directory)+":\n"
        string += "--> Total number of files: "+str(len(files))
        print(string)
    return files

# execute single workflow
def execute_file(f,worker_path):
    print("\nSTART WOrkflow:",f['name'])
    # setup the code in the Prefix String
    sparql.setup_nb_code(f['name'])
    # initialize new workflow dictionary and copy main fields
    run_wf = {}
    run_wf['name'] = f['name']
    run_wf['topic'] = f['topic']
    run_wf['worker'] = f['worker']
    run_wf['macro_topic'] = f['macro_topic']
    # initialize search workflow dictionary 
    run_wf['exploratory_workflow']={}
    # iterate over goals
    for g in f['exploratory_workflow']:
        run_wf['exploratory_workflow'][g] = []
        # execute the queries
        for query in f['exploratory_workflow'][g]:
            # copy main fields of the query
            new_query = {'query':query['query']}
            # response is a dictionary containing "time", "output", "error","timestamp"
            resp = sparql.run_query(query['query'])
            # create the execution object
            execu = {'execution_time':resp["time"],'execution_output':resp["output"],'execution_error':resp["error"],'execution_timestamp':resp["timestamp"]}
            # add the object in the query dictionary
            new_query['execution'] = execu
            run_wf['exploratory_workflow'][g].append(new_query)
    print("Save Workflow",f['name'])
    if not os.path.exists(worker_path):
        os.makedirs(worker_path)
    file = open(worker_path+os.sep+f['name']+".json","w")
    json.dump(run_wf,file)
    file.close()

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
    # setup vars
    json_wf_folder = configs.get("json_notebook_dir").data
    executed_wf_folder = configs.get("json_executed_dir").data
    keywords.setup_keywords(configs.get("keywords").data,verbose )
    # load the workflows
    workflows = load_json(json_wf_folder)
    # run the program
    # create the main folder if it not exists
    if not os.path.exists(executed_wf_folder):
        os.makedirs(executed_wf_folder)
    # go over workers
    for worker in workflows:
        # go over workflows
        for f in workflows[worker]:
            # create worker folder
            worker_path = executed_wf_folder+os.sep+f['worker']
            # if it already exists, skip it. I don't want to re-execute
            if os.path.exists(worker_path+os.sep+f['name']+".json"):
                continue
            execute_file(f, worker_path)
if __name__ == "__main__":
    if len(sys.argv)!=2 or not sys.argv[1].endswith(".properties"):
        print("-- ERROR --")
        print("You must specify a .properties file in the command line. A suitable example is of execution is:\n")
        print("python executor.py config2022.properties\n")
        exit()
    main(sys.argv[1])