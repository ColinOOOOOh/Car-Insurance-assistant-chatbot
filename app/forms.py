from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,RadioField

from wtforms.validators import DataRequired


# 创建deployment和svc表单
class LoginForm(FlaskForm):
    app = StringField('app',validators=[DataRequired(message='please input app name')])
    command = StringField('command')
    env = StringField('environment')
    port = StringField('port',validators=[DataRequired(message='please input port')])
    targetport = StringField('target port',validators=[DataRequired(message='please input target port')])
    path = StringField('volumemount path')

    submit = SubmitField('Create')

# 创建cm表单
class configmapForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(message='please input configmap name')])
    configname = StringField('configname',validators=[DataRequired(message='please input configname')])
    configtxt = TextAreaField('configtxt',validators=[DataRequired(message='please input content')])
    submit = SubmitField('Create')

# 修改cm表单
class configmap_edit_Form(FlaskForm):
    # cm_inf=TextAreaField('cm_inf',validators=[DataRequired(message='please input content')])
    submit = SubmitField('Save')


