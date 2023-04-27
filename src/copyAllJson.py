import os
import json
import csv

## Copy all JSON files both noteboks and gts in a single directory
main='../'
savePath = main+'json_resources'
if not os.path.exists(savePath):
    os.makedirs(savePath)
    
def copy_files(source, destination):
    for folder in os.listdir(source):
        subdir = source + os.sep + folder
        for file in os.listdir(subdir):
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                command = 'cp '+filepath+' '+destination
                os.system(command)
                
def copy_gt(source, destination):
    for file in os.listdir(source):
        filepath = source + os.sep + file
        if filepath.endswith(".json"):
            command = 'cp '+filepath+' '+destination
            os.system(command)
                

if __name__ == "__main__":
    copy_files(main+'tracks/2022/workflows_evaluated',savePath)
    copy_files(main+'tracks/2021/workflows_evaluated',savePath)
    copy_gt(main+'tracks/2021/ground_truths/gt_json',savePath)
    copy_gt(main+'tracks/2022/ground_truths/gt_json',savePath)