import socket, select

s = socket.socket()
s.bind(('', 9606))
s.listen(10)

#select now
inputs = [s]
print(type(inputs))
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
	    c, addr = s.accept()
	    print 'Got connection from', addr
	    inputs.append(c)
	else:
	    try:
	        data = r.recv(1024)
		r.send('Msg received!\n')
		disconnected = not data
	    except socket.error:
	        disconnected = True
	    
	    if disconnected:
	        print r.getpeername(),  ' disconnected'
		inputs.remove(r)
	    else:
	        print data
