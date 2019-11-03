class Config(object):
    SECRET_KEY = 'yinzi-yinzi-yinzi'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/public'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True