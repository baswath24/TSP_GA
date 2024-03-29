import numpy as np
import random
import operator
import pandas as pd
import time
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
inm = [[0]*3 for _ in range(cities)]
for i in range(cities):
	inm[i] = [float(j) for j in input().strip().split(" ")]
for i in range(cities):
	a=[]
	for j in range(cities):
		xDis = abs(inm[i][1] - inm[j][1])
		yDis = abs(inm[i][2] - inm[j][2])
		distance = np.sqrt((xDis ** 2) + (yDis ** 2))
		a.append(float(distance))
	distMat.append(a)    	
print(distMat)
print("population size: ")
popSize=int(input())
print("elite size: ")
eliteSize=int(input())
print("mutation Rate: ")
mutationRate=float(input())
print("generations: ")
generations=int(input())
start_time=time.time()
geneticAlgorithm(population=cityList, popSize=popSize, eliteSize=eliteSize, mutationRate=mutationRate, generations=generations,distMatrix=distMat)
elapsed_time=time.time()-start_time
print("elapsed_time: ",elapsed_time)