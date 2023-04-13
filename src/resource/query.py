import resource.utils as utils
import json
import numpy as np
import pandas as pd

def get_number_of_goal(text):
    text = utils.format_string(text)
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
                f = utils.format_string(it)
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
                ret+=" "+lines[ind][:lines[ind].find("#")].strip()
            ind+=1
        #append the last line if there is something
        ret+=" "+lines[ind].replace("\"\"\"","").strip()
    else:
        ret = st[1:-1]
    return ret.replace("\\\"","\"").strip()

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
            # code cells. Looking for the queries
            for it in row.source:
                if not count:
                    continue
                if "run_query" in str(it).lower():
                    ##run query command --> extract the query
                    param = get_function_parameter(it)
                    query_str = get_query_text(container,param)
                    #append the string in the list of queries of the related goal
                    if actual_goal not in query_dict:
                        query_dict[actual_goal] = [query_str]
                    else:
                        query_dict[actual_goal].append(query_str)
                    container = []
                elif "run_ask_query" in str(it).lower():
                    ##run ask query command --> extract the query
                    param = get_function_parameter(it,True)
                    query_str = get_query_text(container,param)
                    #append the string in the list of queries of the related goal
                    if actual_goal not in query_dict:
                        query_dict[actual_goal] = [query_str]
                    else:
                        query_dict[actual_goal].append(query_str)
                    container = []
                else:
                    container.append(it)
    ## at then end return the object
    return query_dict