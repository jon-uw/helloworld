import socket

s = socket.socket()
s.connect(('localhost', 9606))

a = s.recv(1024)
print 'received: ' + str(a)

s.close()
