import asyncio

clients = []

class ChatProtocol(asyncio.Protocol):
    def __init__(self):
        self.connections = []

    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info('peername')
        print("Подключился:", self.peername)
        clients.append(self)

    def connection_lost(self, exc):
        print("Отключился:", self.peername)
        clients.remove(self)

    def data_received(self, data):
        print(self.peername, "отправил:", data.decode('utf-8'))
        for client in clients:
            if client is not self:
                client.transport.write(data )

if __name__ == "__main__":
    print("Запуск...")
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ChatProtocol, host='localhost', port=9876)
    server = loop.run_until_complete(coro)

    print("Сервер запущен")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        asyncio.run(server.wait_closed())
    loop.close()

