import asyncio

HOST = 'localhost'
PORT = 9876

class Client(asyncio.Protocol):
    def __init__(self, user="User"):
        self.user = user
        self.loop = asyncio.get_event_loop()

    def connection_made(self, transport):
        self.transport = transport

    def connection_lost(self, exc):
        print("Connection close")

    def data_received(self, data):
        if data:
            print(data.decode('utf-8'))

    async def client_loop(self):
        try:
            loop = asyncio.get_event_loop()
            while True:
                msg = await loop.run_in_executor(None, input) #Get stdout input forever
                self.transport.write(msg.encode('utf-8'))
        except KeyboardInterrupt:
            self.transport.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    userClient = Client()
    coro = loop.create_connection(lambda: userClient, HOST, PORT)
    server = loop.run_until_complete(coro)

    asyncio.run(userClient.client_loop())
    
    loop.run_forever()

    loop.close()
