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
        self.client_resp=[]
    def run(self):
        print("Connected")
        # List Req
        client_req=pickle.loads(self.clientsocket.recv(1024))
        if(client_req=="0x0000"):
            hex_string="0x0010"
            self.client_resp=onlyfiles.copy()
            self.client_resp.insert(0,len(onlyfiles))
            self.client_resp.insert(0,hex_string)
            self.clientsocket.send(pickle.dumps(self.client_resp))
            
        # File Req
        client_req=pickle.loads(self.clientsocket.recv(1024))
        print(client_req)
        self.client_resp.clear()
        if(client_req[0]=="0x0001" and client_req[1] in onlyfiles):
            print("File req Recived")
            hex_string="0x0011"
            self.client_resp.append(hex_string)
            self.client_resp.append(client_req[1])
            status=os.stat(join(path,client_req[1]))
            self.client_resp.append(status.st_size)
            print(self.client_resp)
            self.clientsocket.send(pickle.dumps(self.client_resp))
            print("File req sended")
            self.send_file_chunk()
    def send_file_chunk(self):
        CHUNK_SIZE = 100
        offset=0
        hex_string="0x0012"
        self.client_resp.clear()
        f = open(join(path,onlyfiles[0]), 'r')
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            self.client_resp.append(hex_string)
            self.client_resp.append(offset)
            self.client_resp.append(chunk)
            print(chunk)
            self.clientsocket.send(pickle.dumps(self.client_resp))
            self.client_resp.clear()
            offset=pickle.loads(self.clientsocket.recv(1024))
            chunk=f.read(CHUNK_SIZE) #read the next chunk
            offset+=1
                
        #loop until the chunk is empty (the file is exhausted)
        f.close()
        
        self.clientsocket.send(pickle.dumps("End"))
        