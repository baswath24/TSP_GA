from project import *
import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self,distMatrix):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += distMatrix[fromCity][toCity]
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self,distMatrix):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance(distMatrix))
        return self.fitness


def rankRoutes(population,distMatrix):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness(distMatrix)
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)