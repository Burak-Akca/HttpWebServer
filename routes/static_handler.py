import os
import mimetypes
from utils import http_response
def static_handler(method, path, headers, body):
    if method != "GET":
        return http_response(405, "text/plain", "Method Not Allowed")

    filepath = path.lstrip('/')
    if os.path.exists(filepath) and os.path.isfile(filepath):
        with open(filepath, 'rb') as f:
            content = f.read()
        content_type = mimetypes.guess_type(filepath)[0] or 'application/octet-stream'
        header = (
            f"HTTP/1.1 200 OK\r\n"
            f"Content-Type: {content_type}\r\n"
            f"Content-Length: {len(content)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode()
        return header + content
    else:
        return http_response(404, "text/plain", "404 Not Found")
