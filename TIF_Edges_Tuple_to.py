#!/usr/bin/python
# coding: UTF-8
 
# CSVファイルの読み込み
 
import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite 
from decimal import Decimal

G=nx.DiGraph()
 
filename = "TIG_TF_show.csv"

csvfile = open(filename) #1~300

# print G.node

ib = 0
for row in csv.reader(csvfile):
	ia = 0
	while ia < 137:
		if Decimal(row[ia]) < 0.05 :
			ia += 1
			print "fuck"
		else:
			print row[ia]
			print ia
			print ib
			G.add_edges_from([(ib,ia)],weight=row[ia])
			ia += 1
			print "ass"
	
	ib += 1

print G.number_of_nodes()
print G.number_of_edges()

list = G.edges()

filename1 = "table02.csv"
writecsv = csv.writer(file(filename1, 'w'), lineterminator='n')

i=0
while list:
	tuple = list[i]
	writecsv.writerow([tuple[0],tuple[1]])
	print tuple[0]
	i += 1


csvfile.close()


