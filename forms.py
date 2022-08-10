from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField, SubmitField, IntegerField

class ContactForm (FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    message = StringField("message", validators=[DataRequired()])
    submit = SubmitField('dateSubmitted')