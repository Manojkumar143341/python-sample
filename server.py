import http.server
import socketserver

PORT = 8000

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
