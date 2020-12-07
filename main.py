import numpy as np
import pandas as pd 
from random import random, sample
import  fitness, mutation
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.30, random_state=69)

input_dat = pre_coeffs(X_train,y_train) #placeholder; need to get from a pretrained model 
pop_size = 50
generations = 1000
mutation_probablity = 0.3
input_fitness = None #placeholder

class Agent:

    def __init__(self,input_size) :
        
        self.value = [random() for i in range(len(input_size))]
        self.fitness = -1


def pop_init(pop_size,input_size):
    return [Agent(input_size) for _ in range(pop_size)]

if __name__ == "__main__":
    
    
    agents = pop_init(pop_size,len(input_dat))

    for x in range(generations):
        print("Gen :",x)
         

        #fitness
        fitness.agent_fitness(agents,X_train,y_train) 

        #select
        picked_agents = selection(agents) 

        #crossover
        new_agents = crossover(picked_agents,)

        #mutation
        agents = mutation.mutate(new_agents,mutation_probablity)
        fitness.agent_fitness(agents,X_train,y_train) 

        if any(agent.fitness > fitness.fitness(input_dat,X_train,y_train) for agent in agents): # agent_fitness > input fitness 
            # print(agent.values)
            # print(agent.fitness)
            break
    
    final = selection(agents)
    print(final[0])
        

def pre_coeffs(X,y):
    
    reg_model = linear_model.LinearRegression()
    reg_model.fit(X, y)

    return reg_model.coef_

def selection(agents):
    selected_agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True) 

    return selected_agents[:int(0.2 * len(agents))]

def crossover(agents, input_size):

    children = []
    for _ in range(int(0.6*len(agents))):
        

        p1,p2 = sample(agents,2)
        index = int(0.5*input_size)
        child1 = Agent(len(input_dat))
        child2 = Agent(len(input_dat))
        child1.value = p1.value[:index] + p2.value[index:]
        child2.value = p2.value[:index] + p1.value[index:]

        children.append(child1,child2)
    
    return agents.extend(children)
