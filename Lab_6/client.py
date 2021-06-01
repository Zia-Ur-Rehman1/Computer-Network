# Import socket module
import socket
import pickle
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 5050

# connect to the server on local computer
s.connect(('192.168.100.50', port))
print("Connected with server")
while True:
    choice=input(pickle.loads(s.recv(1024)))
    s.send(pickle.dumps(choice))
    message = input(pickle.loads(s.recv(1024)))
    s.send(pickle.dumps(message))
    print(pickle.loads(s.recv(1024)))
    s.close()
    break
# close the connection