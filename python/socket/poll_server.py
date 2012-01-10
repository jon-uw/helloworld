import socket, select

s = socket.socket()
s.bind(('', 9606))
s.listen(5)
print 'server started..'

# poll now
fdmap = {s.fileno(): s}
p = select.poll()
p.register(s)
print 'create poll instance'
while True:
    # print 'start to poll now..'
    events = p.poll();
    #print 'event length: ', len(events)
    for fd, event in events:
        if fdmap[fd] is s:
            c, addr = s.accept()
	    print 'Got connection from: ', addr
	    p.register(c)
	    fdmap[c.fileno()] = c
	elif event & select.POLLIN:
	    data = fdmap[fd].recv(1024)
	    if not data: # no data, connection closed
	        print fdmap[fd].getpeername(), ' disconnected'
		p.unregister(fd)
		del fdmap[fd]
	    else:
	        print data

