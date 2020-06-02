import socket
import struct
import sys
import netifaces

possibleMsgs = {
    b"quit": closeConnection
}

def closeConnection():
    print("closing")
    connection.close()
    state = possibleStates[1]

def getIP():
    return(netifaces.ifaddresses('eth0')[2][0]['addr'])

def handleMessage(msg):
    if msg in possibleMsgs.keys():
        print(msg)
        possibleMsgs[msg](connection)
    else:
        print(msg)

ServerIP = getIP()
ServerPort = 42069
connection = None

possibleStates = [
    "connected", # 0
    "listening" # 1
]
state = possibleStates[1]

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ServerIP, ServerPort)
    sock.bind(server_address)
    print("starting at", ServerIP, "on port", ServerPort)
    # Listen for incoming connections
    sock.listen(1)
    connection = None
    n = 1
    connection = None
    while True:
        if state == possibleStates[1]:
            print('waiting for a connection at', ServerIP, ServerPort)
            connection, address = sock.accept()
            print("connected from", address)
            state = possibleStates[0]
        received_message = connection.recv(1024)
        if received_message:
            handleMessage(received_message)