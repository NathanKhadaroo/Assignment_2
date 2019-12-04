# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:15:51 2019

@author: msra2nk3
"""

import random


class Agent():
    
#Creates our drinkers and gives them acces to the information they 
#need for their behaiviour  
    def __init__ (self, environment, agents, pubx, puby, adresses):
         
         self.environment = environment
         self.env_limits = len(environment)
         #initialies the starting coordinates of the drunks somewhere in the pub
         self.pubx = pubx
         self.puby = puby
         self.x = random.randrange (min(pubx), max(pubx)+1, 1)
         self.y = random.randrange (min(puby), max(puby)+1, 1)
         self.agents = agents
         #assigns a home to each agent
         self.adresses = adresses
         
     
    def move(self):
        #randomly moves agents by 7 steps in both dimensions
            if random.random() < 0.5:
                self.y = (self.y + 5)
            else:
                self.y = (self.y - 5)
        
            if random.random() < 0.5:
                self.x = (self.x + 5)
            else:
                self.x = (self.x - 5)
       #checks to see if the agents movement pushes them off the border of the
       #environment, if it does it instead outputs their location as at the border
            if self.x < 0:
                self.x = 0
            
            if self.y < 0:
                self.y = 0
                
            if self.x > 300:
                self.x = 300
                
            if self.y > 300:
                self.y = 300
                
    def found_home(self, agents):
        agents.remove(self)
        