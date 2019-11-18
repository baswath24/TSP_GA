import numpy as np
import random
import operator
import pandas as pd
import time
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from geneticAlgo import *
def gaMain(cities, popSize, eliteSize, mutationRate, generations,coMatrix):
	cityList = []
	cities=int(cities)
	for i in range(0,cities):
		cityList.append(i)
	distMat = []
	inm = coMatrix
	for i in range(cities):
		a=[]
		for j in range(cities):
			xDis = abs(inm[i][0] - inm[j][0])
			yDis = abs(inm[i][1] - inm[j][1])
			distance = np.sqrt((xDis ** 2) + (yDis ** 2))
			a.append(float(distance))
		distMat.append(a)    	
	print(distMat)	
	fdist=geneticAlgorithm(population=cityList, popSize=int(popSize), eliteSize=int(eliteSize), mutationRate=float(mutationRate), generations=int(generations),distMatrix=distMat)
	fdist="Final Distance :"+fdist

	
root=Tk()
root.geometry("1000x500")
root.title('GA for TSP')
w = Label(root, text='Genetic Algo for TSP').grid(row=0) 

Label(root, text='City Count :').grid(row=1)
Label(root, text='City Co-Ordinates :').grid(row=2) 
e1 = Entry(root) 
e1.grid(row=1, column=1) 
TextArea = Text(root, height=10, width=10)
ScrollBar = Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.grid(row=2,column=2)
TextArea.grid(row=2,column=1)
Label(root, text='Population Size :').grid(row=3) 
Label(root, text='Elite Size :').grid(row=4) 
Label(root, text='Mutation Rate :').grid(row=5) 
Label(root, text='Generations :').grid(row=6) 
e3 = Entry(root) 
e4 = Entry(root) 
e5 = Entry(root) 
e6 = Entry(root) 
e3.grid(row=3, column=1) 
e4.grid(row=4, column=1) 
e5.grid(row=5, column=1) 
e6.grid(row=6, column=1)
def inp():
	cities=int(e1.get())
	popSize=(e3.get())
	eliteSize=(e4.get())
	mutationRate=(e5.get())
	generations=(e6.get())
	coMat=TextArea.get("1.0",'end-1c')
	coMat=coMat.strip().split("\n")
	coMatrix = [[0]*2 for _ in range(cities)]
	for i in range(cities):
		coMatrix[i] = [float(j) for j in coMat[i].strip().split(" ")]
	#print(coMat[0])		
	gaMain(cities=cities, popSize=popSize, eliteSize=eliteSize, mutationRate=mutationRate, generations=generations,coMatrix=coMatrix)
b = Button(root,activebackground='pink',text='Calculate',command=inp)
b.grid(row=7, column=1)
root.mainloop()
