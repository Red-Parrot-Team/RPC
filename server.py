from twisted.internet import reactor, protocol, endpoints
from functions import *

class ServerProto(protocol.Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        peer = self.transport.getPeer()
        self.peerAddress = formatAddress(peer)
        
        joinMessage = "[{}] joined the chat".format(self.peerAddress) 
        print(joinMessage)
        self.sendAllWithoutThis(joinMessage.encode('utf-8'))
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        message = "[{}] left the chat".format(self.peerAddress) 
        print(message)
        self.sendAllWithoutThis(message.encode('utf-8'))
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        message = "[{}]: {}".format(self.peerAddress, data.decode('utf-8'))
        print(message)
        self.sendAllWithoutThis(message.encode('utf-8'))

    def sendAllWithoutThis(self, msg):
        for client in self.factory.clients:
            if not(client is self):
                client.transport.write(msg)

class PubFactory(protocol.ServerFactory):
    protocol = ServerProto
    def __init__(self):
        self.clients = set()


reactor.listenTCP(8000, PubFactory())
reactor.run()
