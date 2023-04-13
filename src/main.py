import converter as conv
import evaluator as ev
import export_ttl as exp
import clean as cl

def main():
    for configs in ['config2021.properties','config2022.properties']:
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
    main()