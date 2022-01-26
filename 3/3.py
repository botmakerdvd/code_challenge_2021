#!/usr/bin/python3
import ast
from fractions import Fraction
def as_2_dict(asi):
	asi=asi.replace("=","':'")
	asi=asi.replace(",","','")
	dic="{'"+asi+"'}"
	return dic
def tup_2_dict(tup):
	tup=tup.replace(")]","'}")
	tup=tup.replace("[(","{")
	tup=tup.replace("), (",";")
	tup=tup.replace(", ",":'")
	dic=tup.replace(";","',")
	return dic
def dic_2_dict(dic):
	dic=dic.replace(": ",": '")
	dic=dic.replace(",","',")
	dic=dic.replace("}","'}")
	return dic



n = int(input())
for case in range(n):
    
	data = input().split("|")
	word_a=data[0].split("-")[0]
	word_b=data[0].split("-")[1]
	values=data[1]
	if values[0] == "{":
		dic=dic_2_dict(values)
	elif values [0] == "[":
		dic=tup_2_dict(values)
	else:
		dic=as_2_dict(values)
 
	key_dic=ast.literal_eval(dic)
	word_a_points=0
	word_b_points=0
	for element in word_a:
		word_a_points=word_a_points + Fraction(key_dic[element])
	for element in word_b:
		word_b_points=word_b_points + Fraction(key_dic[element])

	if(word_a_points > word_b_points):
		print("Case #"+str(case+1)+": "+word_a)
	elif(word_b_points > word_a_points):
		print("Case #"+str(case+1)+": "+word_b)
	else:
		print("Case #"+str(case+1)+": -")