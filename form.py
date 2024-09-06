
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, EmailField, SelectField,SubmitField
from wtforms.validators import DataRequired



class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
   
    email = EmailField('Email', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    date = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])

    address = StringField('Address', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired()])

 

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    