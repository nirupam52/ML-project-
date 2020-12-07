from random import random, sample


def crossover(agents, input_size):

    children = []
    for _ in range(int(0.6*len(agents))):
        

        p1,p2 = sample(agents,2)
        index = int(0.5*input_size)
        child1 = p1.value[:index] + p2.value[index:]
        child2 = p2.value[:index] + p1.value[index:]

        children.append(child1,child2)
    
    return agents.extend(children)






#custom crossover 
