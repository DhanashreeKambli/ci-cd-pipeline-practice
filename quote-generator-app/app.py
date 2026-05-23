from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself!",
    "DevOps is fun 🚀",
    "Consistency beats motivation.",
    "Small steps every day.",
    "Dream big and work hard."
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)