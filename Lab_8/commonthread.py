from threading import Thread
import pickle
from os import listdir
from os.path import isfile, join
import os

path = 'files/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

class commonThread(Thread):
    def __init__(self, clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket
    def run(self):
        print("Connected")
        # List Req
        client_req=pickle.loads(self.clientsocket.recv(1024))
        client_resp=[]
        if(client_req=="0x0000"):
            hex_string="0x0010"
            client_resp=onlyfiles.copy()
            client_resp.insert(0,len(onlyfiles))
            client_resp.insert(0,hex_string)
            self.clientsocket.send(pickle.dumps(client_resp))
            
        # File Req
        client_req=pickle.loads(self.clientsocket.recv(1024))
        print(client_req)
        client_resp.clear()
        if(client_req[0]=="0x0001" and client_req[1] in onlyfiles):
            print("File req Recived")
            hex_string="0x0011"
            client_resp.append(hex_string)
            client_resp.append(client_req[1])
            status=os.stat(join(path,client_req[1]))
            client_resp.append(status.st_size)
            print(client_resp)
            self.clientsocket.send(pickle.dumps(client_resp))
            print("File req sended")
            
            