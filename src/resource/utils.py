### File that contains a lot of utility functions

## divide the name of the workflow to get the MACRO - TOPIC
def getMacroTopic(name):
    return name.split(" ")[0].strip()


#return the student ID from the filepath of the notebook
def get_student_id(file):
    return file.split("/")[-2].replace("M","")

#return the name of the notebook file from the filepath
def get_notebook_name(file):
    return file.split("/")[-1]

def format_string(text):
    return text.strip().replace('\n','')


def format_perc(num):
    return (float(int(num*10000)))/100.0