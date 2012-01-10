from SocketServer import TCPServer, StreamRequestHandler
from SocketServer import ForkingMixIn, ThreadingMixIn

class ForkServer(ForkingMixIn, TCPServer): pass
class ThreadServer(ThreadingMixIn, TCPServer): pass

class SimpleHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
	print 'Got connection from: ' + addr[0]
	self.wfile.write('Server is constructed using SocketServer\n')

server = ForkServer(('', 9606), SimpleHandler)
server.allow_reuse_address = True
server.serve_forever()
