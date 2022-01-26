#!/usr/bin/python3 
import networkx as nx
testcases=int(input())
for case in range(testcases):
	ganancia= {}
	G = nx.DiGraph()
	markets=int(input())
	for market in range(markets):
		vertices = int(input().split(" ")[1])
		for vertice in range(vertices):
			vertice_data=input().split("-")
			inputcoin=vertice_data[0]
			outputcoin=vertice_data[2]
			if(outputcoin == "BTC"):
				outputcoin = "ENDBTC"
			exchangewinning=int(vertice_data[1])
			if exchangewinning !=0: #if it is 0 it is not reccomended 
				G.add_edge(inputcoin,outputcoin)
				if (inputcoin,outputcoin) in ganancia:
					if ganancia[inputcoin,outputcoin] < exchangewinning:
						ganancia[inputcoin,outputcoin] = exchangewinning
				else:
					ganancia[inputcoin,outputcoin] = exchangewinning
	paths=[]
	winning = 1
	try:
		for path in nx.all_simple_paths(G, "BTC","ENDBTC"):
			paths.append(path)
		paths.sort(key=len)
		for i in range(len(paths)):
			winning = 1
			for j in range(len(paths[i])-1) :
				if ganancia[paths[i][j],paths[i][j+1]] != 1 :
					winning= winning * ganancia[paths[i][j],paths[i][j+1]]
				if(path[i+1] == "BTC"):
					break
			if winning > 1:
				break
	except nx.exception.NodeNotFound:
		pass
	print("Case #"+str(case+1)+": "+str(winning))
	

