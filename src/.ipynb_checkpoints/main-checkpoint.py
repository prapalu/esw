
import resource.notebooks as nbks
import resource.logs as logs
import resource.statistics as stats
import resource.evaluation as evaluation
from jproperties import Properties

def setup(configs, verbose = False):
    nbks.setup_keywords(configs.get("keywords").data,verbose )
    logs.setup_logs_dir(configs.get("logs").data,verbose )
    nbks.setup_notebooks(configs.get("notebook").data,verbose )
    nbks.setup_workflows(verbose)
    evaluation.setup_evaluation_folder(configs.get("evaluations").data, verbose)
    evaluation.setup_results_folder(configs.get("results").data, verbose)

def main():
    #load properties
    configs = Properties()
    with open('config.properties', 'rb') as config_file:
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
    
    # print informations
    nbks.print_workflows_informations()
    
    # solid creation
    nbks.create_solid(verbose)
    print(nbks.solid.shape)
    
    # popolation
    nbks.popolate_solid(verbose)
    
    # student's notebook analysis
    evaluation.compute_analysis()
    
    

if __name__ == "__main__":
    main()