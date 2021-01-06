#  coding: utf-8
#  Author: fengjianbo@wifipix.com
#  Creadted Time: 2021/1/6 17:15


import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


DEBUG = True

DIALCT = 'mysql'
DRIVER = "mysqldb"
USERNAME = 'root'
PASSWORD = 'Mysql@930822'
HOST = '127.0.0.1'
PORT = '3306'
DBNAME = 'blogs'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True        #没有此配置会导致警告