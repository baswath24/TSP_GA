import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child1 = childP2[:startGene]+childP1+childP2[startGene:]
    child.append(child1)

    childP11 = []
    childP22 = []

    for i in range(startGene, endGene):
        childP22.append(parent2[i])
        
    childP11 = [item for item in parent1 if item not in childP22]

    child2 = childP11[:startGene]+childP22+childP11[startGene:]
    child.append(child2)

    return child

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child[0])
        children.append(child[1])
    return children