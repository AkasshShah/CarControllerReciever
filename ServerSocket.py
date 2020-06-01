import socket
import sys

ServerIP = 'localhost'
ServerPort = 42069

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (ServerIP, ServerPort)
print("starting at", ServerIP, "on port", ServerPort)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
connection = None
n = 1
while True:
    if connection is None or connection.fileno() == -1:
        print(sys.stderr, 'waiting for a connection')
        connection, address = sock.accept()
        print("connected from", address)
    received_message = connection.recv(1024)
    if not received_message:
        continue
    print(received_message)
    # message handling
    if received_message == b"quit":
        print("closing")
        connection.close()
    