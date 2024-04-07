import socket
host = "192.168.1.14"
port = 12345
obj = socket.socket()
obj.bind((host,port))
message = input("enter message : ")

obj.send(message.encode)
data = obj.recv(1024).decode()
print("received from server: ",+ data )