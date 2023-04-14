import os
from jproperties import Properties
import sys

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
    if len(sys.argv)!=2 or not sys.argv[1].endswith(".properties"):
        print("-- ERROR --")
        print("You must specify a .properties file in the command line. A suitable example is of execution is:\n")
        print("python converter.py config2022.properties\n")
        exit()
    main(sys.argv[1])