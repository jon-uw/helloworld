from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):
    def connectionMade(self):
        print 'Got connection from: ', self.transport.client

    def connectionLost(self):
        print self.transport.client, ' disconnected'

    def dataReceived(self, data):
        print "received: ", data

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(9606, factory)
reactor.run()

