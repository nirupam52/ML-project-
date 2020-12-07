from random import choice,random, sample, uniform


def mutate(agents, probability):
    
    
    for agent in agents:

        specimen_length = len(agent.value)
        indexes = [i for i in range(specimen_length)]
        number = int(probability*specimen_length)
        to_be_mutated = sample(indexes,number)

        for x in to_be_mutated:
            agent.value[x] = agent.value[x]*random()

    return agents 



#custom mutation can be attempted 