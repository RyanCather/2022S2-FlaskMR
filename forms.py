from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from models import User

class ContactForm (FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    message = StringField("message", validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    email_address = StringField("Email Address (Username)", validators=[DataRequired(), Email()])
    name = StringField("Full Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_email_address(self, email_address_to_register):
        user = User.query.filter_by(email_address=email_address_to_register.data).first()
        if user is not None:
            raise ValidationError("Please Use a Different Email Address)")

class LoginForm(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class ResetPasswordForm(FlaskForm):
    new_password = StringField('New Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserProfileForm(FlaskForm):
    email_address = StringField("Email Address (Username)", validators=[DataRequired(), Email()])
    name = StringField("Full Name", validators=[DataRequired()])
    submit = SubmitField("Update Profile")


