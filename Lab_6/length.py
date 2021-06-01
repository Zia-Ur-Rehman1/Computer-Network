import socket
import pickle


def main():
    s = socket.socket()
    print("Socket successfully created")
    port = 5053
    s.bind(('192.168.100.50', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("Palindrome socket is listening")

    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        message = "Enter Message\n"
        c.send(pickle.dumps(message))
        n = pickle.loads(c.recv(1024))
        message = len(n)
        c.send(pickle.dumps(message))


if __name__ == "__main__":
    main()
