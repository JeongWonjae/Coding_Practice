from scapy.all import *

packets=rdpcap("scapy_ex1.pcap")
print(packets)

#length
print(len(packets))

#select
print(packets[2554]['IP'].version)
print(packets[2554]['IP'].proto)
print(packets[2554]['IP'].ttl)
print(packets[2554]['IP'].src)
print(packets[2554]['IP'].dst)

#select specific condition
for p in packets:
    if p['IP'].src=="45.119.97.203":
        print (p['IP'].src+" -> "+p['IP'].dst)

#fetch image file on ICMP packets
flag=""
for p in packets:
    if p['IP'].src="1.1.1.1":
        flag+=p['Raw'].load