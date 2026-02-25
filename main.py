"""
This is main.py file
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>This is My Website</h1>"


import sys
print("Python Version is,", sys.version)
print("Executable Location is,", sys.executable)


if __name__ == "__main__":
    # this block will executes when i run the main.py directly
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
