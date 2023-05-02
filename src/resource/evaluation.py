import resource.utils as utils
import resource.keywords as keywords
import json
import os
import numpy as np
from dateutil.parser import parse
import resource.sparql_setup as virtuoso

## define constant variable
global TYPE_SET
TYPE_SET = "set"
global TYPE_SINGLE
TYPE_SINGLE = "single"
global TYPE_REFERRED
TYPE_REFERRED = "referred"
global CHECK_URI
CHECK_URI = "uri"
global CHECK_ASK
CHECK_ASK = "ask"
global people_dir
global ground_truth
global eval_dir


# setup the evaluation folder
def setup_evaluation_folder(folder, verbose = False):
    global eval_dir
    eval_dir = folder
    if verbose:
        print("Set up evaluation directory at ",folder)

def load_json_notebooks(nbks_dir, verbose = False):
    #popolate people_dir list
    global people_dir
    people_dir={}
    for folder in os.listdir(nbks_dir):
        subdir = nbks_dir + os.sep + folder
        nbks = []
        for file in os.listdir(subdir):
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                nbks.append(filepath)
            people_dir[folder] = nbks
    if verbose:
        string = "Successfully load the json notebooks from the folder "+str(nbks_dir)+":\n"
        string += "--> Original number of students: "+str(len(os.listdir(nbks_dir)))+"\n"
        string += "--> Actual number of students: "+str(len(people_dir))+"\n"
        string += "--> Total number of notebooks: "+str(sum([len(people_dir[x]) for x in people_dir]))
        print(string)
        
def load_ground_truths(gt_dir, verbose = False):
    #popolate people_dir list
    global ground_truth
    ground_truth={}
    for file in os.listdir(gt_dir):
        filepath = gt_dir + os.sep + file
        if filepath.endswith(".json"):
            gt = json.load(open(filepath))
            description = gt['description'].replace("Workflow's name:","").strip()
            ground_truth[description] = gt['results']
    if verbose:
        string = "Successfully load the json ground truths from the folder "+str(gt_dir)+":\n"
        string += "--> Original number of ground truths: "+str(len(os.listdir(gt_dir)))+"\n"
        string += "--> Actual number of ground truths: "+str(len(ground_truth))
        print(string)


