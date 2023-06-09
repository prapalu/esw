import resource.conversion as conv
import resource.gt_conversion as gt_conv
import resource.logs as logs
from jproperties import Properties
import datetime
import sys

def setup(configs, verbose = False):
    conv.setup_nb_folder(configs.get("notebook").data,verbose )
    conv.setup_json_folder(configs.get("json_notebook_dir").data,verbose )
    logs.setup_logs_folder(configs.get("logs").data,verbose )
    gt_conv.setup_nb_folder(configs.get("gt_nbks_dir").data,verbose )
    gt_conv.setup_json_folder(configs.get("gt_converted").data,verbose )
    gt_conv.setup_indexes(configs.get("topic_index").data,verbose )

def main(config_file):
    #load properties
    configs = Properties()
    with open(config_file, 'rb') as config_file:
        configs.load(config_file)
    verbose = configs.get("verbose").data
    start_date = configs.get("start_date").data
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = configs.get("end_date").data
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
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
    conv.load_notebooks(verbose)
    # load the logs, between start and end (dates)
    logs.load_logs(start_date,end_date,verbose)
    # convert the notebooks in json files, and store them in the folder specified in the properties
    conv.convert_nb(verbose)
    # load the json notebooks filepaths from the folder just created
    conv.load_json_notebooks(verbose)
    # associate the logs to the json files
    conv.associate_logs(conv.people_dir,logs.code_list,verbose)
    # associate the execution to the json files
    conv.associate_execution(configs.get("json_executed_dir").data,verbose)

    ### convert ground truths
    # load the python notebook's filepaths
    gt_conv.load_gt_notebooks(verbose)
    # convert the notebooks in json files, and store them in the folder specified in the properties
    gt_conv.convert_gt_nb(verbose)
    

if __name__ == "__main__":
    if len(sys.argv)!=2 or not sys.argv[1].endswith(".properties"):
        print("-- ERROR --")
        print("You must specify a .properties file in the command line. A suitable example is of execution is:\n")
        print("python converter.py config2022.properties\n")
        exit()
    main(sys.argv[1])