#!/usr/bin/python3

n = int(input())
for case in range(n):
	data = input().split()
	num_pokes = int(data[0])
	num_rows = int(data[1])
	num_cols = int(data[2])
	num_letters= int(num_rows) * int(num_cols)
	pokemons=[]
	for k in range(num_pokes):
		pokemons.append(list(input()))

	fulltext = []
	for row in range(num_rows):
		fulltext = fulltext + input().split()
	k=0
	remaining_pokes=num_pokes
	while k < remaining_pokes:
		found =0
		pokemon_len=len(pokemons[k])
		l=0
		remaining_letters= num_letters
		while l < remaining_letters:
			if (fulltext[l:l+pokemon_len]==pokemons[k]) or (fulltext[l:l+pokemon_len] == pokemons[k][::-1]):
				del fulltext[l:l+pokemon_len]
				pokemons.remove(pokemons[k])
				k=0 #
				found = 1
				remaining_pokes =remaining_pokes - 1
				remaining_letters= remaining_letters - pokemon_len
				break
			l=l+1
		if found ==0:
			k=k+1
	print("Case #"+str(case+1)+": "+''.join([str(elem) for elem in fulltext]))	
