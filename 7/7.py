#!/usr/bin/python3
import telnetlib
from time import sleep
host = "codechallenge-daemons.0x14.net"
SIZE=100 #SIZE IN COLS AND ROWS OF MAZE
port = 4321
cur_pos=[]

telnet = telnetlib.Telnet()
telnet.open(host, port)
out = telnet.read_until("- bye\n".encode('ascii'), 1)
telnet.write('where am I\r\n'.encode('ascii'))
out = telnet.read_until(")\n".encode('ascii'), 1)
out = out.decode('ascii')
out = out.replace("(","")
out = out.replace(")\n","")
out = out.replace(", ",",")
cur_pos.append(int(out.split(",")[0]))
cur_pos.append(int(out.split(",")[1]))
grid=[(x,y) for x in range(SIZE) for y in range(SIZE)]
unchecked={n:float('inf') for n in grid}
unchecked[(cur_pos[0],cur_pos[1])] = 0
checked = {}
reversepath = {}
while unchecked:
	cur_pos=min(unchecked,key=unchecked.get)
	checked[cur_pos]=unchecked[cur_pos]
	telnet.write(('go to '+str(cur_pos[0])+','+str(cur_pos[1])+'\r\n').encode('ascii'))
	telnet.read_until("\n".encode('ascii'))
	telnet.write('is exit?\r\n'.encode('ascii'))
	out = telnet.read_until("No. Sorry, traveller...\n".encode('ascii'), 1)
	if(out != b'No. Sorry, traveller...\n'):
		break
	telnet.write('look\r\n'.encode('ascii'))
	out = telnet.read_until("\n".encode('ascii'), 1).decode('ascii')
	options=  out.replace(": ",":").replace("\n","").split(":")[1].split(" ")
	for diropt in ['west','east','north','south']:
		if diropt in options:
			if diropt== "west":
				new_pos=(cur_pos[0]+1,cur_pos[1])
				telnet.write(("west"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
				telnet.write(("east"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
			elif diropt== "east":
				new_pos=(cur_pos[0]-1,cur_pos[1])
				telnet.write(("east"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
				telnet.write(("west"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
			elif diropt== "north":
				new_pos=(cur_pos[0],cur_pos[1]+1)
				telnet.write(("north"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
				telnet.write(("south"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
			elif diropt== "south":
				new_pos=(cur_pos[0],cur_pos[1]-1)
				telnet.write(("south"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
				telnet.write(("north"+'\r\n').encode('ascii'))
				telnet.read_until("\n".encode('ascii'))
			if new_pos in checked:
				continue
			costtemp=unchecked[cur_pos]+1

			if costtemp < unchecked[new_pos]:
				unchecked[new_pos]=costtemp
				reversepath[new_pos]=cur_pos
	unchecked.pop(cur_pos)
fullPath=[]
fullPath.append(cur_pos)
cell=(19,17)
while cell!=(0,0):
	fullPath.append(reversepath[cell])
	cell=reversepath[cell]
fullPath.reverse()
print(*fullPath, sep = ", ")
telnet.close()
	