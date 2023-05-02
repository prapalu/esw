import numpy as np
import pandas as pd
import json
import os
from functools import reduce 
import resource.logs as logs

global nbks_dir
global json_dir
global people_dir

## function to setup the folder of notebooks
def setup_nb_folder(folder,verbose = False):
    global nbks_dir
    nbks_dir = folder
    if verbose:
        print("Notebook folder set at: ",folder)

## function to setup the folder of notebooks
def setup_json_folder(folder,verbose = False):
    global json_dir
    json_dir = folder
    if verbose:
        print("Folder set where storing JSON notebooks at: ",folder)


        
# people_dir is a dictionary with keys the folders of the people and values the list of the notebooks of that people
# 
# nbks_dir is the notebooks directory

def load_notebooks(verbose = False):
    global people_dir
    #initialize list of folders
    people_dir = {}
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
        
# same as load_notebooks, but it loads json files
def load_json_notebooks(verbose = False):
    #popolate people_dir list
    global people_dir
    global json_dir
    people_dir={}
    for folder in os.listdir(json_dir):
        subdir = json_dir + os.sep + folder
        nbks = []
        for file in os.listdir(subdir):
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                nbks.append(filepath)
            people_dir[folder] = nbks
    if verbose:
        string = "Successfully load the json notebooks from the folder "+str(json_dir)+":\n"
        string += "--> Original number of students: "+str(len(os.listdir(json_dir)))+"\n"
        string += "--> Actual number of students: "+str(len(people_dir))+"\n"
        string += "--> Total number of notebooks: "+str(sum([len(people_dir[x]) for x in people_dir]))
        print(string)
    

# ### Notebook Conversion

def convert_nb(verbose = False):
    global json_dir
    global people_dir

    if not os.path.exists(json_dir):
        os.mkdir(json_dir)
    for p in people_dir:
        stud_dir = json_dir+os.sep+p
        if not os.path.exists(stud_dir):
            os.mkdir(stud_dir)
        for j in people_dir[p]:
            nb_name = get_notebook_name(j).split(".")[0]
            topic = get_topic(j)
            macro = get_macro_topic(topic)
            goals = find_workflow_goals(j)
            dictionary = query_extractor(j,goals)
            #create json final object
            json_obj = {}
            json_obj["macro_topic"] = macro
            json_obj["topic"] = topic
            json_obj["worker"] = get_student_id(j)
            json_obj["goals"] = goals
            #json_obj["query_log"] = get_num_query_log(nb)
            #json_obj["filepath"] = j
            json_obj["name"] = nb_name
            json_obj["exploratory_workflow"] = dictionary

            filename = stud_dir+os.sep+nb_name+".json"
            fd = open(filename,"w")
            json.dump(json_obj, fd)
            fd.close()
    if verbose:
        print("Notebooks converted at",json_dir)
        
# function to associate executions from the logs to the notebooks
# people_dir is a dictionary with the json filepaths
def associate_logs(people_dir,code_list,verbose):
    if verbose:
        print("Start to associate logs to existing json files")
    for p in people_dir:
        for nb in people_dir[p]:
            # load the json notebook
            fd = open(nb,"r")
            file = json.load(fd)
            fd.close()
            # skip notebooks with no queries in the logs
            if file["name"] not in code_list:
                continue
            map_ = logs.map_query_into_dict(code_list[file["name"]])
            check = []
            for goal in file["exploratory_workflow"]:
                #check+=[query['query'] in map_ for query in file["exploratory_workflow"][goal]]
                for index in range(len(file["exploratory_workflow"][goal])):
                    if file["exploratory_workflow"][goal][index]['query'] in map_:
                        ## add the execution
                        file["exploratory_workflow"][goal][index]['execution'] = [{'datetime':d} for d in map_[file["exploratory_workflow"][goal][index]['query']]]
                    #print(query['query'] in map_)
                    #print(query['query'])
                #break
            fd = open(nb,"w")
            json.dump(file, fd)
            fd.close()
            #print(check)
    if verbose:
        print("Finished to associate logs to existing json files")
        
        

#return the student ID from the filepath of the notebook
def get_student_id(file):
    return file.split("/")[-2].replace("M","")

#return the name of the notebook file from the filepath
def get_notebook_name(file):
    return file.split("/")[-1]

def format_string(text):
    return text.strip().replace('\n','')

