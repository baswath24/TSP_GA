import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt
from project import *


cityList = []

for i in range(0,input()):
    cityList.append(i)
distMat = []
distMat.append(input())

geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500,distMatrix=distMat)
