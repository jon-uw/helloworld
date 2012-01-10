from SocketServer import TCPServer, StreamRequestHandler

class SimpleHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
	print 'Got connection from: ' + addr[0]
	self.wfile.write('Server is constructed using SocketServer\n')

server = TCPServer(('', 9606), SimpleHandler)
server.allow_reuse_address = True
server.serve_forever()
