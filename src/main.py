import converter as conv
import evaluator as ev
import export_ttl as exp
import clean as cl
import sys

def main(config_file = None):
    configurations = ['config2021.properties','config2022.properties']
    if config_file is not None:
        configurations = [config_file]
    for configs in configurations:
        print("--> Clean old folders for", configs)
        cl.main(configs)
        print("--> Start conversion for",configs)
        conv.main(configs)
        print("--> Start evaluation for",configs)
        ev.main(configs)
        print("--> Start export turtles for",configs)
        exp.main(configs)
    
    
# execute everything
if __name__ == "__main__":
    if len(sys.argv)==2 and sys.argv[1].endswith(".properties"):
        main(sys.argv[1])
    else:
        main()