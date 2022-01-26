#!/usr/bin/python3
n = int(input())
for i in range(n):
    result_dices = input().split(":")
    needed=int(result_dices[0])+int(result_dices[1])+1
    if needed < 13 :
        print("Case #"+str(i+1)+": "+str(needed))
    else:

        print("Case #"+str(i+1)+": -")
