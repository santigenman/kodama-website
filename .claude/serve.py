import functools
import http.server
import socketserver

ROOT = "/Users/santigenman/Desktop/Claude Kodama Landing Page"
PORT = 3456

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    httpd.serve_forever()
