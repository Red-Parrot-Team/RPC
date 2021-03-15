from twisted.internet import reactor, protocol, stdio
from twisted.protocols import basic
from os import linesep
from functions import *
import signal

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        signal.signal(signal.SIGINT, self.disconnect) # Регистрируем нажатие Ctrl+C
        stdio.StandardIO(IO(self))

    def dataReceived(self, data):
        print("{}".format(data.decode('utf-8')))


    def connectionLost(self, reason):
        print("Connection lost")

    def disconnect(self, signum, frame):
        """Обертка для нормального выхода по Ctrl+C"""
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost")
        reactor.stop()

class IO(basic.LineReceiver):
    delimiter = linesep.encode("utf-8")

    def __init__(self, connection):
        self.connection = connection
    
    def connectionMode(self):
        pass
    
    def lineReceived(self, line):
        self.connection.transport.write(line)

# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("192.168.0.103", 8000, f)

    reactor.run()


# this only runs if the module was *not* imported
if __name__ == "__main__":
    main()
