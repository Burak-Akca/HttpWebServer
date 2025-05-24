import socket
import threading
import json
import re
from routes import user_handler
from routes import hello_handler
from routes import static_handler
from utils import http_response
HOST = '0.0.0.0'
PORT = 8080

def log(msg):
    print(f"[LOG] {msg}")

def not_found_handler(method, path, headers, body):
    return http_response(404, "text/plain", "404 Not Found")

routes = [
    (re.compile(r"^/api/hello$"), hello_handler.hello_handler),
    (re.compile(r"^/user/(\d+)$"), user_handler.user_handler),
    (re.compile(r"^/static/.*$"), static_handler.static_handler),

]

def parse_request(request_text):
    lines = request_text.split("\r\n")
    method, path, version = lines[0].split()
    headers = {}
    body = ""
    i = 1
    while lines[i] != "":
        key, value = lines[i].split(":", 1)
        headers[key.strip()] = value.strip()
        i += 1
    i += 1
    if i < len(lines):
        body = "\r\n".join(lines[i:])
    return method, path, headers, body




def handle_client(conn, addr):
    try:
        request = conn.recv(4096).decode()
        if not request:
            return
        method, path, headers, body = parse_request(request)
        log(f"{addr} - {method} {path}")

        for pattern, handler in routes:
            match = pattern.match(path)
            if match:
                response = handler(method, path, headers, body, *match.groups())
                break
        else:
            response = not_found_handler(method, path, headers, body)

        # Log status code and message from response (if str)
        if isinstance(response, str):
            first_line = response.split("\r\n")[0]
            log(f"Response: {first_line}")

            conn.sendall(response.encode())
        else:
            log(f"Response: [binary data]")
            conn.sendall(response)

    except Exception as e:
        error_response = http_response(500, "text/plain", "Internal Server Error")
        conn.sendall(error_response.encode())
        log(f"[ERROR] {e}")
    finally:
        conn.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        log(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
     start_server()
