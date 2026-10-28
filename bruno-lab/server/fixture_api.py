#!/usr/bin/env python3
"""The Bruno lab's fixture API server.

A tiny, dependency-free HTTP API used by the Bruno for Mere
Mortals guide. It runs on loopback only and answers a handful
of invented endpoints for a fictional bookstore's stock room:

    GET  /health                 -> {"status": "ok"}
    GET  /books                  -> a JSON list of books
    GET  /books/2                -> one book as JSON
    POST /orders                 -> echoes the JSON it was sent
    GET  /whoami                 -> needs a bearer token
    GET  /echo                   -> reports query string and headers
    GET  /missing                -> 404, on purpose

Run it:  python3 fixture_api.py [port]     (default 18080)
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qsl

# The lab's invented token. It guards /whoami the way a real
# API key would, and it is worth exactly nothing anywhere else.
LAB_TOKEN = "lab-token-123"

BOOKS = [
    {"id": 1, "title": "The Left Hand of Darkness",
     "author": "Ursula K. Le Guin", "inStock": 4},
    {"id": 2, "title": "A Wizard of Earthsea",
     "author": "Ursula K. Le Guin", "inStock": 7},
    {"id": 3, "title": "The Dispossessed",
     "author": "Ursula K. Le Guin", "inStock": 0},
]


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):  # keep the lab quiet
        pass

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parts = urlparse(self.path)
        path = parts.path
        if path == "/health":
            self._send_json(200, {"status": "ok"})
        elif path == "/books":
            self._send_json(200, BOOKS)
        elif path.startswith("/books/"):
            try:
                book_id = int(path.rsplit("/", 1)[1])
            except ValueError:
                book_id = None
            book = next((b for b in BOOKS if b["id"] == book_id), None)
            if book is None:
                self._send_json(404, {"error": "no such book"})
            else:
                self._send_json(200, book)
        elif path == "/whoami":
            auth = self.headers.get("Authorization", "")
            if auth == "Bearer " + LAB_TOKEN:
                self._send_json(200, {"user": "stockroom",
                                      "role": "inventory"})
            else:
                self._send_json(401, {"error": "missing or bad token"})
        elif path == "/echo":
            self._send_json(200, {
                "query": dict(parse_qsl(parts.query)),
                "headers": {
                    "User-Agent": self.headers.get("User-Agent"),
                    "X-Lab-Marker": self.headers.get("X-Lab-Marker"),
                },
            })
        else:
            self._send_json(404, {"error": "no such endpoint"})

    def do_POST(self):
        parts = urlparse(self.path)
        if parts.path != "/orders":
            self._send_json(404, {"error": "no such endpoint"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        try:
            received = json.loads(raw.decode() or "{}")
        except (ValueError, UnicodeDecodeError):
            self._send_json(400, {"error": "body was not JSON"})
            return
        self._send_json(201, {
            "orderId": 42,
            "received": received,
            "contentType": self.headers.get("Content-Type"),
        })


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 18080
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"fixture api listening on http://127.0.0.1:{port}",
          flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
