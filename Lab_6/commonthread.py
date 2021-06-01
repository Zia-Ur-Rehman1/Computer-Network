from threading import Thread
import pickle
import socket

class commonThread(Thread):
    def __init__(self, clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.echo_server=('192.168.100.50', 5051)
        self.palindrome=('192.168.100.50', 5052)
        self.length_server=('192.168.100.50', 5053)
    
    def run(self):
        print("Client Connected")
        message="Press 1 for Echo\n"+"Press 2 for \n"+ "Press 3 for Palindrome\n"
        self.clientsocket.send(pickle.dumps(message))
        choice = pickle.loads(self.clientsocket.recv(1024))
        if(choice =='1'):
            self.communicate(self.echo_server)        
        elif(choice =='2'):
            self.communicate(self.palindrome)        
        else:
            self.communicate(self.length_server)        
            
    def communicate(self,server):    
        s = socket.socket()
        s.connect(server)
        self.clientsocket.send(s.recv(1024))
        s.send(self.clientsocket.recv(1024))
        self.clientsocket.send(s.recv(1024))
            
            