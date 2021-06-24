
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
user=[]
while True:
    choice=input(pickle.loads(s.recv(1024)))
    s.send(pickle.dumps(choice))
    message = (pickle.loads(s.recv(1024)))
    for i in message:
        user.append(input(i))
    s.send(pickle.dumps(user))
    message = (pickle.loads(s.recv(1024)))
    print(message)
    continue
    # s.close()
    # break
# close the connection