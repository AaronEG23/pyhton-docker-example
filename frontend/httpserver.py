import http.server
import socketserver

PORT_HTTP_SERVER = 5001

def startHTTPServer():
	Handler = http.server.SimpleHTTPRequestHandler
	with socketserver.TCPServer(("", PORT_HTTP_SERVER), Handler) as httpd:
		httpd.serve_forever()

startHTTPServer()
