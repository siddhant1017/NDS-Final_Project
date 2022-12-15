#!/bin/env python3

import socks

#Initializing socket for communication

sk = socks.socksocket()


sk.set_proxy(socks.SOCKS5, "192.168.20.99", 9000) # Setting the proxy to the given IP address and 9000 Port

host = "www.google.com"
sk.connect((host, 80)) 

serverrequest = b"GET / HTTP/1.0\r\nHost: " + host.encode('utf-8') + b"\r\n\r\n"
sk.sendall(severrequest)

# Wait to receive the response via Port 2048
serverresponse = sk.recv(2048)
while serverresponse:
  print(serverresponse.split(b"\r\n"))
  serverresponse= sk.recv(2048)