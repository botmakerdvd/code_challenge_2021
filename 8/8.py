#!/usr/bin/python3
import networkx as nx
C = int(input())
for case in range(C):
	T = int(input())
	city_list=[]
	crit_cities=[]
	G= nx.Graph()
	for i in range(T):
		cities=input().split(",")
		G.add_edge(cities[0], cities[1])
	critical_paths=list(nx.articulation_points(G))
	
	if(len(critical_paths) == 0):
		print("Case #"+str(case+1)+": -")
	else:
		print("Case #"+str(case+1)+": ",end="")
		print(*sorted(critical_paths), sep = ",")
