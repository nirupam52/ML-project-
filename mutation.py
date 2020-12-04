from random import choice,random, sample


def mutate(specimen, probability):
    
    specimen_length = len(specimen.value)
    indexes = [i for i in range(specimen_length)]
    number = int(probability*specimen_length)
    to_be_mutated = sample(indexes,number)

    for x in to_be_mutated:
        specimen.value[x] = specimen.value[x]*random()

    return specimen 



#custom mutation can be attempted 