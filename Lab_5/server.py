import socket
from common_thread import commonThread


address = "192.168.100.50"

port = 5050
def main():


    s = socket.socket()
    s.bind((address,port))

    s.listen(5)
    print("Listing for clients ...")
    while True:
        c , addr = s.accept()
        print("Client Connected :  "  , addr)
        clientThread = commonThread(c)
        clientThread.start()

if __name__ == "__main__":
    main()