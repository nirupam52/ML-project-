from random import random


def crossover(p1,p2, input_size):


    index = int(0.5*input_size)
    child1 = p1.value[:index] + p2.value[index:]
    child2 = p2.value[:index] + p1.value[index:]

    return child1,child2






#custom crossover 
