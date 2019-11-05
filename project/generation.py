import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt
from fitness import *
from selection import *
from mutate import *
from breed import *

def nextGeneration(currentGen, eliteSize, mutationRate, distMatrix):
	popRanked = rankRoutes(currentGen,distMatrix)
	selectionResults = selection(popRanked, eliteSize)
	matingpool = matingPool(currentGen, selectionResults)
	children = breedPopulation(matingpool, eliteSize)
	nextGeneration = mutatePopulation(children, mutationRate, eliteSize)
	return nextGeneration