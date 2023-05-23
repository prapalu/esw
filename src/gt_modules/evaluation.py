'''To save the results found by this ground truth we are going to create a JSON object. Before creating the object we have to identify this workflow. All the workflows are indexed in the script notebook when we ran the statistics and we saved a csv file that contains all the workflows' name and the related index. This file is saved in `/indexes/workflows.csv`. Before starting to run the queries of the ground truth, we have to find the name of the current workflow (always in the second cell of the notebook) and then reading the csv file of the indexes find the related index. In this way we always know which notebook we are talking about. The results found in a ground truth will be store in the folder `/results/` with the name that is **workflow{index}.json** where index is the related index found in the csv file of the indexes. 

The JSON object is composed by:
- name of the workflow
- results' object

The results' object is a dictionary with keys the number of the goal of the workflow and value the expected result
The result of each goal can be of two types:
- **single** when the result is well known, for example it is a specific `URI` or more than one. Then there is an array of objects that correspond to the expected result. Every object can be composed by different field, usually an URI and the related name. When there is more than one element inside the values array, it must be specified if the expected result is the whole set of elements in the array or it is necessary to find only one of those elements
- **set** when the result is more then one elements and it is not well defined, that is when there is not a query that provide only the wanted results. Also in this case there is an array of objects that correspond to the expected result.
There is also another field that specify the type of the check that must be done in the evaluation in order to determine if the student find the expected result. Usually we want to verify `URIs` but it can happen that the results are numbers or names. This is helpful in the evaluation phase because we know exactly what to compare to evaluate the student's notebook.
'''

##before start set some variables to save the result
#open this notebook as json
import os
import json
import pandas as pd
from pathlib import Path

global work_filepath
global result_path
## define constant variable
global TYPE_SET
TYPE_SET = "set"
global TYPE_SINGLE
TYPE_SINGLE = "single"
global TYPE_REFERRED
TYPE_REFERRED = "referred"
#define some paths
parent = str(Path(os.getcwd()).parent.absolute())
work_filepath = parent+os.sep+"indexes/workflows.csv"
#work_filepath = "/locale/data/jupyter/prando/notebook/sparqlthesis/indexes/workflows.csv"
result_path = parent+"/gt_json"

def setup_indexes(index):
    global work_filepath
    work_filepath = index

def setup(filepath):
    #create the directory results if not exist
    if not os.path.exists(result_path):
        os.mkdir(result_path)
    # get the name 
    source = get_source(filepath)
    # get the index
    index = get_index_workflow(filepath)
    # create the first json file
    create_json(index,source)
        
## load the source (name - topic) of the ground truth given the path to the file
def get_source(filepath):
    data = json.load(open(filepath))
    #get the list of the cells 
    df = pd.DataFrame(data['cells'])
    #get the first line of the cells that tells me the title of the notebook
    source = df['source'][2][0].replace("\n","").replace("#","").strip()
    return source

def get_work_filename(index_work):
    # this variable contains the filepath of the ground truth's json object of this workflow
    return result_path+os.sep+"workflow"+str(index_work)+".json"
    

def get_index_workflow(ipname_path):
    # get the name 
    source = get_source(ipname_path)
    ### source contains the name of the workflow

    #read the workflow indexes
    workflow_indexes = pd.read_csv(work_filepath)

    # this variable will contain the index of this workflow
    index_workflow = -1
    for index, row in workflow_indexes.iterrows():
        if row["name"] == source:
            index_workflow = str(row["macro"])+"_"+str(row["index"])
    if index_workflow == -1:
        print("ERROR: WORKFLOW DOES NOT EXIST IN THE INDEXES")
    else:
        print("The index of this workflow is:",index_workflow)
    return index_workflow
    
#value is always an array of element
#any_all is a string value that must be "any" or "all"
def add_result(index_work,goal_num, type_ , check ,value, any_all = None ,type_inside = None, elements_per_tuple = 1):
    
    # check if the json already exists
    path = get_work_filename(index_work)
    print("The path is",path)
    if not os.path.exists(path):
        return "Please create the JSON with the command create_json(index_work,source) before adding results"
    
    #load the current dict
    dict_ = json.load(open(path))
    result = {}
    if "results" in dict_:
        result = dict_["results"]
    
    # add the object in the dictionary
    # create the current dictionary for the specific goal, or get it if it already exists from the big JSON object
    current_dict = {}
    if goal_num in result:
        current_dict = result[goal_num]
    
    
    if type_ == TYPE_SET:
        ## the result is a set of element, so is not well define
        current_dict["type"] = type_
        current_dict["check"] = check
        current_dict["values"] = value
    elif type_ == TYPE_SINGLE:
        ## the result is well defined, it is one or more than one element and it must be set the any_all field
        current_dict["type"] = TYPE_SINGLE
        current_dict["check"] = check
        if any_all is not None and check != "ask":
            current_dict["any_all"] = any_all
        current_dict["values"] = value
    elif type_ == TYPE_REFERRED:
        current_dict["type"] = type_
        current_dict["check"] = check
        current_dict["elements_per_tuple"] = elements_per_tuple
        current_dict["values"] = value
        
        
    ## put the current dictionary for the specific goal in the result's object inside the JSON object
    result[goal_num] = current_dict
    ## put the result's object in the JSON object
    dict_["results"] = result
    
    ## save the JSON object
    fd = open(get_work_filename(index_work),"w")
    json.dump(dict_, fd)
    fd.close()
    
    print("JSON object updated")
    
def create_json(index_work,source):
    if not os.path.exists(get_work_filename(index_work)):
        dict_ = {"description":source}
        fd = open(get_work_filename(index_work),"w")
        json.dump(dict_, fd)
        fd.close()