from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

# Database setup
connection = sqlite3.connect("datastore.db")

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM users").fetchall()
        data = json.dumps(rows)
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        # Incoming data will look like this:
        # {
        #   "name": "xxxxx",
        #   "surname": "xxxxx"
        # }
        data = json.loads(post_data)  # serialisation
        name = data.get("name")
        surname = data.get("surname")

        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO users (name, surname) VALUES ('{name}', '{surname}')"
        )
        connection.commit()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        results = {"id": cursor.lastrowid}
        self.wfile.write(bytes(json.dumps(results), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
