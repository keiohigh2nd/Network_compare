#!/usr/bin/python
# coding: UTF-8
 
# CSVファイルの読み込み
 
import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite 


G=nx.DiGraph()
 
filename = "TFnew_1000.csv"

csvfile = open(filename) #1~300

# print G.node

for row in csv.reader(csvfile):
   G.add_edges_from([(row[0],row[1])],weight=row[2])

print "From HERE
"
print G.number_of_nodes()
print G.number_of_edges()


print "average_neighbor_degree"
dict = nx.average_neighbor_degree(G) 
list1 = dict.keys()
list2 = dict.values()
print list1
print list2

print "degree_assortativity_coefficient"
print nx.degree_assortativity_coefficient(G)

print "degree_pearson_correlation_coefficient"
print nx.degree_pearson_correlation_coefficient(G)  
#print nx.k_nearest_neighbors(G)
print "STOP HERE"

print "bipartite.closeness_centrality(G,G.node)"
dict2 = bipartite.closeness_centrality(G,G.node)
list3 = dict2.values()
print list3

print "nx.degree_centrality(G)"
dict3 = nx.degree_centrality(G)
list4 = dict3.values()
print list4

print "nx.betweenness_centrality(G)"
dict4 = nx.betweenness_centrality(G)
list5 = dict4.values()
print list5
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

#print "nx.max_flow(G, 'Fosl2.48h', 'Hoxa9.48h')"
#print nx.max_flow(G, 'Fosl2.48h', 'Hoxa9.48h')


#print nx.network_simplex(G)

#print nx.pagerank(G,alpha=0.9)

#print "nx.pagerank_numpy"
#print nx.pagerank_numpy(G,alpha=0.9)

print "hits_numpy"
dict5 = nx.hits_numpy(G)

print dict5

# print(nx.shortest_path(G,source=0,target=4))
# print(nx.average_shortest_path_length(G))

#paths = nx.all_simple_paths(G, source=0, target=3, cutoff=2)
#print(list(paths))
csvfile.close()
