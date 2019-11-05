import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt

def createRoute(cityList):
	route = random.sample(cityList, len(cityList))
	return route

def initialPopulation(popSize, cityList):
	population = []

	for i in range(0, popSize):
		population.append(createRoute(cityList))
	return population