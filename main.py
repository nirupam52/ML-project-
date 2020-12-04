import numpy as np
import pandas as pd 
from random import random
import crossover, fitness, mutation, pre_model

input_dat = pre_model.pre_coeffs() #placeholder; need to get from a pretrained model 
pop_size = 50
generations = 1000

input_fitness = None #placeholder

class Agent:

    def __init__(self,input_size) :
        
        self.value = [random() for i in range(len(input_size))]
        self.fitness = -1


def agent_init(pop_size,input_size):
    return [Agent(input_size) for _ in range(pop_size)]

if __name__ == "__main__":
    
    initial_pop = agent_init(pop_size,len(input_dat))
    
    for x in range(generations):
        print("Gen :",x)
        # do stuff  

        if ( ): # agent_fitness > input fitness 
            break
        
