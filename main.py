import os
import socket
import struct
import sys
import netifaces
import time
import json
import ServerSocket as SS
import HandleGPIO as GP

if __name__ == "__main__":
    print(sys.argv)
    print("starting at", SS.ServerIP, "on port", SS.ServerPort, "pid: ", os.getpid())
    connection = None
    sock = SS.startSocket()
    sock.listen(1)
    sockState = SS.possibleStates[0]
    frState = {"r": 0.0, "f": 0.0}
    GP.pinsSetup() # now redundant, but fine to keep
    try:
        while True:
            if sockState == SS.possibleStates[0]:
                try:
                    print('waiting for a connection at', SS.ServerIP, SS.ServerPort)
                    connection, address = sock.accept()
                    print("connected from", address)
                    sockState = SS.possibleStates[1]
                except:
                    connection.close()
                    break
            if sockState == SS.possibleStates[1]:
                received_message = connection.recv(1024)
            if received_message:
                sockState = SS.possibleStates[1]
                frState = SS.handleMessage(received_message, frState, sockState, connection, sock)
                # set GPIO Pins according to frState
    finally:
        print("cleaning up")
        GP.pinsCleanup()
