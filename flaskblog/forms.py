from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    #limitation b/w 2-20 character
    email =StringField('Email', validators=[DataRequired(),Email()])   #data is required also check the emails are valid
    password = PasswordField('Password',validators=[DataRequired()])   #password needs to validate
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email =StringField('Email', validators=[DataRequired(),Email()])   #check that email password are correct
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')