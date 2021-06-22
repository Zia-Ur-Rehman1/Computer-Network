import socket
import pickle
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#
# socket.gethostname()
udp_host = "192.168.100.50"
udp_port = 12345
req_file=[]

msg="Connection"
sock.sendto(pickle.dumps(msg), (udp_host, udp_port))
data,addr=sock.recvfrom(1024)
print("Receied Messages:", pickle.loads(data), "form ",addr)
# Server Responded Yes

hex_string="0x0000"
sock.sendto(pickle.dumps(hex_string), (udp_host, udp_port))


data,addr=sock.recvfrom(1024)
message=pickle.loads(data)
print(message)

# file req
req_file.append("0x0001")
req_file.append(message[2])
print(req_file)
sock.sendto(pickle.dumps(req_file),(udp_host,udp_port))

# file response
data,addr=sock.recvfrom(1024)
message=pickle.loads(data)
if(message[0]=='0'):
    print(message[1])
    input("Press Enter to Exit")
else:
    end=message[2]/100
    file=""
    while(end>=0):
        data,addr=sock.recvfrom(1024)
        message=pickle.loads(data)
        file=file+message[2]
        end-=1
    print(file)
    input("Press Enter to Exit")
# close the connection

input("Enter")
