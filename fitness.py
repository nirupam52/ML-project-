# implement 



def fitness(agent):

    agent.fitness = solver(agent.values)

    return fitness


def solver(values):
    #implement regression using LSE 