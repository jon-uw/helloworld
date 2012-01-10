import socket

s = socket.socket()
host =  socket.gethostname()
port = 9606
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5) # backlog 5

while True:
    c, addr = s.accept()
    print 'Got connection from: ' + addr[0]
    c.send('Thank you from connection\n')
    c.close()
