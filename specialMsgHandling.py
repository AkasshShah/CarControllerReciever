import socket
import struct
import sys

def closeConnection():
    print("closing")
    connection.close()
    state = possibleStates[1]