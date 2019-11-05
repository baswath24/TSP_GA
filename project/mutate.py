import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutatePopulation(population, mutationRate, eliteSize):
    mutatedPop = []
    for ind in range(0,eliteSize):
    	mutatedPop.append(population[ind])
    
    for ind in range(eliteSize, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop