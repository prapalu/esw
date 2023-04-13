import resource.conversion as conv
from jproperties import Properties

def setup(configs, verbose = False):
    conv.setup_nb_folder(configs.get("notebook").data,verbose )
    conv.setup_json_folder(configs.get("json_notebook_dir").data,verbose )

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
    conv.load_notebooks(verbose)
    conv.convert_nb(verbose)
    

if __name__ == "__main__":
    main()