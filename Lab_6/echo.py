import socket
import pickle

def main():
    s = socket.socket()
    print("Socket successfully created")
    port = 5051
    s.bind(('192.168.100.50', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("Echo service is listening")

    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        message="Enter Message\n"
        c.send(pickle.dumps(message))
        c.send(c.recv(1024))


if __name__ == "__main__":
    main()
