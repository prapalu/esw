import resource.utils as utils
import json
import resource.query as qu
import resource.notebooks as nbks
import resource.statistics as res_stats
import resource.logs as logs
import os
import numpy as np
import resource.sparql_setup as virtuoso

## define constant variable
global TYPE_SET
TYPE_SET = "set"
global TYPE_SINGLE
TYPE_SINGLE = "single"
global TYPE_MULTIPLE
TYPE_MULTIPLE = "multiple"
global CHECK_URI
CHECK_URI = "uri"
global CHECK_ASK
CHECK_ASK = "ask"

global EVALUATION_FOLDER
global RESULTS_FOLDER

def setup_evaluation_folder(folder, verbose = False):
    global EVALUATION_FOLDER
    EVALUATION_FOLDER = folder
    if not os.path.exists(EVALUATION_FOLDER):
        os.mkdir(EVALUATION_FOLDER)
        if verbose:
            print("Evaluation folder created and set up at",EVALUATION_FOLDER)
    if verbose:
        print("Evaluation folder set up at",EVALUATION_FOLDER)

def setup_results_folder(folder, verbose = False):
    global RESULTS_FOLDER
    RESULTS_FOLDER = folder
    if not os.path.exists(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
        if verbose:
            print("Results folder created and set up at",RESULTS_FOLDER)
    if verbose:
        print("Results folder set up at",RESULTS_FOLDER)
    

#result set is an array of array of tuples
#true_result is a dictionary with keys: type, check, values
def verify_result(result_set, true_result, ask = None):
    global TYPE_SET
    global TYPE_SINGLE
    global TYPE_MULTIPLE
    
    #this counts the number of matches in the true result set (ground truth)
    matches = 0
    
    #this keep track of the different elements found, to not count some elements twice
    element_found = []
    if true_result["type"] == TYPE_SINGLE:
        if type(true_result["check"]) == list:
            ## manage the list of possible values
            true_r_s = [[j[c] for c in true_result["check"]] for j in true_result["values"]]
            for res in result_set:
                #list of values of the row of the student's result set
                res_val = [t[1] for t in res]
                #iterate over the true result list
                for j in true_result["values"]:
                    #pick the true_r_s : at least one of that values must be in the result
                    true_r_s = [j[c] for c in true_result["check"]]
                    #verify if there is a reference to another value that must be present in the row of the student's result set
                    referred = "refers_to" in j or "refers_to_name" in j
                    
                    #the element is referred, check the presence of the referred element
                    if referred:
                        referred = False
                        if "refers_to" in j and j["refers_to"] in res_val:
                            referred = True
                        if "refers_to_name" in j and j["refers_to_name"] in res_val:
                            referred = True
                        if not referred:
                            continue
                    #check the presence of the element
                    if j not in element_found and any([x==y for x in true_r_s for y in res_val]):
                        matches+=1
                        element_found.append(j)
                '''for tre in true_r_s:
                    # the value to find is referred to another main object that it must be present in the result
                    referred = False
                    if "refers_to" in true_result["values"] and true_result["values"]["refers_to"] in res_val:
                        referred = True
                    if "refers_to_name" in true_result["values"] and true_result["values"]["refers_to_name"] in res_val:
                        referred = True
                    if ("refers_to" in true_result["values"] or "refers_to_name" in true_result["values"]) and not referred:
                        continue
                    if any([x==y for x in tre for y in res_val]):
                        matches+=1'''
        elif true_result["check"] == CHECK_ASK:
            ask_element = true_result["values"][0]
            ask_answer = ask_element["ask"]
            # verifico se ho ask query con risultato true o false
            if ask is not None:
                if ask==ask_answer:
                    return 1.0
                return 0.0
            
            ##verifico se ci sono almeno i parametri del confronto
            ## verifico se c'è una query che mi fornisce quei due risultati
            find = [False for i in range(0,len(ask_element["elements"]))]
            for res in result_set:
                #check if there is the uri or the name
                for item in range(0,len(find)):
                    if (ask_element["elements"][item]["uri"] in [t[1] for t in res] or ask_element["elements"][item]["name"] in [t[1] for t in res]):
                        ##verify if there is the value needed for the comparison
                        if ask_element["elements"][item][ask_element["check"]] in [t[1] for t in res]:
                            find[item] = True
            if all(find):
                return len(find)
        else :
            #I have to verify only one element, of type uri in the values
            true_uri = [x[true_result["check"]] for x in true_result["values"]]
            for res in result_set:
                for t_u in true_uri:
                    if t_u in [t[1] for t in res] and not t_u in element_found:
                        element_found.append(t_u)
                        matches += 1
        
    ## more than one result in a single task
    if true_result["type"] == TYPE_MULTIPLE:
        # result set 
        # mult_res contains an uri and a name that represent the main object of the result tuple
        mult_res = true_result["results"][0]["values"]
        # iterate over the student's result set
        for res in result_set:
            #iterate over the multiple true result set
            for val in mult_res:
                main_uri = val["uri"]
                main_name = val["name"]
                associate_values = val["value"]
                #verify if the main uri or the main name are contained in the tuple of the result set
                if main_uri in [t[1] for t in res] or main_name in [t[1] for t in res]:
                    # to obtain a score this tuple MUST contained also the elements in the associate_values
                    
                    # iterate over the associate values
                    #keep track of how many match I did 
                    inside_match = 0
                    for ass_key in associate_values:
                        # manage two type of element: list and single object
                        find_inside_element = False
                        if type(associate_values[ass_key]) == list:
                            #go through the list
                            for elem in associate_values[ass_key]:
                                #dictionary
                                if type(elem) == dict:
                                    elem_val = list(elem.values())
                                    for e_v in elem_val:
                                        if e_v in [t[1] for t in res]:
                                            ## found the element associated
                                            find_inside_element=True
                                else:
                                    #simple object
                                    if elem in [t[1] for t in res]:
                                        ## found the element associated
                                        find_inside_element=True
                            if find_inside_element:
                                inside_match+=1
                        elif type(associate_values[ass_key]) == dict:
                            elem_val = list(associate_values[ass_key].values())
                            found_val = []
                            for e_v in elem_val:
                                if e_v in [t[1] for t in res] and e_v not in found_val:
                                    ## found the element associated
                                    
                                    inside_match+=1
                                    found_val.append(e_v)
                    matches+=float(inside_match)/float(len(associate_values))
        
    if true_result["type"] == TYPE_SET and true_result["check"] == CHECK_URI:
        #I have to verify only one element, of type uri in the values
        true_uri = [x["uri"] for x in true_result["values"]]
        for res in result_set:
            for t_u in true_uri:
                if t_u in [t[1] for t in res] and not t_u in element_found:
                    element_found.append(t_u)
                    matches+=1
    return matches

##notebook evaluation that return a JSON with all the information
def evaluate_notebook(nb,goals,true_result, verbose = False):
    #get the index of the student
    index_stud = nbks.get_index_by_student(utils.get_student_id(nb))
    if verbose:
        print("Student",utils.get_student_id(nb),index_stud)

    #print("Reading notebook "+nb)
    dictionary = qu.query_extractor(nb,goals)
    evaluation={}
    for d in dictionary:
        #goal index
        index_goal = nbks.get_index_by_goal(goals,d)
        #skip if for this goal there is nothing to check
        if d not in true_result:
            continue
        #analyze query
        i_q = 0
        if verbose:
            print("Doing task",d)

        #this boolean is necessary after the for if the student did not find anything
        stud_find_something = False
        solutions = []
        for q in dictionary[d]:
            i_q+=1
            if verbose:
                print("Running query #"+str(i_q))
            #print(q)
            # manage ask query
            ask = None
            res = virtuoso.run_query(q)
            if res == None:
                continue
            if nbks.analyze_query(q)[1] == 1:
                ## it means that this is an ask query
                ask = res['boolean']

            #verification of the result
            verification = verify_result(res,true_result[d],ask)
            if true_result[d]["type"] == TYPE_SET and verification > 0:
                stud_find_something = True
                #compute the recall
                recall = float(verification)/float(len(true_result[d]["values"]))
                #compute the precision
                precision = float(verification)/float(len(res))

                #store the solution
                solutions.append({"recall":recall,"precision":precision,"query_num":i_q})
                
                if verbose:
                    print("Student find a set of",verification,"elements over a ground truth set of",len(true_result[d]["values"]),"elements after",i_q,"queries in a set of",len(res),"elements")
            elif true_result[d]["type"] == TYPE_MULTIPLE and verification > 0:
                stud_find_something = True
                #compute the recall
                recall = float(verification)/float(len(true_result[d]["results"][0]["values"]))
                #compute the precision
                precision = float(verification)/float(len(res))

                #store the solution
                solutions.append({"recall":recall,"precision":precision,"query_num":i_q})
                
                if verbose:
                    print("Student find a set of",verification,"elements over a ground truth set of",len(true_result[d]["values"]),"elements after",i_q,"queries in a set of",len(res),"elements")
            elif verification > 0 and true_result[d]["type"] == TYPE_SINGLE :
                stud_find_something = True

                # I have to distinguish between result in an ask query and the others.
                # the result in the ask query is inside
                recall = float(verification)/float(len(true_result[d]["values"]))
                if "any_all" in true_result[d] and true_result[d]["any_all"] == "any":
                    recall = 1.0
                elif true_result[d]["check"] == "ask" and ask is None:
                    # the true result set is inside the ask element inside values
                    recall = float(verification)/float(len(true_result[d]["values"][0]["elements"]))
                if ask is not None:
                    precision = float(verification)
                else:
                    #res cannot be empty since verification is greater than 0
                    precision = float(verification)/float(len(res))

                #store the solution
                solutions.append({"recall":recall,"precision":precision,"query_num":i_q})
                
                if verbose:
                    print("Student find the result after",i_q,"queries in a set of",len(res),"elements")
        ##manage the solutions found by the student
        ## add to the final JSON only the solution with highest (recall+precision)
        if len(solutions)==0:
            evaluation[d] = {"recall":0,"precision":0,"query_num":0}
        else:
            max_ = max(s["recall"]+s["precision"] for s in solutions)
            high_recall = 0
            for s in solutions:
                if s["recall"]+s["precision"] == max_ and s["recall"] > high_recall:
                    evaluation[d] = s
                    high_recall = s["recall"]
    if verbose:
        print(evaluation)
    print("-> Complete evaluation computation of",nb)
    return evaluation

### return the JSON object with all the statistics about keywords usage
def compute_notebook_stats( nb, goals, topic, verbose = False):
    #get the student id from the notebook's filepath
    stud = utils.get_student_id(nb)
    #get the index of the macro-topic
    index_macro = nbks.get_index_by_macro_topic(nbks.get_macro_from_sub_topic(topic))
    #get the number of total query done by the student
    all_q = res_stats.sum_query(nbks.solid[index_macro,nbks.get_index_by_sub_topic(topic),nbks.get_index_by_student(stud)])
    if verbose:
        print("Analyzing student",stud,"tot query in notebook",all_q)
    statistics = {}
    goals[""] = "Empty"
    for g in goals:
        #run the statistics
        stat = res_stats.do_statistics(topic = topic,student = stud, goal = g, verbose=False)
        tot_query = (res_stats.sum_query(nbks.solid[index_macro,nbks.get_index_by_sub_topic(topic),nbks.get_index_by_student(stud),nbks.get_index_by_goal(goals,g)]))
        # add the informations in the dictionary
        goal_stat = {"number":g,"description":goals[g],"queries":tot_query,"keywords":{}}
        
        for index in range(len(nbks.keywords)):
            goal_stat["keywords"][nbks.keywords[index]] = int(stat[index])
        if g!="":
            statistics[g] = goal_stat
        else:
            statistics["0"] = goal_stat
        
        
        if verbose:
            print("Goal",g,goals[g],"Tot queries:",tot_query)
            print(stat)
            print("\n")
    ## overall
    stat = res_stats.do_statistics(topic = topic,student = stud, verbose=False)
    goal_stat = {"description":"overall","queries":all_q,"keywords":{}}

    for index in range(len(nbks.keywords)):
        goal_stat["keywords"][nbks.keywords[index]] = int(stat[index])

    statistics["overall"] = goal_stat
    goals.pop("")
    print("-> Complete statistics computation of",nb)
    return statistics

## compute the analysis of the notebooks
def compute_analysis( ):
    global RESULTS_FOLDER
    
    for macro in nbks.workflows:
        for w in nbks.workflows[macro]:
            index_work = nbks.get_index_by_sub_topic(w)
            index_macro = nbks.get_index_by_macro_topic(macro)
            #analyze directors
            
            if index_macro<5:
                continue
            
            work_path = RESULTS_FOLDER+os.sep+"workflow"+str(index_macro)+"_"+str(index_work)+".json"
            evaluation = []
            print(work_path)
            
            try:
                true_result = json.load(open(work_path))["results"]
            except:
                true_result = None
                print("The file for this workflow does not exists")

            #find the goals of the notebook, necessary to determine the tasks
            goals = qu.find_workflow_goals(nbks.workflows[macro][w][0])
            #goals[""] = "Empty Goal"
            #iterate through the people
            for nb in nbks.workflows[macro][w]:
                print(nb)
                eval_dir = EVALUATION_FOLDER+os.sep+utils.get_student_id(nb)
                if not os.path.exists(eval_dir):
                    os.mkdir(eval_dir)
                eval_filepath = eval_dir+os.sep+"workflow"+str(index_macro)+"_"+str(index_work)+".json"

                #create json final object
                json_obj = {}
                
                json_obj["macro_topic"] = macro
                json_obj["topic"] = w
                json_obj["student"] = utils.get_student_id(nb)
                json_obj["goals"] = compute_notebook_stats(nb, goals, w)
                json_obj["query_log"] = logs.get_num_query_log(nb)
                json_obj["filepath"] = nb
                if true_result is not None:
                    evaluation = evaluate_notebook(nb,goals,true_result,verbose=False)
                    for key in evaluation:
                        if key not in json_obj["goals"]:
                            json_obj["goals"][key] = {}
                        json_obj["goals"][key]["evaluation"] = evaluation[key]
                fd = open(eval_filepath,"w")
                json.dump(json_obj, fd)
                fd.close()

                print("Complete student",utils.get_student_id(nb),"for workflow:",w)
    print("Analysis done")