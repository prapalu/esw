import numpy as np


#define global variables
global keywords

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

def convert_bitmap(bitmap):
    global keywords
    d = {}
    for index in range(len(keywords)):
        d[keywords[index]] = int(bitmap[index])
    return d

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