# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    # Username field with DataRequired validator
    username = StringField('Username', validators=[DataRequired()])

    # Password field with DataRequired validator
    password = PasswordField('Password', validators=[DataRequired()])

    # Submit button for the login form
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    # Username field with DataRequired and Length validators
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])

    # Email field with DataRequired and Email validators
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Password field with DataRequired and Length validators
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

    # Confirm password field with DataRequired and EqualTo validators
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    # Submit button for the registration form
    submit = SubmitField('Register')
