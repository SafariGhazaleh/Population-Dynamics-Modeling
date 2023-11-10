#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 17:16:56 2022

@author: Ghazaleh Safari

"""

"""
Problem: 
    - making a network by networkx module
    - how many frinds does each person have in this network?
    - how many frinds (on average) does each friend of her\him?
    - examine the feld's friendship paradox
"""

"""Import modules"""
import numpy as np
import networkx as nx


"""creating a network by networkx module with 100 nodes and arbitrary 
probability"""
n = 100
p = 0.9
#k = 5
G = nx.erdos_renyi_graph(n, p)
#G = nx.barabasi_albert_graph(n, k)
#G = nx.watts_strogatz_graph(n, k, p)
"""
Defining the function that counts the mean of friends' friends for each node 
"""
def Ave(Graph, x):
    return np.mean([nx.degree(Graph, v) for v in Graph.neighbors(x)])


"""
Computing and saving the number of friends, name of them and the average of 
their friends for each node in the lists
"""

"""Making 3 empty lists"""
num_friends = []
List_friends = []
Ave_friends = []

"""Using the for loop to compute the above stuff and save them in the lists"""
for i in range (n):
       
    """save the number of each node's friends in the list """
    num_friends.append(nx.degree(G, i))
    
    """save the list for each node's friends in the list """
    List_friends.append (list(G.neighbors(i)))
    
    """save the average of friends' friends for each node in the list"""
    Ave_friends.append(Ave(G, i))

"""Rounding the Ave_friends"""
Ave_friends = [round(num, 1) for num in Ave_friends]


"""Printing the results of above"""
print ("The number of each person's friends", num_friends)
print ("The list of friends for each person", List_friends)
print ("The average of friends' friends for each person", Ave_friends)

    
"""Changing lists to numpy arrays to comapre their elements"""
num_friends = np.array(num_friends)
Ave_friends = np.array(Ave_friends)


"""
Examining the feld's friendship paradox: Based on the Scott Feld’s
friendship  paradox "our friends have (on average) more friends
than we do". So we save those individuals who have friends more
than the average of their friends'  friends in a list (as the
contradictive samples).
"""

"""Counting the contradictive samples"""
num_paradox = 0

"""Making an empty list to save them"""
List_paradox = []

"""Examine the feld's friendship paradox by the For Loop"""
for j in range (n):    
    if num_friends[j] > Ave_friends[j]:
        num_paradox += 1
        List_paradox.append(j)
        print ("Scott Feld’s paradox does not holds for", j)

print (f"paradox does not hold {len(List_paradox)}% in this network")
