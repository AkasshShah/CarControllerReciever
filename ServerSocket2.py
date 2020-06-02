import socket
import struct
import sys
import netifaces
import time

ServerIP = netifaces.ifaddresses('eth0')[2][0]['addr']
ServerPort = 42069
connection = None

possibleStates = [
    "connected", # 0
    "listening" # 1
]
state = possibleStates[1]
server_address = (ServerIP, ServerPort)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
def closeConnection():
    global state
    global connection
    global sock
    print("closing")
    connection.close()
    state = possibleStates[1]
    sock.close()

possibleMsgs = {
    b"quit": closeConnection
}

def handleMessage(msg):
    if msg in possibleMsgs.keys():
        print(msg)
        possibleMsgs[msg]()
    else:
        print(msg)

if __name__ == "__main__":
    print("starting at", ServerIP, "on port", ServerPort)
    # Listen for incoming connections
    sock.listen(1)
    connection = None
    n = 1
    connection = None
    while True:
        if state == possibleStates[1]:
            try:
                print('waiting for a connection at', ServerIP, ServerPort)
                connection, address = sock.accept()
                print("connected from", address)
                state = possibleStates[0]
            except:
                print("here")
                time.sleep(5)
        received_message = connection.recv(1024)
        if received_message:
            state = possibleStates[0]
            handleMessage(received_message)