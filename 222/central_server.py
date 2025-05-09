from http.server import BaseHTTPRequestHandler, HTTPServer
import json

articles_db = []

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/submit_article":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                article = json.loads(post_data.decode('utf-8'))
                articles_db.append(article)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode())
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Error: {e}".encode())

    def do_GET(self):
        if self.path == "/articles":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(articles_db, indent=2).encode())

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
