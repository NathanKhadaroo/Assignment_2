# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:15:51 2019

@author: msra2nk3
"""

import random


class Agent():
    
#Creates our drinkers and gives them acces to the information they 
#need for their behaiviour  
    def __init__ (self, environment, agents, pubx, puby, house):
         
         self.environment = environment
         
         #initialies the starting coordinates of the drunks somewhere in the pub
         self.pubx = pubx
         self.puby = puby
         self.x = random.randrange (min(pubx), max(pubx)+1, 1)
         self.y = random.randrange (min(puby), max(puby)+1, 1)
         self.agents = agents
         self.house = house
         
     
    def move(self):
            if random.random() < 0.5:
                self.y = (self.y + 1) % 300
            else:
                self.y = (self.y - 1) % 300
        
            if random.random() < 0.5:
                self.x = (self.x + 1) % 300
            else:
                self.x = (self.x - 1) % 300