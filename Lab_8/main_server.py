import socket
from commonthread import commonThread


def main():
    s = socket.socket()
    print("Socket successfully created")
    port = 5050
    s.bind(('192.168.100.50', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("socket is listening")
    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        clientthread = commonThread(c)
        clientthread.start()


if __name__ == "__main__":
    main()
