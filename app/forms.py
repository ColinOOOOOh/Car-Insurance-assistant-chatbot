from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,RadioField

from wtforms.validators import DataRequired


class registerForm(FlaskForm):

    submit = SubmitField()

class loginform(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    submit = SubmitField('Submit')