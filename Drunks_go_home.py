# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:19:53 2019

@author: msra2nk3
"""

#Importing packages
import matplotlib.pyplot as plt
import pandas


#creates the environment from the raster file

environment = []



with open('drunk.plan.txt') as f:
    for row in f:
        rowlist = row.split(',')
        rowlist_of_lists = [int(x) for x in rowlist]
        environment.append(rowlist_of_lists)
        
env_limits = len(environment)  
#Plots the bare environment to tests whether the environment is read correctly
        

"""
plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment)

"""
#Creates the pubs 

#reads in the raster file a dataframe
pubfinder = pandas.read_csv('drunk.plan.txt')

#creates lists for the vertical and horizontal dimesnions of the pub
pubx = []
puby = []

#checks the all x, y coordinates for value of 1, if found appends the
#coordinates to pubx and puby lists
for row in range(len(pubfinder)): 
         for col in range(len(pubfinder)):
             if pubfinder.iat[row,col] == 1:
                 pubx.append(row)
                 puby.append(col)


plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment)
plt.scatter(pubx, puby)       
plt.show()       

#finds the houses 

houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,\\
          120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

