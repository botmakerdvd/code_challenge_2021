#!/usr/bin/python3 
#initially readed ID from ICMP layer and it tells to reorder the frames 
# so now I read the load of ICMP layer and order them based on ICMP seq number 
from scapy.all import ICMP,  rdpcap

pcap = rdpcap('data.pcap')
file = open("sample.png","wb")
password={}
passwordlist=[]
for p in pcap:
	password[p[ICMP].seq] = p[ICMP].load
for i in range(1,214):
	passwordlist.append(password[i])
for element in passwordlist:
	file.write(element)
file.close()
#It is a PNG file containing a QR code so I decode it on 
#https://online-barcode-reader.inliteresearch.com/