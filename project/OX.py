import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


def orderbreed(parent1, parent2):
    child = [],
    childP1 = [int(-1) for i in parent1]
    childP2 = [int(-1) for i in parent1]
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene,endGene+1):
        childP1[i]=parent1[i]
    j=endGene+1
    for i in range(endGene+1,len(parent1)):
        if(parent2[i] in childP1):
            continue
        else:
            childP1[j]=parent2[i]
            j=j+1
    if(j==len(parent1)):
        j=0
        for i in range(0,endGene):
            if(parent2[i] in childP1):
                continue
            else:
                childP1[j]=parent2[i]
                j=j+1
    else:
        for i in range(0,endGene):
            if(parent2[i] in childP1):
                continue
            else:
                j=j+1
                if(j<=len(parent1)):
                    childP1[j-1]=parent2[i]
                else:
                    childP1[j-len(parent1)-1]=parent2[i]

    
    for i in range(startGene,endGene+1):
        childP2[i]=parent2[i]
    j=endGene+1
    for i in range(endGene+1,len(parent2)):
        if(parent1[i] in childP2):
            continue
        else:
            childP2[j]=parent1[i]
            j=j+1
    if(j==len(parent2)):
        j=0
        for i in range(0,endGene):
            if(parent1[i] in childP2):
                continue
            else:
                childP2[j]=parent1[i]
                j=j+1
    else:
        for i in range(0,endGene):
            if(parent1[i] in childP2):
                continue
            else:
                j=j+1
                if(j<=len(parent1)):
                    childP2[j-1]=parent1[i]
                else:
                    childP2[j-len(parent1)-1]=parent1[i]                




    child.append(childP1)
    child.append(childP2)
    return child



def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children
