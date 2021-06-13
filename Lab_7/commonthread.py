from threading import Thread
import pickle
import socket
user_dict={}
class commonThread(Thread):
    def __init__(self, clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.echo_server=('192.168.100.50', 5051)
        self.palindrome_server=('192.168.100.50', 5052)
        self.length_server=('192.168.100.50', 5053)
        self.identity_server=('192.168.100.50', 5054)
    def run(self):
        print("Connected")
        checker=pickle.loads(self.clientsocket.recv(1024))
        if(checker=='0'):
            message=["Enter Username\n","Enter Password\n"]
            self.clientsocket.send(pickle.dumps(message))
            valid=self.authenticate(self.clientsocket.recv(1024),self.identity_server)
            if(valid==1):
                message="1:For Echo Service\n"+"2:For Palindrome Service\n"+"3:For Length Service\n"
                self.clientsocket.send(pickle.dumps(message))
                choice=pickle.loads(self.clientsocket.recv(1024))
                if(choice[0] in user_dict and user_dict[choice[0]]==choice[1]):
                    if(choice[2] =='1'):
                        self.clientsocket.send(pickle.dumps(self.echo_server))
                        remove=pickle.loads(self.clientsocket.recv(1024))
                        del user_dict[remove]
                    elif(choice[2] =='2'):
                        self.clientsocket.send(pickle.dumps(self.palindrome_server))
                        remove=pickle.loads(self.clientsocket.recv(1024))
                        del user_dict[remove]
                    elif(choice[2] =='3'):
                        self.clientsocket.send(pickle.dumps(self.length_server))
                        remove=pickle.loads(self.clientsocket.recv(1024))
                        del user_dict[remove]
            
        else:
            self.clientsocket.send(pickle.dumps("Give User"))
            user=pickle.loads(self.clientsocket.recv(1024))
            if(user[0] in user_dict and user_dict[user[0]]==user[1]):
                self.clientsocket.send(pickle.dumps("1"))
            else:
                self.clientsocket.send(pickle.dumps("0"))
    # Verify User
    def authenticate(self,login_info,server):
        s = socket.socket()
        s.connect(server)
        s.send(login_info)
        username=pickle.loads(login_info)
        check=pickle.loads(s.recv(1024))
        if(check[0]=='1'):
            user_dict[username[0]]=check[1]
            self.clientsocket.send(pickle.dumps(check))
            return(1)
        else:
            self.clientsocket.send(pickle.dumps(check))
            return(0)
            
            
            