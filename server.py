import http.server as serv
import socketserver
import os

class Handler(serv.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='static/', **kwargs)

socketserver.TCPServer.allow_reuse_address = True
os.chdir('static/')

with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("serving...")
    httpd.serve_forever()
