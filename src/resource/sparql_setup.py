import resource.keywords as keywords
from SPARQLWrapper import SPARQLWrapper, JSON
import time
import datetime

global prefixString
prefixString = """
##-statistics-##
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
PREFIX sc: <http://schema.org/>
"""
def setup_nb_code(code):
    global prefixString
    prefixString = """
    ##-"""+code+"""-##
    PREFIX wd: <http://www.wikidata.org/entity/> 
    PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
    PREFIX sc: <http://schema.org/>
    """


# select and construct queries
def run_query(queryString, verbose = False):
    if(keywords.analyze_query(queryString)[1] == 1):
        return run_ask_query(queryString)
        
    global prefixString
    to_run = prefixString + "\n" + queryString
    
    sparql = SPARQLWrapper("http://grace.dei.unipd.it/sparql/")
    sparql.setTimeout(300)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(to_run)
    # example of format 13/Dec/2022:10:26:16
    timestamp = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S")
    try :
        start = time.time()
        results = sparql.query()
        end = time.time()-start
        json_results = results.convert()
        if len(json_results['results']['bindings'])==0:
            if verbose:
                print("Empty")
            return {"time":end,"output":[],"error":None,"timestamp":timestamp}
        array = []
        for bindings in json_results['results']['bindings']:
            app = [ (var, value['value'])  for var, value in bindings.items() ]
            array.append(app)
            if verbose:
                print( app )
        return {"time":end,"output":array,"error":None,"timestamp":timestamp}

    except Exception as e :
        print("The operation failed", e)
        return {"time":0,"output":None,"error":str(e),"timestamp":timestamp}
    
# ASk queries
def run_ask_query(queryString):
    global prefixString
    #query execution
    to_run = prefixString + "\n" + queryString
    
    sparql = SPARQLWrapper("http://grace.dei.unipd.it/sparql/")
    sparql.setTimeout(300)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(to_run)
    # example of format 13/Dec/2022:10:26:16
    timestamp = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S")
    try :
        start = time.time()
        res = sparql.query().convert()
        end = time.time()-start
        return {"time":end,"output":sparql.query().convert(),"error":None,"timestamp":timestamp}
        #return sparql.query().convert()
    except Exception as e :
        print("The operation failed", e)
        return {"time":0,"output":None,"error":str(e),"timestamp":timestamp}