#result set is an array of array of tuples
#true_result is a dictionary with keys: type, check, values
def verify_result(result_set, true_result, ask = None):
    global TYPE_SET
    global TYPE_SINGLE
    global TYPE_REFERRED
    
    #this counts the number of matches in the true result set (ground truth)
    matches = 0
    accuracy = 0.0
    
    # remove multiple result
    result_set = convert_multiple_set(result_set)
    
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
        elif true_result["check"] == CHECK_ASK:
            ask_element = true_result["values"][0]
            ask_answer = ask_element["ask"]
            # verifico se ho ask query con risultato true o false
            if ask is not None:
                if ask==ask_answer:
                    return 1.0,1.0
                return 0.0,0.0
            
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
                return len(find),1.0
        else :
            #I have to verify only one element, of type uri in the values
            #print(true_result["values"])
            true_uri = [x[true_result["check"]] for x in true_result["values"]]
            for res in result_set:
                for t_u in true_uri:
                    if t_u in [t[1] for t in res] and not t_u in element_found:
                        element_found.append(t_u)
                        matches += 1
        
    ## the results are referred
    if true_result["type"] == TYPE_REFERRED:
        ## given that the type is referred, even if there is the elements_per_tuple parameter
        # There can be different elements that refer to the same element
        # for this reason, I create a map to know how many different element refer to 
        # the same element. Otherwise the accuracy will not be precise
        map_referred_count={}
        mult_res = true_result["values"]
        for val in mult_res:
            if val["refers_to"] not in map_referred_count:
                map_referred_count[val["refers_to"]]=0
            map_referred_count[val["refers_to"]] += 1
        # for each element in the values array I have to check the presence of the element referred
        
        # dictionary to track the referred result already found. To avoid counting multiple time same referred result
        referred_found = {}
        # iterate over the student's result set
        for res in result_set:
            #iterate over the multiple true result set
            elements_in_tuple = [t[1] for t in res]
            for val in mult_res:
                # check the presence of the referred element
                ref_uri = val["refers_to"]
                ref_name = val["refers_to_name"]
                # skip if it is not in the result
                if not (ref_uri in elements_in_tuple or ref_name in elements_in_tuple):
                    continue
                else:
                    if ref_uri not in element_found:
                        matches+=1
                        element_found.append(ref_uri)
                # values check 
                if type(val["check"]) == list:
                    # manage list check
                    t_u = [val[j] for j in val["check"]]
                    # manage type of values
                    # if the check type is a list, then it will always be a URI-name
                    if any([x==y for x in t_u for y in elements_in_tuple]):
                        # first check if I already found this referred result
                        if not (ref_uri in referred_found and t_u in referred_found[ref_uri]):
                            # there is a correct result, so I count it
                            accuracy+=1.0/float(true_result["elements_per_tuple"])
                            # add the found result to referred_found 
                            if ref_uri not in referred_found:
                                referred_found[ref_uri] = []
                            referred_found[ref_uri].append(t_u)
                elif val[val["check"]] in elements_in_tuple:
                    if not (ref_uri in referred_found and val[val["check"]] in referred_found[ref_uri]):
                        # there is a correct result, so I count it
                        accuracy+=1.0/float(true_result["elements_per_tuple"])
                        # add the found result to referred_found 
                        if ref_uri not in referred_found:
                            referred_found[ref_uri] = []
                        referred_found[ref_uri].append(val[val["check"]])
            
        
    if true_result["type"] == TYPE_SET:
        
        #I have to verify a set of elements
        for res in result_set:
            # the elements in this result tuple
            elements_in_tuple = [t[1] for t in res]
            # check the type
            for val in true_result["values"]:
                if type(true_result["check"]) == list:
                    # manage list check
                    t_u = [val[j] for j in true_result["check"]]
                    f_el = [y for x in t_u for y in elements_in_tuple if x==y]
                    if len(f_el)>0 and not any([j in element_found for j in t_u]):
                        matches+=1
                        for e in t_u:
                            element_found.append(e)
                else:
                    if val[true_result["check"]] in elements_in_tuple and val[true_result["check"]] not in element_found:
                        matches+=1
                        element_found.append(val[true_result["check"]])
    if len(element_found)==0:
        return matches,0.0
    tot_element = float(len(element_found))
    # normalize the accuracy according to the map_referred_count
    if true_result["type"] == TYPE_REFERRED:
        tot_element = float(sum([map_referred_count[obj] for obj in element_found]))
    return matches,accuracy/tot_element

## function to check if the string is a date 
def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False
    
## function to check if elements are all numbers
def are_numbers(array):
    if type(array) != list:
        array=[array]
    return (len(get_numbers(array)) == len(array))

## function to get numbers from an array
def get_numbers(array):
    if type(array) != list:
        array=[array]
    array=[str(a) for a in array]
    result = [float(val) for val in array if val.replace(".", "", 1).isdigit()]
    return result

def find_closest(arr, val):
    if arr is None or len(arr)==0:
        return 0
    if not (type(arr) is np.ndarray) and type(arr) is list:
        arr = np.array(arr)
    idx = np.abs(arr - val).argmin()
    return arr[idx]

def compute_accuracy(val, reference):
    if reference == 0:
        if val == 0:
            return 1.0
        else:
            return 0.0
    tmp = abs(float(val-reference)/float(reference))
    if tmp>1.0:
        return 0.0
    return 1.0-tmp

def convert_multiple_set(values):
    tmp = []
    for x in values:
        if x not in tmp:
            tmp.append(x)
    return tmp
        
