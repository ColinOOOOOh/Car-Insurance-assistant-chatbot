from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,RadioField

from wtforms.validators import DataRequired


# 创建deployment和svc表单
class registerForm(FlaskForm):

    submit = SubmitField()

class loginform(FlaskForm):
    username = StringField('User')
    passwd = StringField('password')
    # env = StringField('environment')
    # port = StringField('port',validators=[DataRequired(message='please input port')])
    # targetport = StringField('target port',validators=[DataRequired(message='please input target port')])
    # path = StringField('volumemount path')

    submit = SubmitField('Login')