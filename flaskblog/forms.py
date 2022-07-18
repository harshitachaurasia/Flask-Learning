from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    #limitation b/w 2-20 character
    email =StringField('Email', validators=[DataRequired(),Email()])   #data is required also check the emails are valid
    password = PasswordField('Password',validators=[DataRequired()])   #password needs to validate
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken. Please choose another one')

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is taken. Please choose another one')
    
    


class LoginForm(FlaskForm):
    email =StringField('Email', validators=[DataRequired(),Email()])   #check that email password are correct
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')