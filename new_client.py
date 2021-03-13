import asyncio

HOST = 'localhost'
PORT = 9876

class Client(asyncio.Protocol):
    def __init__(self, on_con_lost, user="User"):
        self.user = user
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        self.transport = transport
        print("Connection")

    def connection_lost(self, exc):
        print("Connection close")
        if not self.on_con_lost.done():
            self.on_con_lost.set_result(True)

    def data_received(self, data):
        if data:
            print(data.decode('utf-8'))

    async def client_loop(self):
        loop = asyncio.get_event_loop()
        while True:
            msg = await loop.run_in_executor(None, input) #Get stdout input forever
            if msg == "/exit":
                break
            self.transport.write(msg.encode('utf-8'))



async def main():
    loop = asyncio.get_event_loop()
    on_con_lost = loop.create_future()
    userClient = Client(on_con_lost)

    transport, protocol = await loop.create_connection(lambda: userClient, HOST, PORT)
    
    transport.write("Hello world".encode('utf-8'))
    
    try:
        await userClient.client_loop()
    finally:
        transport.close()
        




if __name__ == '__main__':
    asyncio.run(main())
    
