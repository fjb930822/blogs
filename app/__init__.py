#  coding: utf-8
#  Author: fengjianbo@wifipix.com
#  Creadted Time: 2021/1/6 18:28

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# app.register_blueprint()

from app import routes