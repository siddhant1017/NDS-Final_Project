#!/usr/bin/python3
from scapy.all import *

# from a random src to local DNS server
IPpkt  = IP(src='1.2.3.4',dst='10.9.0.53')
# from a random sport to DNS dport
UDPpkt = UDP(sport=12345, dport=53,chksum=0)

Qdsec    = DNSQR(qname='twysw.example.com') 
DNSpkt   = DNS(id=0xAAAA, qr=0, qdcount=1, qd=Qdsec)
Querypkt = IPpkt/UDPpkt/DNSpkt
