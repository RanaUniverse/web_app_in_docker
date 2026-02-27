"""
This is main.py file
"""

import datetime
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"""
    Thanks you
        <h1>Hello, Rana Universe!</h1>
        <p>Handled by PID: {os.getpid()}</p>

        <a href="/time">Click here to see current Indian time</a>
    """


@app.route("/time")
def shows_now_time():
    now_time_gmt = datetime.datetime.now(tz=datetime.timezone.utc)
    now_time_ind = now_time_gmt + datetime.timedelta(hours=5, minutes=30)
    return f"""
    <a href="/">Go To Main Page</a>
    <h1>Rana Universe</h1>
    <h2>Current Indian Time: {now_time_ind}</h2>
        <p>Handled by PID: {os.getpid()}</p>
    """


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
