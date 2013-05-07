#!/usr/bin/python
# coding: UTF-8
 
# CSVファイルの読み込み
 
import csv
import networkx as nx
from networkx.algorithms import bipartite 
from collections import deque
import math
import sys
from collections import defaultdict
import numpy as np





G=nx.DiGraph()
 
filename = "TF_analysis.csv"

csvfile = open(filename) #1~300

Gene_name =[]

m = 8
n = 137
  
np.Array1 = n*[m*[0]]

for row in csv.reader(csvfile):
   G.add_edges_from([(row[0],row[1])],weight=row[2])
   Gene_name.append(row[0])

#queue = deque([row[0]])
#print G.node
#print Gene_name

#Model of comparing networks
print "average_neighbor_degree"
dict = nx.average_neighbor_degree(G) 

# print dict

#異常検出のリスト
put_aside = []

for x in Gene_name:
   y = str(x)
   put_aside.append(dict[y])

list1 = dict.keys()
list2 = dict.values()


print nx.triangles(G,0)

a = np.array([list1])
b = np.array([list2])


print np.dstack((a,b))