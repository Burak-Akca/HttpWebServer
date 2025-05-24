import json
from utils import http_response  

def hello_handler(method, path, headers, body):
    if method == "GET":
        response_body = json.dumps({"message": "Hello World!"})
        return http_response(200, "application/json", response_body)
    return http_response(405, "text/plain", "Method Not Allowed")
