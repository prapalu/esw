from urllib.parse import unquote
import resource.utils as utils
import os
import datetime

global logs_file_dir
global code_list

# setup the logs dir
def setup_logs_folder(filepath, verbose = False):
    global logs_file_dir
    logs_file_dir = filepath
    if verbose:
        print("Set up logs directory at ",filepath)

# function for parsing a line of log file
def parse_log_line(line,verbose = False):
    line = unquote(line)
    ret = {}
    try:
        ip = line.split("-")[0].strip()
        ret["ip"] = ip
        date = line.split("+")[0].split("[")[1].strip()
        ret["date"] = date
        query = line.split("HTTP/1.1")[0].split("GET")[1].strip().split("&format=json&output=json&results=json")[0].strip()
        query = query.split("/sparql?query=")[1]
        ret["query"] = clean_query(query)
        code = query.split("##-")[1].split("-##")[0].strip()
        ret["code"] = code
        if verbose:
            print(ip,date)
            print(query)
            print(code)
        ret["error"] = 0
        return ret
    except:
        ret["error"] = 1
        return ret

# function to clean the query in the log
def clean_query(query):
    query = query.replace("+"," ")
    new = ""
    for line in query.split("\n"):
        if (line.startswith("##-") and line.endswith("-##")) or line.startswith("PREFIX") or line.strip()=="":
            continue
        if line.find("#") == -1:
            new+=" "+line.strip()
        else:
            ## need to check if it is a PREFIX line
            split_sharp = line.split("#")
            # PREFIX condition
            if line.strip().upper().startswith("PREFIX") and (split_sharp[1].strip())[0] == ">":
                # it is a prefix, so keep the entire line
                ret+=" "+line.strip()
            else:
                remain = line[:line.find("#")].strip()
                if remain != "":
                    ret+=" "+remain
    return new.strip()

# function to get the total number of query executed given the notebook's code
def get_num_query_log(nb,start,end):
    global logs_file_dir
    refer_code = nb.split("/")[-1].split(".")[0]
    tot_lines = 0
    for file in os.listdir(logs_file_dir):
        if not file.endswith("log"):
            continue
        file_t = file.replace(".log","").replace("http","")
        year = file_t[4:]
        month = file_t[2:4]
        day = file_t[:2]
        # convert from string format to datetime format
        date = datetime.datetime.strptime(year+"-"+month+"-"+day, '%Y-%m-%d').date()
        #file to be skipped because are not part of the project (my runs when I started to work on thesis)
        if not (date>start and date<end):
            continue
        #define bitmap
        f = open(logs_file_dir+os.sep+file, "r")
        lines = f.read().split("\n")
        f.close()
        for l in lines:
            if l.strip() != "":
                ret = parse_log_line(l)
                if ret["code"] is not None and ret["code"] == refer_code:
                    tot_lines+=1
    return tot_lines


def load_logs(start,end,verbose = False):
    global logs_file_dir
    global code_list
    if verbose:
        print("Start to read the logs from",logs_file_dir,":",len(os.listdir(logs_file_dir)),"files")
    errors = 0
    code_list={}
    tot_lines = 0
    for file in os.listdir(logs_file_dir):
        if not file.endswith("log"):
            continue
        file_t = file.replace(".log","").replace("http","")
        year = file_t[4:]
        month = file_t[2:4]
        day = file_t[:2]
        #file to be skipped because are not part of the project (my runs when I started to work on thesis)
        if year != "2022" or (year == "2022" and month == "12" and int(day)>26):
            continue
        #define bitmap
        f = open(logs_file_dir+os.sep+file, "r")
        lines = f.read().split("\n")
        f.close()
        for l in lines:
            if l.strip() != "":
                ret = parse_log_line(l)
                errors+=ret["error"]
                if "code" not in ret:
                    continue
                code = ret["code"]
                if code not in code_list:
                    code_list[code]=[ret]
                else:
                    code_list[code].append(ret)
        tot_lines+=len(lines)
    if verbose:
        print("Finished to read the logs from",logs_file_dir)
        print("Total errors",errors)
        print("Total line analyzed",tot_lines)
        
# function to map the queries into a dictionary with keys the text ok the queries and values an array with their executions
def map_query_into_dict(queries):
    ret = {}
    for q in queries:
        if q["query"] not in ret:
            ret[q["query"]] = [q['date']]
        else:
            ret[q["query"]].append(q['date'])
    return ret