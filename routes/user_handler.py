import json
from utils import http_response

def user_handler(method, path, headers, body, user_id):
    if method == "GET":
        response_body = json.dumps({"user_id": user_id, "name": "User " + user_id})
        return http_response(200, "application/json", response_body)
    elif method == "POST":
        try:
            data = json.loads(body)
            response_body = json.dumps({"received": data, "user_id": user_id})
            return http_response(200, "application/json", response_body)
        except:
            return http_response(400, "text/plain", "Bad Request")
    else:
        return http_response(405, "text/plain", "Method Not Allowed")
