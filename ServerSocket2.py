import socket
import struct
import sys

possibleMsgs = {
    b"quit": closeConnection
}

def closeConnection():
    print("closing")
    connection.close()
    state = possibleStates[1]

def getIP():
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def handleMessage(msg):
    if msg in possibleMsgs.keys():
        print(msg)
        possibleMsgs[msg]()
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
        if not received_message:
            continue
        handleMessage(received_message)