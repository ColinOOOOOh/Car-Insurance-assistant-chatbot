from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,RadioField

from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    # image = RadioField('image',validators=[DataRequired(message='please input image')])
    app = StringField('app',validators=[DataRequired(message='please input app name')])
    command = StringField('command')
    env = StringField('environment')
    port = StringField('port',validators=[DataRequired(message='please input port')])
    targetport = StringField('target port',validators=[DataRequired(message='please input target port')])
    path = StringField('volumemount path')

    submit = SubmitField('Create')


class replicationcontrollerForm(FlaskForm):
    
    metadataname = StringField('metadataname',validators=[DataRequired(message='please input name')])
    app = StringField('app(labels)',validators=[DataRequired(message='please input app name')])
    spectype = StringField('type', validators=[DataRequired(message='please input command')])
    port = StringField('port', validators=[DataRequired(message='please input port')])
    targetport = StringField('target port',validators=[DataRequired(message='please input target port')])
    nodeport = StringField('node port',validators=[DataRequired(message='please input node port')])
    submit = SubmitField('Create')

class configmapForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(message='please input configmap name')])
    configname = StringField('configname',validators=[DataRequired(message='please input configname')])
    configtxt = TextAreaField('configtxt',validators=[DataRequired(message='please input content')])
    submit = SubmitField('Create')


class configmap_edit_Form(FlaskForm):

    # cm_inf=TextAreaField('cm_inf',validators=[DataRequired(message='please input content')])
    submit = SubmitField('Save')

