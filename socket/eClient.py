import socket

host = socket.gethostname() 
port = 2228

socket = socket.socket()
socket.connect((host,port))
data = socket.recv(1024)
print(data)
socket.close()
