#!/usr/bin/python
# coding: UTF-8
 
# CSVファイルの読み込み
 
import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite 
from collections import deque


G=nx.DiGraph()
 
filename = "TF_analysis.csv"

csvfile = open(filename) #1~300

Gene_name =[]


for row in csv.reader(csvfile):
   G.add_edges_from([(row[0],row[1])],weight=row[2])
   Gene_name.append(row[0])

#queue = deque([row[0]])
#print G.node
#print Gene_name

#Model of comparing networks
print "average_neighbor_degree"
dict = nx.average_neighbor_degree(G) 
print dict

#異常検出のリスト
put_aside = []

for x in Gene_name:
   y = str(x)
   print dict[y] 
   if dict[y] > 2.0:
    put_aside.append(dict[y])



print "degree_assortativity_coefficient"
print nx.degree_assortativity_coefficient(G)

print "degree_pearson_correlation_coefficient"
print nx.degree_pearson_correlation_coefficient(G)  
#print nx.k_nearest_neighbors(G)



print bipartite.closeness_centrality(G,G.node)

print nx.degree_centrality(G)

print nx.betweenness_centrality(G)

#print nx.current_flow_closeness_centrality(G, normalized=True, weight='weight', dtype='float', solver='lu')

#centrality=nx.eigenvector_centrality(G)
#print(['%s %0.2f'%(node,centrality[node]) for node in centrality])
#print nx.eigenvector_centrality(G, max_iter=100, tol=1e-02, nstart=None)

#print nx.communicability(G)

#print nx.triangles(G)
#directed Graphでなくてはだめ

#print(nx.clustering(G,0))
#print nx.average_clustering(G)

# print nx.diameter(G, e=None)
#print nx.center(G, e=None)

print nx.max_flow(G, 'Fosl2.48h', 'Hoxa9.48h')

#print nx.network_simplex(G)

#print nx.pagerank(G,alpha=0.9)

print nx.pagerank_numpy(G,alpha=0.9)

print nx.hits_numpy(G)

# print(nx.shortest_path(G,source=0,target=4))
# print(nx.average_shortest_path_length(G))

#paths = nx.all_simple_paths(G, source=0, target=3, cutoff=2)
#print(list(paths))

csvfile.close()