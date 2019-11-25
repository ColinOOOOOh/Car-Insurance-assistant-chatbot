class Config(object):
    SECRET_KEY = 'yinzi-yinzi-yinzi'
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/public'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True