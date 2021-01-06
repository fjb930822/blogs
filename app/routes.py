#  coding: utf-8
#  Author: fengjianbo@wifipix.com
#  Creadted Time: 2021/1/6 19:03
from flask import render_template

from blogs import app


@app.route("/")
@app.route('/login')
def hello_world():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
