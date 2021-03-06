import socket

HOST = ''
PORT = 9999

sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(2)
connection, address = sock.accept()

print('connected:', address)

while True:
    data = connection.recv(1024).decode('utf-8')
    if not data:
        break
    connection.send(data.upper().encode('utf-8'))

connection.close()

