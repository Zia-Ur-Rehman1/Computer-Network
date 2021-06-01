# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('192.168.100.50', port))
print("Coneected with server")
while True:
    message = s.recv(1024).decode("utf-8")
    username = input(message)
    s.send(username.encode("utf-8"))
    message = s.recv(1024).decode("utf-8")
    password = input(message)
    s.send(password.encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
 
# close the connection
