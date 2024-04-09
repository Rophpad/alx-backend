#!/usr/bin/env python3
"""Setup Flask app"""

from flask import Flask, render_template

app = Flask(__name__)
port = 5000


@app.route('/')
def index():
    """Render index.html"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
