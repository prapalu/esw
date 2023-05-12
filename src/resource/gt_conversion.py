import numpy as np
import pandas as pd
import json
import os
from functools import reduce 
import resource.logs as logs
import resource.conversion as conversion
import gt_modules.evaluation as gt_mod

global gt_dir
global gt_converted_dir
global gt_nbks_dir

## function to setup the folder of notebooks
def setup_nb_folder(folder,verbose = False):
    global gt_nbks_dir
    gt_nbks_dir = folder
    if verbose:
        print("Notebook folder set at: ",folder)

## function to setup the folder of notebooks
def setup_json_folder(folder,verbose = False):
    global gt_converted_dir
    gt_converted_dir = folder
    if verbose:
        print("Folder set where storing JSON notebooks at: ",folder)

## setup the file for indexes
def setup_indexes(index,verbose=False):
    gt_mod.setup_indexes(index)


''' 
since it already exists the folder gt_json which contains the ground truths for the evaluation,
all the grount truths will be converted and stored under the folder ground_truths/converted
such as a simple Workflow. The division by their macro-topic will be preserved
'''
def convert_gt_nb(verbose = False):
    global gt_converted_dir
    global gt_dir

    if not os.path.exists(gt_converted_dir):
        os.mkdir(gt_converted_dir)
    for p in gt_dir:
        macro_dir = gt_converted_dir+os.sep+p
        if not os.path.exists(macro_dir):
            os.mkdir(macro_dir)
        for j in gt_dir[p]:
            #nb_name = get_notebook_name(j).split(".")[0]
            nb_name = "workflow"+gt_mod.get_index_workflow(j)
            topic = conversion.get_topic(j)
            macro = conversion.get_macro_topic(topic)
            goals = conversion.find_workflow_goals(j)
            dictionary = conversion.query_extractor(j,goals)
            #create json final object
            json_obj = {}
            json_obj["macro_topic"] = macro
            json_obj["topic"] = topic
            json_obj["goals"] = goals
            #json_obj["query_log"] = get_num_query_log(nb)
            #json_obj["filepath"] = j
            json_obj["name"] = nb_name
            json_obj["exploratory_workflow"] = dictionary

            filename = macro_dir+os.sep+nb_name+".json"
            fd = open(filename,"w")
            json.dump(json_obj, fd)
            fd.close()
    if verbose:
        print("Notebooks converted at",gt_converted_dir)
        
def load_gt_notebooks(verbose = False):
    global gt_dir
    #initialize list of folders
    gt_dir = {}
    #popolate gt_dir list
    for folder in os.listdir(gt_nbks_dir):
        if os.path.isdir(gt_nbks_dir+os.sep+folder) and not folder.startswith(".") and folder not in gt_dir:
            subdir = gt_nbks_dir + os.sep + folder
            nbks = []
            for file in os.listdir(subdir):
                filepath = subdir + os.sep + file
                if filepath.endswith(".ipynb") and not file.startswith("._"):
                    nbks.append(filepath)
            if len(nbks)>0:
                gt_dir[folder] = nbks
    if verbose:
        print("Total people: "+str(len(gt_dir)))