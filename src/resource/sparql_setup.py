## SETUP used later

from SPARQLWrapper import SPARQLWrapper, JSON



prefixString = """
##-statistics-##
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
PREFIX sc: <http://schema.org/>
"""

# select and construct queries
def run_query(queryString, verbose = False):
    if(nbks.analyze_query(queryString)[1] == 1):
        return run_ask_query(queryString)
        
    to_run = prefixString + "\n" + queryString
    
    sparql = SPARQLWrapper("https://grace.dei.unipd.it/sparql")
    sparql.setTimeout(300)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(to_run)

    try :
        results = sparql.query()
        json_results = results.convert()
        if len(json_results['results']['bindings'])==0:
            if verbose:
                print("Empty")
            return []
        array = []
        for bindings in json_results['results']['bindings']:
            app = [ (var, value['value'])  for var, value in bindings.items() ]
            array.append(app)
            if verbose:
                print( app )
        return array

    except Exception as e :
        print("The operation failed", e)
    
# ASk queries
def run_ask_query(queryString):
    #query execution
    to_run = prefixString + "\n" + queryString

    sparql = SPARQLWrapper("http://a256-gc1-02.srv.aau.dk:5820/sparql")
    sparql.setTimeout(300)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(to_run)

    try :
        return sparql.query().convert()

    except Exception as e :
        print("The operation failed", e)