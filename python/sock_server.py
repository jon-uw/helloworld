import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9610))
s.listen(50)
conn, addr = s.accept()
print 'connected by: ', addr

while 1:
    data = conn.recv(1024)
    if not data: break
    print data
conn.close()
