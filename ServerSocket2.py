import socket
import struct
import sys
import netifaces
import time
import json

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
forward = 0.0
right = 0.0
def closeConnection():
    global state
    global connection
    global sock
    print("closing")
    connection.close()
    state = possibleStates[1]
    sock.close()

def toggleHeadlight():
    pass

possibleMsgs = {
    "quit": closeConnection,
    "headlight": toggleHeadlight
}

def handleMessage(recvdMsg):
    msg = recvdMsg.decode('ascii')
    print(msg)
    if msg in possibleMsgs.keys():
        possibleMsgs[msg]()
    else:
        try:
            decoded = json.loads(msg)
            forward = decoded['f']
            right = decoded['r']
            print("f =", forward, "\tright =", right)
        except:
            print("too much data")

if __name__ == "__main__":
    print("starting at", ServerIP, "on port", ServerPort)
    connection = None
    connection = None
    while True:
        sock.listen(1)
        while True:
            if state == possibleStates[1]:
                try:
                    print('waiting for a connection at', ServerIP, ServerPort)
                    connection, address = sock.accept()
                    print("connected from", address)
                    state = possibleStates[0]
                except:
                    print("here")
                    connection.close()
                    break
            if state == possibleStates[0]:
                received_message = connection.recv(1024)
            if received_message:
                state = possibleStates[0]
                handleMessage(received_message)