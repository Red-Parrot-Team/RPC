from twisted.internet import reactor, protocol, stdio
from twisted.protocols import basic
from twisted.application import internet
from os import linesep
import signal
import click
from User import User
from functions import *
from State import *

class EchoClient(protocol.Protocol):
    def __init__(self):
        self.user = User(None)

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
    stateObj = State()

    def __init__(self, connection):
        self.connection = connection
    
    def connectionMade(self):
        self.transport.write(b"Enter your nickname-> ")
        self.stateObj.confirm_type = ConfirmType.NOTCONFIRM # Пользователь не подтвердил никнейм
    
    def lineReceived(self, line):

        if not line: return

        line_dec = line.decode('utf-8')


        if not self.connection.user.isRegistrated():
            self.confirmHandler(line_dec)
        else:
            self.connection.transport.write(line)

    def confirmHandler(self, line):
        if self.stateObj.isNotConfirm():
            self.transport.write(b"Confirm your nickname (y/n): ")
            self.stateObj.confirm_type = ConfirmType.CONFIRMING
        elif self.stateObj.isConfirming():
            if line.lower() == 'y':
                self.connection.user.nickname = line
                
                self.stateObj.confirm_type = ConfirmType.CONFIRM
            elif line.lower() == 'n':
                self.transport.write(b"Enter your nickname-> ")
                self.stateObj.confirm_type = ConfirmType.NOTCONFIRM
            else:
                self.stateObj.confirm_type = ConfirmType.NOTCONFIRM
            

@click.command()
@click.option('-h', '--host', prompt='Enter server host')
@click.option('-p', '--port', prompt='Enter server port', type=int)
def main(host, port):
    f = EchoFactory()
    reactor.connectTCP(host, port, f)

    reactor.run()


if __name__ == "__main__":
    main()
