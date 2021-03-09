from multiprocessing import Process
import socket

class Server:
    def __init__(self, HOST='localhost', PORT=9876):
        self.HOST = HOST
        self.PORT = PORT
        self.socket = socket.socket()
        self.socket.bind((HOST, PORT))
        self.socket.listen(2)
        self.clients = []      # Список подключенных клиентов

    def loop(self):
        """Добавление новых пользователей"""
        while True:
            connect, addr = self.socket.accept()

            print('connected:', addr)

            if addr not in self.clients:
                self.clients.append(addr)

            Process(target=self.newConnect, args=(connect, addr), daemon=True) \
                .start()

    def newConnect(self, connect, addr):
        """Обрабокта каждого пользователя"""
        while True:
            data = connect.recv(1024).decode('utf-8')
            if not data:
                print('disconnect:', addr)
                break
            for client in self.clients:
                print(client)
                #...Рассыла сообщений всем пользователям
            connect.send(data.upper().encode('utf-8'))
        connect.close()

if __name__ == '__main__':
    Server().loop()