## divide the name of the workflow to get the MACRO - TOPIC
def get_macro_topic(name):
    return name.split(" ")[0].strip()

def get_topic(file):
    data = json.load(open(file))
    #get the list of the cells 
    df = pd.DataFrame(data['cells'])
    #get the first line of the cells that tells me the title of the notebook
    topic = df['source'][2][0].replace("\n","").replace("#","").strip()
    return topic

def get_number_of_goal(text):
    text = format_string(text)
    i = text.split(" ")[0]
    a = text[len(i):].strip()
    if i.endswith("."):
        i = i[0:-1]
    return i,a


def find_workflow_goals(notebook): 
    goals = {}
    #open the notebook
    data = json.load(open(notebook))
    #get the list of the cells 
    df = pd.DataFrame(data['cells'])
    reading = False
    for row in df.itertuples():
        for it in row.source:
            if reading:
                #skip blank lines
                f = format_string(it)
                if f=='':
                    continue
                #print(f)
                i,a = get_number_of_goal(f)
                goals[i] = a
            if "workload should" in str(it).lower() or "workload goals" in str(it).lower():
                #read the goals of the notebook
                reading = True
                #print(row)
        if reading:
            return goals
    return goals


## this function return the string of the query given a list of lines of code and the name of the variable
def get_query_text(lines, variable):
    ind = len(lines)-1
    while ind >= 0 and variable not in lines[ind]:
        ind-=1
    ## ind contains the index of the lines where there is the name of the variable
    st = lines[ind].replace(variable,"").replace("=","").strip()
    #print("ST",st)
    ret = ""
    if "\"\"\"" in st or  "f\"\"\"" in st:
        #put the first line if student starts to write the query right after """
        if "f\"\"\"" in st:
            ret = st.replace("f\"\"\"","")
        else:
            ret = st.replace("\"\"\"","")
        ind+=1
        #append each line (separate with a space) until we reach """
        #be careful about comment. In each line if a sharp is found, skip everything that follows the character
        while ind < len(lines) and "\"\"\"" not in lines[ind]:
            if lines[ind].find("#") == -1:
                ret+=" "+lines[ind].strip()
            else:
                ## need to check if it is a PREFIX line
                split_sharp = lines[ind].split("#")
                # PREFIX condition
                if lines[ind].strip().upper().startswith("PREFIX") and (split_sharp[1].strip())[0] == ">":
                    # it is a prefix, so keep the entire line
                    ret+=" "+lines[ind].strip()
                else:
                    remain = lines[ind][:lines[ind].find("#")].strip()
                    if remain != "":
                        ret+=" "+remain
            ind+=1
        #append the last line if there is something
        ret+=" "+lines[ind].replace("\"\"\"","").strip()
    else:
        ret = st[1:-1]
    ret = ret.replace("\\\"","\"").strip()
    return " ".join(ret.split())

## this function return the string of the comments of the query
def get_query_narrative(lines, variable):
    ind = 0
    while ind < len(lines) and variable not in lines[ind]:
        ind+=1
    narr = ""
    # iterate over rows before the query
    for i in range(ind):
        if lines[i].strip().startswith("#"):
            narr+="\n"+lines[i].strip().replace("#","").strip()
    return narr.strip()


#this function return the name of the variable use in the run_query command
def get_function_parameter(line, ask = False):
    line = line.strip()
    offset = 10
    name = "run_query"
    if ask:
        offset = 14
        name = "run_ask_query"
    line = line[line.index(name)+offset:]
    line = line.strip()
    return line[:line.index(")")]

