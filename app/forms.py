from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class HelpRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Elder Help', 'Elder Help'), ('Student Help', 'Student Help'),
        ('Errands', 'Errands'), ('Tutoring', 'Tutoring'),
        ('Companionship', 'Companionship'), ('Other', 'Other')
    ])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location')
    urgent = BooleanField('Urgent')
    submit = SubmitField('Post Request')
