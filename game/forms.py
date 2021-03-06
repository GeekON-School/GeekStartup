# -*- coding: utf8 -*-
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, InputRequired, Regexp, Optional


class LoginForm(Form):
    login = StringField('login', validators=[InputRequired(), Length(min=4, max=80, message="Too short"),
                                             Regexp(r"[0-9a-zA-Z_]+", message="Wrong characters")])
    password = StringField('password', validators=[InputRequired(), Length(min=6, message="Too short")])


class RegistrationForm(Form):
    login = StringField('login', validators=[InputRequired(), Length(min=4, max=80, message="Too short"),
                                             Regexp(r"[0-9a-zA-Z_]+", message="Wrong characters")])
    password = StringField('password', validators=[InputRequired(), Length(min=6, message="Too short")])


class GameForm(Form):
    code = StringField('code', validators=[InputRequired(), Length(min=4, max=10)])
    rounds = IntegerField('rounds', validators=[Optional()], default=10)


class TransactionForm(Form):
    part = IntegerField('part', validators=[InputRequired()])
    amount = IntegerField('amount', validators=[InputRequired()])
    receiver = IntegerField('receiver', validators=[InputRequired()])


class LoginByCodeForm(Form):
    code = StringField('code', validators=[InputRequired(), Length(min=6, max=80, message="Too short"),
                                             Regexp(r"[0-9a-zA-Z_]+", message="Wrong characters")])