def evaluate_notebook(nb,eval_dir,want_execution = False,verbose = False):
    global ground_truth
    global TYPE_SET
    global TYPE_SINGLE
    global TYPE_REFERRED
    # load the json workflow file
    file = json.load(open(nb))
    # ground truth
    
    # iterate trough the goals
    for goal in file['exploratory_workflow']:
        # first compute the keywords and the indexes
        for i_q in range(len(file['exploratory_workflow'][goal])):
            query = file['exploratory_workflow'][goal][i_q]
            file['exploratory_workflow'][goal][i_q]['keywords'] = keywords.convert_bitmap(keywords.analyze_query(query['query']))
            file['exploratory_workflow'][goal][i_q]['index'] = i_q
            
        # skip the evaluation if the goal is not in the ground truth
        if file['topic'] not in ground_truth or goal not in ground_truth[file['topic']]:
            continue
        # get the ground truth corresponding this goal
        true_result = ground_truth[file['topic']][goal]
        
        if verbose:
            print("Doing task",goal)
        # for each query evaluate the output
        for i_q in range(len(file['exploratory_workflow'][goal])):
            query = file['exploratory_workflow'][goal][i_q]
            file['exploratory_workflow'][goal][i_q]['keywords'] = keywords.convert_bitmap(keywords.analyze_query(query['query']))
            file['exploratory_workflow'][goal][i_q]['index'] = i_q
            
            if verbose:
                print("Running query #"+str(i_q))
            #print(q)
            # manage ask query
            ask = None
            if want_execution:
                res = run_query(query['query'])
                if res == None:
                    continue
                if analyze_query(query['query'])[1] == 1:
                    ## it means that this is an ask query
                    ask = res['boolean']
            else:
                res = query['output']
            
            recall = 0.0
            precision = 0.0
            if query['output'] is None:
                verification=0
                accuracy=0
            else:
                verification,accuracy = verify_result(query['output'],true_result,ask)
            #print(verification,accuracy)
            if true_result["type"] == TYPE_SET and verification > 0:
                stud_find_something = True
                #compute the recall
                recall = float(verification)/float(len(true_result["values"]))
                #compute the precision
                precision = float(verification)/float(len(res))

                if verbose:
                    print("Student find a set of",verification,"elements over a ground truth set of",len(true_result["values"]),"elements after",i_q,"queries in a set of",len(res),"elements")
            elif true_result["type"] == TYPE_REFERRED and verification > 0:
                stud_find_something = True
                #compute the recall
                recall = float(verification)/float(len(true_result["values"]))
                #compute the precision
                precision = float(verification)/float(len(res))/float(true_result["elements_per_tuple"])
                if verification > len(res):
                    # there is the possibility to find more result in a single record
                    precision = 1.0/float(true_result["elements_per_tuple"])
                

                if verbose:
                    print("Student find a set of",verification,"elements over a ground truth set of",len(true_result["values"]),"elements after",i_q,"queries in a set of",len(res),"elements")
            elif verification > 0 and true_result["type"] == TYPE_SINGLE :
                stud_find_something = True

                # I have to distinguish between result in an ask query and the others.
                # the result in the ask query is inside
                recall = float(verification)/float(len(true_result["values"]))
                if "any_all" in true_result and true_result["any_all"] == "any":
                    recall = 1.0
                elif true_result["check"] == "ask" and ask is None:
                    # the true result set is inside the ask element inside values
                    recall = float(verification)/float(len(true_result["values"][0]["elements"]))
                if ask is not None:
                    precision = float(verification)
                else:
                    #res cannot be empty since verification is greater than 0
                    precision = float(verification)/float(len(res))

                if verbose:
                    print("Student find the result after",i_q,"queries in a set of",len(res),"elements")
                    
            ## append the value of recall/precision/accuracy for the query
            file['exploratory_workflow'][goal][i_q]['recall'] = recall
            file['exploratory_workflow'][goal][i_q]['precision'] = precision
            file['exploratory_workflow'][goal][i_q]['accuracy'] = accuracy
            f_score = 0.0
            if recall+precision>0.0:
                f_score = 2*(recall*precision)/(recall+precision)
            file['exploratory_workflow'][goal][i_q]['fscore'] = f_score
            
    ## store the new file with the information about the evaluation of each query
    
    # create the main directory if it no exists
    if not os.path.exists(eval_dir):
        os.mkdir(eval_dir)
    # create the directory for this student
    eval_dir = eval_dir+os.sep+file['worker']
    if not os.path.exists(eval_dir):
        os.mkdir(eval_dir)
    eval_filepath = eval_dir+os.sep+nb.split("/")[-1]
    fd = open(eval_filepath,"w")
    json.dump(file, fd)
    fd.close()
    if verbose:
        print("-> Complete evaluation computation of",nb)
    
def run_evaluation(verbose):
    global people_dir
    global eval_dir
    for x in people_dir:
        for nb in people_dir[x]:
            evaluate_notebook(nb,eval_dir,False,False)
    
