import socket
import pickle

def palin(n):
    if n == n[::-1]:
        return ("This word is palindrome")
    else:
        return ("This word is not palindrome")
def main():
    s = socket.socket()
    main_server=socket.socket()
    print("Socket successfully created")
    port = 5052
    s.bind(('192.168.100.50', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("Palindrome socket is listening")

    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        main_server.connect(('192.168.100.50', 5050))
        main_server.send(pickle.dumps("1"))
        print(pickle.loads(main_server.recv(1024)))
        main_server.send(c.recv(1024))
        check = pickle.loads(main_server.recv(1024))
        if(check == "1"):
            message="Enter Message\n"
            c.send(pickle.dumps(message))
            n=pickle.loads(c.recv(1024))
            message=palin(n)
            c.send(pickle.dumps(message))

if __name__ == "__main__":
    main()
