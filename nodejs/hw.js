// from nodejs.org as a helloworld example

var http = require('http');
http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('Hello, NodeJs\n');
}).listen(9600, 'localhost')

console.log("Server running at http://localhost:9600")
