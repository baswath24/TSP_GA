import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt
from create_pop import *
from fitness import *
from generation import *

def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations,distMatrix):
	pop = initialPopulation(popSize, population)
	print("Initial distance: " + str(1 / rankRoutes(pop,distMatrix)[0][1]))
	progress = []
	progress.append(1 / rankRoutes(pop,distMatrix)[0][1])


	for i in range(0, generations):
		pop = nextGeneration(pop, eliteSize, mutationRate,distMatrix)
		print(i)
		progress.append(1 / rankRoutes(pop,distMatrix)[0][1])
	print("Final distance: " + str(1 / rankRoutes(pop,distMatrix)[0][1]))
	bestRouteIndex = rankRoutes(pop,distMatrix)[0][0]
	bestRoute = pop[bestRouteIndex]
	bestRoute
	plt.plot(progress)
	plt.ylabel('Distance')
	plt.xlabel('Generation')
	plt.show()
	return bestRoute