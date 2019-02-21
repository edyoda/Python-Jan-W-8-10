# TCP 
# UDP 

# www.zekelabs.com get/post request TCP sockets 

# client socket			TCP					sockets 	server 

# Server :

# ip address 
# port no 

# bind(hostname,port )
# listen 
# accept
# send/recv => byte 

# Clinet :
# connect(host,port)
# send/recv

import socket

host = socket.gethostname()
port = 2228
# print(host)

# getfqdn("")
# gethostbyname("")

conn = socket.socket()
conn.bind((host,port))
conn.listen(1)

sock_client , addr = conn.accept()
print(addr)
sock_client.send(b"data from server")
conn.close()




