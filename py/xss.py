from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class ReflectiveXSSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        
        user_input = query.get('input', [''])[0]
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write((
            f"<html><body>"
            f"<h1>Welcome!</h1>"
            f"<p>You said: {user_input}</p>"
            f"</body></html>"
        ).encode('utf-8'))

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, ReflectiveXSSHandler)
    print("Starting server on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()