import socketserver
import http.server
import json

class SMRequestHandler(http.server.BaseHTTPRequestHandler):
    """Request handler for SM requests in JSON format."""
    def do_GET(self, request):
        response_data = request
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())

def run_server(self, port):
    """Runs the server on the specified port,
       delegating each client to a separate thread."""
    server_address = ('', port)
    httpd = socketserver.ThreadingTCPServer(server_address, SMRequestHandler)
    print(f"Server running on port {port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped")

if __name__ == "__main__":
    run_server(8080)
