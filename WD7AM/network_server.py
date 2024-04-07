import socket

host = "127.0.0.1"
port = 12345
server = socket.socket()
print("socket created")
server.bind((host,port))
print("binded")
server.listen()
print("listening....")
connection, addr = server.accept()
print("connection", str(addr))
data  = connection.recv(1024).decode()
print("message from client: " ,data)
connection.close()