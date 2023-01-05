import http.server as serv
import socketserver
import argparse


class Handler(serv.SimpleHTTPRequestHandler):
    '''A simple handler that lives in the static/ directory'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="static/", **kwargs)


def handle_command_line_arguments():
    parser = argparse.ArgumentParser(description="Static HTTP server")
    parser.add_argument("--port", "-P", type=int, default=8000)
    return parser.parse_args()


def serve():
    args = handle_command_line_arguments()

    with socketserver.TCPServer(("", args.port), Handler) as server:
        print("serving on port %d..." % args.port)
        server.serve_forever()


if __name__ == "__main__":
    serve()
