from random import random, sample, choice
from math import floor
from tqdm import tqdm
from numpy import array, dot, mean
from numpy.linalg import pinv
from sys import exit

def check_termination_condition():
    if ((best_individual['COD'] >= 98.0)
            or (generation_count == max_generations)):
        return True
    else:
        return False