from flask import Flask, render_template
from config import Config
#
app = Flask(__name__)
app.config.from_object(Config)

import routes


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
