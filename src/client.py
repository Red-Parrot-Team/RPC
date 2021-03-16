from twisted.internet import reactor, protocol, stdio
from twisted.protocols import basic
from os import linesep
from functions import *
import signal
import click

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

@click.command()
@click.option('-h', '--host', prompt='Enter server host')
@click.option('-p', '--port', prompt='Enter server port', type=int)
def main(host, port):
    f = EchoFactory()
    reactor.connectTCP(host, port, f)

    reactor.run()


if __name__ == "__main__":
    main()
