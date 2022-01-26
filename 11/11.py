#!/usr/bin/python3 
def count_sames(words):
	count=0
	len_shortest_word = len(min(words, key=len))
	for i in range(len_shortest_word):
		words_same=1
		for j in range(1,len(words)):
			if words[j][i]==words[0][i]:
				words_same +=1
			else:
				break
		if words_same==len(words):
			count+=1
		else:
			break
	return count


T = int(input())
for test in range(T):
	cases = input().split(" ")
	N=int(cases[0])
	K=int(cases[1])
	words=[]
	points=0
	for i in range(N):
		words.append(input())
	words=sorted(words)

	while(len(words)) > 0:
		resultado=[]
		for i in range(len(words)-K+1):
			comparacion=[]
			for j in range(K):
				comparacion.append(words[i+j])
			resultado.append(count_sames(comparacion))

		max_value=max(resultado)
		max_index = resultado.index(max_value)
		points=points+max_value
		for i in range(K):
			words.remove(words[max_index])

	print("Case #"+str(test+1)+": "+str(points))