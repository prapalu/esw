import numpy as np
import resource.utils as utils
import resource.notebooks as nbks
import resource.query as qu

#function to sum everything that the return the bitmaps' sum
def sum_bitmaps(matrix):
    while matrix.ndim > 1:
        matrix = np.sum(matrix,axis = 0)
    return matrix

#return the number of queries done in the solid provided in input
def sum_query(sub):
    if sub.ndim > 2:
        return sum(sum_query(sub[i]) for i in range(sub.shape[0]))
    else:
        return sum([1 if (np.sum(sub[x],axis = 0))>0 else 0 for x in range(sub.shape[0])])

#this function return the type of the elements in the list 
def check_list_elements(_list):
    l = [type(x) for x in _list] 
    l = list(set(l))
    if len(l) == 1:
        return l[0]
    return None

#run the statistics on the parameters provided in input
def do_statistics( macro = None, topic = None, student = None, goal = None , verbose = False):
    if macro == None and topic == None and student == None and goal == None:
        return sum_bitmaps(nbks.solid)
    index_topic = None
    index_macro = None
    if verbose:
        print(*[macro,topic,student,goal],sep = '\n')
    
    #setup macro index
    if macro != None:
        #there is a macro topic, check the type of the element
        if type(macro) == int:
            index_macro = macro
        elif type(macro) == str:
            index_macro = nbks.get_index_by_macro_topic(macro)
        elif verbose:
            print("Error with the macro-topic parameter")
        if verbose:
            print("INDEX MACRO TOPIC",index_macro)
        if index_macro == None:
            return None
        elif index_macro<0:
            if verbose:
                print("Macro Topic does not exists")
            return None
    if topic != None:
        #there is a topic, check the type of the element
        if type(topic) == int:
            index_topic = topic
        elif type(topic) == str:
            index_topic = nbks.get_index_by_sub_topic(topic)
        elif verbose:
            print("Error with the sub-topic parameter")
        if verbose:
            print("INDEX SUB TOPIC",index_topic)
        if index_topic == None:
            return None
        elif index_topic<0:
            if verbose:
                print("Topic does not exists")
            return None
        index_macro = nbks.get_index_by_macro_topic(nbks.get_macro_from_sub_topic(topic))
    #student part
    index_student = None
    if student != None:
        #there is a student, check the type of the element
        if type(student) == int:
            index_student = student
        elif type(student) == str:
            index_student = nbks.get_index_by_student(student)
        elif verbose:
            print("Error with the student parameter")
        if verbose:
            print("INDEX STUDENT",index_student)
        if index_student == None:
            return None
        elif index_student < 0:
            if verbose:
                print("Student does not exists")
            return None
    index_goal = None
    if goal != None:
        #there is a student, check the type of the element
        if type(goal) == int:
            index_goal = goal
        elif type(goal) == str:
            macro = nbks.get_macro_from_sub_topic(topic)
            index = nbks.get_sub_topic_by_index(topic) if type(topic)==int else topic
            goals_work = qu.find_workflow_goals(nbks.workflows[macro][index][0])
            index_goal = nbks.get_index_by_goal(goals_work,goal)
        elif verbose:
            print("Error with the student parameter")
        if verbose:
            print("INDEX GOAL",index_goal)
        if index_goal == None:
            return None
        elif index_goal < 0:
            if verbose:
                print("Goal does not exist")
            return None
        
    
    
    if index_macro == None and index_topic == None and index_student != None:
        return sum_bitmaps(nbks.solid[:, : , index_student,:])
    elif index_macro != None and index_topic == None and index_student != None:
        return sum_bitmaps(nbks.solid[index_macro, : , index_student,:])
    elif index_macro != None and index_topic == None and index_student == None:
        return sum_bitmaps(nbks.solid[index_macro, : , :,:])
    elif index_topic != None and index_student == None and index_goal == None:
        return sum_bitmaps(nbks.solid[index_macro, : , index_topic , :,:])
    elif index_topic != None and index_student == None and index_goal != None:
        return sum_bitmaps(nbks.solid[index_macro , index_topic , :,index_goal])
    elif index_topic != None and index_student != None and index_goal == None:
        return sum_bitmaps(nbks.solid[index_macro,index_topic , index_student,:])
    elif index_topic != None and index_student != None and index_goal != None:
        return sum_bitmaps(nbks.solid[index_macro,index_topic , index_student,index_goal])
    return None