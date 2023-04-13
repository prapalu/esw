import os
from jproperties import Properties

def main(config_file):
    configs = Properties()
    with open(config_file, 'rb') as config_file:
        configs.load(config_file)
    if os.path.exists(configs.get('json_notebook_dir').data):
        print("--> Clean workflows_json folder for",config_file)
        os.system('rm -r '+configs.get('json_notebook_dir').data)
    if os.path.exists(configs.get('evaluations').data):
        print("--> Clean workflows_evaluated folder for",config_file)
        os.system('rm -r '+configs.get('evaluations').data)
    if os.path.exists(configs.get('rdf').data):
        print("--> Clean rdf folder for",config_file)
        os.system('rm -r '+configs.get('rdf').data)
    
    
# execute everything
if __name__ == "__main__":
    main('config.properties')