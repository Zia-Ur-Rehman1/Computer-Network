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
req_file=[]
# List Req
hex_string="0x0000"
s.send(pickle.dumps(hex_string))
message=pickle.loads(s.recv(1024))
print(message)
# file req
req_file.append("0x0001")
req_file.append(message[2])
s.send(pickle.dumps(req_file))
message=pickle.loads(s.recv(1024))
wow=""
while(message!="End"):
    message=pickle.loads(s.recv(1024))
    wow=wow+message[2]
    s.send(pickle.dumps(message[1]))
print(wow)
input("Press Enter to Exit")
# close the connection
