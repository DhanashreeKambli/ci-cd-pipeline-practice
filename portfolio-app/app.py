from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

VERSION = "v1.1.1"

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>DevOps Portfolio</title>
    </head>
    <body>
        <h1>Welcome to Dhanashree's DevOps App 🚀</h1>

        <h2>Build & Release Engineer</h2>

        <p><b>Application Version:</b> {VERSION}</p>

        <p>Application deployed on AKS using Kubernetes.</p>

        <p><b>Hostname:</b> {socket.gethostname()}</p>

        <p><b>Current Time:</b> {datetime.now()}</p>

        <p><b>Status:</b> Running Successfully</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)