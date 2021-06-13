import socket
import pickle
import secrets 
            
user_dict={"Zia":"zia123"}

def main():
    s = socket.socket()
    print("Socket successfully created")
    port = 5054
    s.bind(('192.168.100.50', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("Identity service is listening")
    message=[]
    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        login_info=pickle.loads(c.recv(1024))
        if(login_info[0] in user_dict and user_dict[login_info[0]]==login_info[1]):
            message=("1",secrets.token_hex(nbytes=64)) 
            c.send(pickle.dumps(message))
        else:
            message = ["0","Username or Password Incorrect"]
            c.send(pickle.dumps(message))


if __name__ == "__main__":
    main()
