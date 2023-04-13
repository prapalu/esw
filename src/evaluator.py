import resource.evaluation as evaluation
import resource.keywords as keywords
from jproperties import Properties
import datetime

def setup(configs, verbose = False):
    evaluation.setup_evaluation_folder(configs.get("evaluations").data,verbose )
    evaluation.load_json_notebooks(configs.get("json_notebook_dir").data,verbose )
    evaluation.load_ground_truths(configs.get("results").data,verbose )
    keywords.setup_keywords(configs.get("keywords").data,verbose )

def main(config_file):
    #load properties
    configs = Properties()
    with open(config_file, 'rb') as config_file:
        configs.load(config_file)
    verbose = configs.get("verbose").data
    if verbose == None:
        verbose = False
    elif verbose.lower() == 'true':
        verbose = True
    elif verbose.lower() == 'false':
        verbose = False
    print(verbose)
    # setup configs
    setup(configs,verbose)
    # load the python notebook's filepaths
    evaluation.run_evaluation(verbose)
    

if __name__ == "__main__":
    main('config.properties')