import socket

HOST = ''
PORT = 9999

sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(1)
connection, address = sock.accept()

print('connected:', address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.send(data.upper())

connection.close()

