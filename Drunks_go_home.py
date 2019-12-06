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

#defining the nuber of iterations

num_of_iterations = 100000

#creates the environment from the raster file


environment = []



with open('drunk.plan.txt') as f:
    for row in f:
        rowlist = row.split(',')
        rowlist_of_lists = [int(x) for x in rowlist]
        environment.append(rowlist_of_lists)
        
env_limits = len(environment)  

"""
#Plots the bare environment to tests whether the environment is read correctly

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

#checks the all coordinates for value of 1, if a one is found appends the
#coordinates to pubx and puby lists
for row in range(len(pubfinder)): 
         for col in range(len(pubfinder)):
             if pubfinder.iat[row,col] == 1:
                 pubx.append(row)
                 puby.append(col)

"""
#Checks that the pub has been correctly identified by plotting it 

plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment)
plt.scatter(pubx, puby)       
plt.show()       
"""


#Create the drinkers and assigns them a house 
agents = [] 

adresses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,\
          120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

for i in range (25):
    agents.append(agentframework_drinkers.Agent(environment, agents,\
                                                pubx,puby, adresses[i]))


"""    
#plots the drinkers, to test that they have been created correctly

plt.xlim(0, env_limits)
plt.ylim(0, env_limits)
plt.imshow(environment) 
for agent in agents:
    plt.scatter(agent.x, agent.y, c = 'snow')    
""" 

#animation time

fig = plt.figure(figsize=(5, 5))

adresses_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,\
          120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250}

def update(frame_number):
    
    
    fig.clear()  
    plt.imshow(environment)
    plt.xlim(0, agents[0].env_limits)
    plt.ylim(0, agents[0].env_limits)
    plt.scatter(pubx, puby)
    plt.imshow(environment)
    
    for agent in agents:  
        
        agent.move()
        
        plt.scatter(agent.x, agent.y, c = 'snow')  
        
        if pubfinder.iat[agent.x, agent.y] == agent.adresses:
           
            agents.remove(agent)
            print("The person who lives at house number", agent.adresses,"has found their way home")
        
        agent.leave_footprint(pubfinder, adresses_set)
            
          
    
    #print(len(agents))
    #print(frame_number)
    if len(agents) == 0:
        print("Everybody found their way home.")
    
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

plt.show()




