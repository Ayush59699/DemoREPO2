import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

# Load data
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)

name_to_marks = {entry["name"]: entry["marks"] for entry in data}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        names = query_params.get("name", [])

        marks = [name_to_marks.get(n, "Not Found") for n in names]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode("utf-8"))
