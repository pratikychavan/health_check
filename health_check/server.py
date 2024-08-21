"""
Package for health check
"""
import json
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
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_content = json.dumps({"status": "OK"}).encode("utf-8")
        self.wfile.write(response_content)

def run() -> None:
    """
    Function to run the health check server
    """
    server_address = ('', 8000)
    httpd = socketserver.TCPServer(server_address, SimpleHTTPRequestHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