#return a dictionary of queries
def query_extractor(notebook,goals):
    #open the notebook
    data = json.load(open(notebook))
    #get the list of the cells 
    df = pd.DataFrame(data['cells'])
    
    #skip the assignment cells of the notebook
    count = False
    
    #contains a list of lines of code. When the run_query command is found, go back in that list and find the related query
    container = []
    #the actual goal that student is analyzing
    actual_goal = ""
    #the dictionary of the queries
    query_dict = {}
    
    
    for row in df.itertuples():
        if row.cell_type == "markdown":
            for it in row.source:
                ## verify if we can start to consider the cells
                if "useful uri" in str(it).lower():
                    count = True
                elif count:
                    #looking for a markdown cell that tells me which task people are doing
                    if "task" in str(it).lower():
                        task_line = str(it).lower()[(str(it).lower().index("task")+5):]
                        for g in goals:
                            if task_line.startswith(g):
                                #task found
                                actual_goal = g
        elif row.cell_type == "code":
            # code cells. Looking for the output
            new_output=[]
            parseError = None
            if len(row.outputs) > 0 and 'text' in row.outputs[0]:
                # get the ouput text of the cell 
                
                output = row.outputs[0]['text']
                if (len(output)==2 and "Empty" in output[1]):
                    # empty result set
                    new_output=[]
                else:
                    # handle bad queries 
                    if len(output) < 2:
                        parseError = "Output not found"
                        if "Results\n" not in output[0]:
                            parseError = output[0].replace("\n","")
                    elif "The history saving thread hit" in output[1]:
                        parseError = output[1].replace("\n","")
                    elif "The operation failed QueryBadFormed:" in output[1]:
                        parseError = output[1].replace("\n","")
                    elif "The operation failed EndPointInternalError: endpoint returned code 500 and response." in output[1]:
                        parseError = output[1].replace("\n","")
                    else:
                        try:
                            # results exist, remove the first line ("Results") and the last (# of results)
                            output = output[1:-1]
                            new_output = [eval(x) for x in output]
                        except:
                            print("Error on file ",notebook,": Probably more queries in the same cell")
            if parseError is not None:
                new_output = None
            # code cells. Looking for the queries
            for it in row.source:
                if not count:
                    continue
                if "run_query" in str(it).lower():
                    ##run query command --> extract the query
                    param = get_function_parameter(it)
                    query_str = get_query_text(container,param)
                    query_narrative = get_query_narrative(container,param)
                    query_exp = {"narrative":query_narrative,"query":query_str,"output":new_output,"parseError":parseError}
                    #append the string in the list of queries of the related goal
                    if actual_goal not in query_dict:
                        query_dict[actual_goal] = [query_exp]
                    else:
                        query_dict[actual_goal].append(query_exp)
                    container = []
                elif "run_ask_query" in str(it).lower():
                    ##run ask query command --> extract the query
                    param = get_function_parameter(it,True)
                    query_str = get_query_text(container,param)
                    query_exp = {"query":query_str,"output":new_output,"parseError":parseError}
                    #append the string in the list of queries of the related goal
                    if actual_goal not in query_dict:
                        query_dict[actual_goal] = [query_exp]
                    else:
                        query_dict[actual_goal].append(query_exp)
                    container = []
                else:
                    container.append(it)
    ## at then end return the object
    return query_dict


def load_execution(directory,verbose = False):
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
        string = "Successfully load the json executions from the folder "+str(directory)+":\n"
        string += "--> Total number of files: "+str(len(files))
        print(string)
    return files

def associate_execution(execution_dir,verbose = False):
    global json_dir
    # load the current json
    work_conv = load_execution(json_dir)
    # load the execution
    work_exec = load_execution(execution_dir)

    c=0
    notc=0
    for worker in work_conv:
        for f in work_conv[worker]:
            ref = None
            if worker in work_exec and f['name'] in [x['name'] for x in work_exec[worker]]:
                for x in work_exec[worker]:
                    if x['name'] == f['name']:
                        ref = x

            for g in f['exploratory_workflow']:
                for index in range(len(f['exploratory_workflow'][g])):
                    if 'execution' not in f['exploratory_workflow'][g][index]:
                        f['exploratory_workflow'][g][index]['execution'] = []
                        
                    if ref is not None and ref['search_workflow'][g][index]['query'] == f['exploratory_workflow'][g][index]['query']:
                        execu = ref['search_workflow'][g][index]['execution']
                        if execu['execution_time'] > 0.0:
                            c+=1
                            new_obj = {'datetime':execu['execution_timestamp'],'duration':execu['execution_time']}
                        else:
                            notc+=1
                            new_obj = {'datetime':execu['execution_timestamp']}
                        f['exploratory_workflow'][g][index]['execution'].append(new_obj)
                        if execu['execution_error'] is not None:
                            f['exploratory_workflow'][g][index]['parseError'] = execu['execution_error']
                        else:
                            f['exploratory_workflow'][g][index]['parseError'] = None
                        f['exploratory_workflow'][g][index]['execution_output'] = execu['execution_output']
            filepath = json_dir+os.sep+worker+os.sep+f['name']+".json"
            fd = open(filepath,"w")
            json.dump(f, fd)
            fd.close()
    #sprint(c,notc)