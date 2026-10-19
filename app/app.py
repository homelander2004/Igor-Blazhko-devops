import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from html import escape

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        name = escape(os.getenv("STUDENT_NAME", "Not set"))
        surname = escape(os.getenv("STUDENT_SURNAME", "Not set"))
        group = escape(os.getenv("STUDENT_GROUP", "Not set"))
        student_id = escape(os.getenv("STUDENT_ID", "Not set"))

        html = f"""
        <html>
        <head><title>DevOps Student Project</title></head>
        <body>
            <h1>DevOps Laboratory Work</h1>
            <p>Name: {name}</p>
            <p>Surname: {surname}</p>
            <p>Group: {group}</p>
            <p>Student ID: {student_id}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
