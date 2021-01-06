#  coding: utf-8
#  Author: fengjianbo@wifipix.com
#  Creadted Time: 2021/1/6 17:54

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    passworde =PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remeber Me")
    submit = SubmitField("Sign in")
