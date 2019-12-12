# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:19:53 2019

@author: msra2nk3
"""

#Importing packages

import matplotlib.animation
import matplotlib.pyplot as plt
import pandas
import agentframework_drinkers
import csv
import sys


#takes the argument given when running the code
#if that argument is an integer it becomes the number of iterations
#otherwise it sets the number of iterations as a default value


while True:
    try:
       num_of_iterations = int(sys.argv[1])
       break
    except ValueError:
        print("Invalid entry, running model with default value of 1000") 
        num_of_iterations = 1000
        break


#Creates the environment from the raster file


#creates an empty list
environment = []

#uses the built in open function to read the raster file

with open('drunk.plan.txt') as f:
    for row in f:
        #breaks down rown in the text file into smaller chunks
        rowlist = row.split(',')
        rowlist_of_lists = [int(x) for x in rowlist]
        #appends the integer values to the empty list 'environment'
        environment.append(rowlist_of_lists)

#creates an integer variable for the dimensions of the environment        
env_limits = len(environment)  

"""
#visualises the environment in pyplot to test whether the environment is read correctly

plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment)

"""
#Creating the pub

#using pandas' read_csv function creates a dataframe called pubfinder from the raster file
pubfinder = pandas.read_csv('drunk.plan.txt')


#creates two empty lists for the vertical and horizontal dimesnions of the pub
pubx = []
puby = []



#cycles through every variable in the dataframe
for row in range(len(pubfinder)): 
         for col in range(len(pubfinder)):
             #checks the all coordinates for values of 1, if one is found appends the
             #row and column index of the point to the pubx and puby lists respectively
             if pubfinder.iat[row,col] == 1:
                 pubx.append(row)
                 puby.append(col)

"""
#Checks that the pub has been correctly identified by plotting it with pyplot

plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment)
plt.scatter(pubx, puby)       
plt.show()       
"""

#creates a list containing all the "adresses" of the houses 
adresses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,\
          120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

#creates an empty list for our agents
agents = [] 

#calls the agent framework and creates a list of agent objects who each have
#a location in the environment, specifically in the pub, and a unique "adress" 
for i in range (25):
    agents.append(agentframework_drinkers.Agent(environment, agents,\
                                                pubx,puby, adresses[i]))

"""    
#plots the drinkers and the environment, to test that they have been created correctly

plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment) 
for agent in agents:
    plt.scatter(agent.x, agent.y, c = 'snow')    
""" 



#Animating the model

#creates a 5 by 5 figure object
fig = plt.figure(figsize=(5, 5))

#creates a set with the adresses as this will be faster
#than a list for checking if an agent is at a house
adresses_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,\
          120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250}



def update(frame_number):
    
    #clears the environment from the last iteration
    fig.clear() 
    #plots the environment
    plt.imshow(environment)
    plt.xlim(0, agents[0].env_limits-1)
    plt.ylim(0, agents[0].env_limits)
    #plots the "pub"
    plt.scatter(pubx, puby)
 
    
    for agent in agents:  
        
        #calls the agent framework and updates 
        agent.move()
        
        #plots the agent in the environment
        plt.scatter(agent.x, agent.y, c = 'snow')  
        
        #cheks to see if the agents "adress" corresponds to its location
        if pubfinder.iat[agent.x, agent.y] == agent.adresses:
            #if above is TRUE, remouves the agent from teh simulation and prints a message 
            agents.remove(agent)
            print("The person who lives at house number", agent.adresses,"has found their way home")
        
        #calls the agent framework to update the environment  
        agent.leave_footprint(pubfinder, adresses_set)
            
           
    #print(len(agents))
   
    #print(frame_number)
    
    #prints a message if all the agents find their way home
    if len(agents) == 0:
        print("Everybody found their way home!")
    
    #checks how many agents aren't "home" (len(agents))at the end of 
    #the model and prints an appropiate message  
    if frame_number == num_of_iterations-1:
        if len(agents) == 25:
            print ("Nobody found their way home.")
        elif len(agents) == 24:
            print("Only 1 person found their way home")
        else:
            print("Only", 25-len(agents), "people found their way home.")
    
#defines the parameters of our animation         
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False,\
                                               frames=num_of_iterations)

#looks for a fig object and opens the window in which it visualises it
plt.show()

#creates a new file csv file called density_map.txt
with open('density_map.txt', 'w', newline='') as output:
            csvwriter = csv.writer(output, delimiter=',',
                                   quoting=csv.QUOTE_MINIMAL)
            #writes the density file by printing the environment printing row by row
            for row in environment:
                csvwriter.writerow(row)