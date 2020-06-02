import socket
import struct
import sys

def closeConnection(connection):
    print("closing")
    connection.close()
    state = possibleStates[1]