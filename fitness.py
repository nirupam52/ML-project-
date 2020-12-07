import multiple_linear_regression as mlr



def fitness(coeff,inputs,outputs):

    fitness = mlr.multiple_linear_regression(inputs,outputs,coeff)

    return fitness

def agent_fitness(agents, inputs, outputs):

    for agent in agents:

        agent.fitness = mlr.multiple_linear_regression(inputs,outputs,agent.values)