import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8080));
while True:
	s.send('test test test')
	print s.recv(1024)