#!/usr/bin/python3
#I entered uhznaf to text   in google and the second result speaks about ROT13
#so i enter plyba:xvyy_nyy_uhznaf into https://codebeautify.org/rot13-to-text-converter and i got
#cylon:kill_all_humans
#with this user and password i could enter into website, and I download a file which the I unzip.
#finnally a little code here to convert that file into a 15 numbers string
file = open("here-is-the-position", "rb")


byte = file.read(1)
contain=[]
result=[]
while byte:
	byte = file.read(1)
	contain.append(byte)

for i in range(len(contain)-2):
	if contain[i]==b'\xe2':
		if contain[i+2]==b'\x8b':
			result.append(0)
		elif contain[i+2]==b'\x8c':
			result.append(1)
finalword=[]
for i in range(int(len(result)/8)):
	finalword.append(result[8*i:8*(i+1)])
finalstring=[]
for word in finalword:
	finalstring.append(chr(int(word[0]*128+word[1]*64 + word[2]*32 + word[3]*16 + word[4]*8 +word[5]*4 +word[6]*2 +word[7])))
for i in finalstring:
    print(i, end="")