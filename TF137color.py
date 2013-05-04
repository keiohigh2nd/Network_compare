#!/usr/bin/python
# coding: UTF-8
 
# CSVファイルの読み込み
 
import csv
import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
 
filename = "TFnew48_RESULT.csv"
filename0 = "TFnew48_RESULT0.csv"
filename1 = "TFnew48_RESULT1.csv"
filename2 = "TFnew48_RESULT2.csv"
csvfile = open(filename) #1~30
csvfile0 = open(filename0) #30~100
csvfile1 = open(filename1) #100~200
csvfile2 = open(filename2) #200~300


for row in csv.reader(csvfile):
   G.add_edges_from([(row[0],row[1])], color='red')

for row in csv.reader(csvfile0):
  G.add_edges_from([(row[0],row[1])], color='blue')

for row in csv.reader(csvfile1):
  G.add_edges_from([(row[0],row[1])], color='green')

for row in csv.reader(csvfile2):
  G.add_edges_from([(row[0],row[1])])




 
csvfile.close()
csvfile1.close()
csvfile2.close()
nx.draw(G)
plt.savefig('TF300color.png')
nx.draw_graphviz(G)
nx.write_dot(G,'TF300color.dot')
plt.show()
