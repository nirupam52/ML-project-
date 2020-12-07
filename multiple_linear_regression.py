from random import random, sample, choice
from math import floor
# from tqdm import tqdm
from numpy import array, dot, mean
from numpy.linalg import pinv
from sys import exit

#SST: the total error in a model, it is the sum of all deviations squared.
#SSR: a measure of the explained variation in SST
#COD: stands for ‘coefficient of determination’ which is basically a measure of how good a model is
#error: the average error, is an average of all deviations from expected values. 


def multiple_linear_regression(inputs, outputs,coeffs):
    X, Y =  inputs, outputs #array(inputs), array(outputs)
    X_t, Y_t = X.transpose(), Y.transpose()
    #coeff = dot((pinv((dot(X_t, X)))), (dot(X_t, Y)))
    Y_p = dot(X, coeffs)
    Y_mean = mean(Y)
    SST = array([(i - Y_mean) ** 2 for i in Y]).sum()
    SSR = array([(i - j) ** 2 for i, j in zip(Y, Y_p)]).sum()
    COD = (1 - (SSR / SST)) * 100.0
    av_error = (SSR / len(Y))
    #return {'COD': COD, 'coeff': coeff, 'error': av_error}
    return COD