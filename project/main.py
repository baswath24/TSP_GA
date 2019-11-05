import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt
from geneticAlgo import *


cityList = []
cities=int(input("No of Cities:"))
for i in range(0,cities):
	cityList.append(i)
distMat = []
print("distance array: ")
# distMat = [[0]*cities for _ in range(cities)]
# for i in range(cities):
#     distMat[i] = [int(j) for j in input().strip().split(" ")]	
inm = [[0]*2 for _ in range(cities)]
for i in range(cities):
	inm[i] = [float(j) for j in input().strip().split(" ")]
for i in range(cities):
	a=[]
	for j in range(cities):
		xDis = abs(inm[i][0] - inm[j][0])
		yDis = abs(inm[i][1] - inm[j][1])
		distance = np.sqrt((xDis ** 2) + (yDis ** 2))
		a.append(float(distance))
	distMat.append(a)    	
print(distMat)
geneticAlgorithm(population=cityList, popSize=200, eliteSize=10, mutationRate=0.045, generations=2000,distMatrix=distMat)
