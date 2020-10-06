# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:29:31 2020

@author: jojo
"""
#nous avons utilisé la bibliotheques postman_problems qui permet de determiner le cycle le plus court qui passe par chaque noeuds au moins 1 fois

import math
import numpy as np
import networkx as nx
import pandas as pd
from postman_problems.solver import cpp
from postman_problems.stats import calculate_postman_solution_stats
import logging
import pkg_resources

#%%
#creation d'une classe point
class Point():
    def __init__(self,longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

def distance(point1,point2):
    k = 6371
    #calcule de la distance, methode avec loi des sinus
    d = k*math.acos(round(math.sin(point1.latitude*math.pi/180)*math.sin(point2.latitude*math.pi/180)+math.cos(point1.latitude*math.pi/180)*math.cos(point2.latitude*math.pi/180)*math.cos(point1.longitude*math.pi/180-point2.longitude*math.pi/180),5))
    return d
#%%
    
#on recupere les coordonnées de nos points
nodelist1 = pd.read_csv('topo.txt')
points = []
for i in range(len(nodelist1)):
    exp = Point(nodelist1['longitude'][i],nodelist1['latitude'][i])
    points.append(exp)
#%%
dist = []
for i in range(len(points)):
    for j in range(len(points)):
        dist.append(distance(points[i],points[j]))
#%%
test = pd.read_csv('données_test.csv')
dist_fin = []
for i in range(len(test)):
    dist_fin.append(dist[test['node1'][i]*test['node2'][i]])

#Graph = np.array(dist).reshape(10,10)

df = pd.DataFrame({'node1':test['node1'],'node2':test['node2'],'trail':test['trail'],'distance':dist_fin})

df.to_csv('données_test.csv')
#%%
# find CPP solution
node_depart=(input(""))
circuit, graph = cpp(edgelist_filename='données_test.csv', start_node='4')

#affiche le circuit
for e in circuit:
    print(e)

# Affiche les informations sur le circuit
for k, v in calculate_postman_solution_stats(circuit).items():
    print(k, v)