# Import socket module
import socket
import pickle
# Create a socket object
s = socket.socket()
service = socket.socket()

# Define the port on which you want to connect
port = 5050

# connect to the server on local computer
s.connect(('192.168.100.50', port))
print("Connected with server")
login = []
user_info = {}
serv = []
while True:
    # main server
    s.send(pickle.dumps("0"))
    message = pickle.loads(s.recv(1024))
    for i in message:
        login.append(input(i))
    message = pickle.dumps(login)
    s.send(message)
    message = pickle.loads(s.recv(1024))
    if(message[0] == '1'):
        user_info[login[0]] = message[1]
        # Ask for Service
        message = input(pickle.loads(s.recv(1024)))
        serv=(login[0],user_info[login[0]],message)
        s.send(pickle.dumps(serv))
        # Service Start
        server_addrs = (pickle.loads(s.recv(1024)))
        service.connect(server_addrs)
        serv=[login[0],user_info[login[0]]]
        service.send(pickle.dumps(serv))
        message=input(pickle.loads(service.recv(1024)))
        service.send(pickle.dumps(message))
        print(pickle.loads(service.recv(1024)))
        s.send(pickle.dumps(login[0]))
        s.close()
        break
    else:
        s.close()
        break

# close the connection
