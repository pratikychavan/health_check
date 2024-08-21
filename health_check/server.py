"""
Package for health check
"""
import http.server
import socketserver

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Request handler for health check
    """
    def do_GET(self) -> None:
        """
        predefined method to execute on GET requests
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response_content = "<html><body><h1>Hello, World!</h1></body></html>"
        self.wfile.write(response_content.encode('utf-8'))

def run() -> None:
    """
    Function to run the health check server
    """
    server_address = ('', 8000)
    httpd = socketserver.TCPServer(server_address, SimpleHTTPRequestHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
