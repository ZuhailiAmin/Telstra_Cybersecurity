from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def block_request(self):
        self.send_response(403)  # Forbidden
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Access to /tomcatwar.jsp is forbidden.", "utf-8"))

    def handle_request(self):
        if self.path == "/tomcatwar.jsp":
            self.block_request()
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()

if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
