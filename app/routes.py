#  coding: utf-8
#  Author: fengjianbo@wifipix.com
#  Creadted Time: 2021/1/6 19:03
from flask import render_template

from app import app


@app.route("/")
@app.route('/login')
def login():
    return render_template("register.html")

# def register():




if __name__ == '__main__':
    app.run()
