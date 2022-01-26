#!/usr/bin/python3
import numpy as np
		
def check_crash(image1, image2):
	imageresult=image1 + image2
	if 2 in imageresult:
		return 1
	else:
		return 0

def coincidencia(imagen1,imagen2,sprite1,sprite2,axis):
	crash=0
	image1_start=0
	image1_end=0
	image2_start=0
	image2_end=0
	start1 =  imagen1[axis]
	start2 =  imagen2[axis]
	ending1 = start1 + sprite1[axis]
	ending2 = start2 + sprite2[axis]
	if start2 >= start1 and start2 <= ending1:
		crash=1
		if ending2 <=ending1 :
			image1_start=start2-start1
			image1_end=start2-start1+sprite2[axis]
			image2_start=0
			image2_end=sprite2[axis]
		else  :
			image1_start=start2-start1
			image1_end=sprite1[axis]
			image2_start=0
			image2_end=ending1-start2
			    
	elif start2 <= start1 and ending2 >= start1:
		crash=1
		if ending2 <=ending1 :
			image1_start=0
			image1_end=ending2-start1
			image2_start=start1-start2
			image2_end=sprite2[axis]			
		else:
			image1_start=0
			image1_end=sprite1[axis]
			image2_start=start1-start2
			image2_end=start1-start2 +sprite1[axis]
 
	return crash, image1_start, image1_end, image2_start, image2_end

sprites=[]


n = int(input())
D = int(input())
for sp in range(D):
	spritesize=input().split(" ")
	cols=int(spritesize[0])
	rows=int(spritesize[1])
	sprite_matrix=[]
	for row in range(rows):
		readed_row=[int(item) for item in list(input())]
		sprite_matrix.append(readed_row)
	sprite_matrix =np.matrix(sprite_matrix)
	sprite={'y' : rows,
			'x' : cols,
			'matrix': sprite_matrix}
	sprites.append(sprite)
for case in range(n):
	crashes=0
	images=[]
	P = int(input())
	for p in range(P):
		p_data=input().split(" ")
		image={ 'spriteID' : int(p_data[0]),
				'x' : int(p_data[1]),
				'y' : int(p_data[2])}
		images.append(image)
	sortedimages = sorted(images, key=lambda d: d['x']) 
	for i in range(len(sortedimages)):
		for j in range (i+1,len(sortedimages)):
			if(sortedimages[j]["x"] > sortedimages[i]["x"]+sprites[sortedimages[i]["spriteID"]]["x"]): 
				break
			chancecrash_x, image1_start_x, image1_end_x, image2_start_x, image2_end_x = coincidencia(sortedimages[i],sortedimages[j],sprites[sortedimages[i]["spriteID"]], sprites[sortedimages[j]["spriteID"]],"x")
			if chancecrash_x == 0:
				continue #crash in X and Y is requested, if there is no crash in X, do not check Y 
			chancecrash_y, image1_start_y, image1_end_y, image2_start_y, image2_end_y = coincidencia(sortedimages[i],sortedimages[j],sprites[sortedimages[i]["spriteID"]], sprites[sortedimages[j]["spriteID"]],"y")
			if chancecrash_y == 0:
				continue #crash in X and Y is requested 

			image1_sub= sprites[sortedimages[i]["spriteID"]]["matrix"][image1_start_y:image1_end_y, image1_start_x:image1_end_x]
			image2_sub= sprites[sortedimages[j]["spriteID"]]["matrix"][image2_start_y:image2_end_y, image2_start_x:image2_end_x]
			if check_crash(image1_sub,image2_sub) == 1:
				crashes=crashes+1
	print("Case #"+str(case+1)+": "+str(crashes))
	
