#!/usr/bin/python3
f = open('Invictus.txt', 'rb')
byte_list = []
keys= []
int_keys = []
byte = f.read(1)
while byte != b"":
	byte_list.append(byte)
	byte = f.read(1)

for i in range(len(byte_list)):
	if byte_list[i] == b'\xf3':
		if byte_list[i+1] == b'\xa0':
			keys.append(byte_list[i+2:i+4])

for i in range(len(keys)):
		if keys[i][0]== b'\x81' :
			int_keys.append(chr(((int.from_bytes(keys[i][0], byteorder='big')-129)*256)+(int.from_bytes(keys[i][1], byteorder='big'))-110))
		else:
			int_keys.append(chr(((int.from_bytes(keys[i][0], byteorder='big')-129)*256)+(int.from_bytes(keys[i][1], byteorder='big'))-302))
print("".join([str(elem) for elem in int_keys]))
	