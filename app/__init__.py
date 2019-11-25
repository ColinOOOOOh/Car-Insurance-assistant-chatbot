from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)





from app import routes




class role(db.Model):
    # 定义一个表名

    __tablename__ = 'role'
    # 定义一个主键  Column代表列
    roleid = db.Column(db.Integer,primary_key=True)
    # nullable允许为空吗?unique可以重复吗?
    rolename = db.Column(db.String(32),nullable=False,unique=False)
    # 方便查找  去这个类下找英雄relationship,这个列不是真实存在的,里面要加类名hero
    # backref 在关系的另一模型中添加反向引用



class user(db.Model):

    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(32), nullable=False, unique=False)
    email = db.Column(db.String(32), nullable=False, unique=False)
    birthday = db.Column(db.String(32), nullable=False, unique=False)
    gender = db.Column(db.String(32), nullable=False, unique=False)
    telephone = db.Column(db.String(32), nullable=False, unique=False)
    pwd = db.Column(db.String(32), nullable=False, unique=False)
    image = db.Column(db.String(120), nullable=False, unique=False)

    occupation = db.Column(db.String(120), nullable=False, unique=False)
    age = db.Column(db.String(120), nullable=False, unique=False)
    car_model = db.Column(db.String(120), nullable=False, unique=False)
    prev_accidents = db.Column(db.String(120), nullable=False, unique=False)


    # roleid = db.Column(db.Integer,db.ForeignKey('role.roleid'))

class company_user(db.Model):

    __tablename__ = 'company_user'

    company_userid =db.Column(db.Integer, primary_key=True)
    # userid = db.Column(db.Integer,nullable=False,unique=False)

    # companyid = db.Column(db.Integer,nullable=False,unique=False)

    companyid = db.Column(db.Integer,db.ForeignKey('company.companyid'))
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))

class company(db.Model):

    __tablename__ = 'company'
    companyid = db.Column(db.Integer,primary_key=True)
    companyname = db.Column(db.String(32),nullable=False,unique=False)
    tototalvalue = db.Column(db.Text(32), nullable=False, unique=False)


class insurance(db.Model):

    __tablename__ = 'insurance'
    insuranceid = db.Column(db.Integer,primary_key=True)
    insurancename = db.Column(db.String(32),nullable=False,unique=False)
    insdescription = db.Column(db.String(200), nullable=False, unique=False)



class company_insurance(db.Model):

    __tablename__ = 'company_insurance'
    company_insuranceid = db.Column(db.Integer,primary_key=True)
    companyid = db.Column(db.Integer,db.ForeignKey('company.companyid'))
    insuranceid = db.Column(db.Integer,db.ForeignKey('insurance.insuranceid'))


class business(db.Model):

    __tablename__ = 'business'
    businessid = db.Column(db.Integer,primary_key=True)
    businessname = db.Column(db.String(32),nullable=False,unique=False)
    busdescription = db.Column(db.String(200), nullable=False, unique=False)


class company_business(db.Model):

    __tablename__ = 'company_business'
    company_businessid = db.Column(db.Integer,primary_key=True)
    companyid = db.Column(db.Integer,db.ForeignKey('company.companyid'))
    businessid = db.Column(db.Integer,db.ForeignKey('business.businessid'))



class detail_insurance(db.Model):

    __tablename__ = 'detail_insurance'

    insuranceid = db.Column(db.Integer,primary_key=True)
    insurance = db.Column(db.Integer, nullable=False, unique=False)
    userid = db.Column(db.Integer, nullable=False, unique=False)

    name = db.Column(db.String(20), nullable=False, unique=False)

    coverage = db.Column(db.String(20), nullable=False, unique=False)
    duration = db.Column(db.String(20), nullable=False, unique=False)
    price = db.Column(db.String(200), nullable=False, unique=False)
    price_range = db.Column(db.String(200), nullable=False, unique=False)
    date = db.Column(db.String(40), nullable=False, unique=False)



class car_insurance(db.Model):
    __tablename__ = 'car_insurance'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=False)
    coverage = db.Column(db.String(20), nullable=False, unique=False)
    duration = db.Column(db.String(20), nullable=False, unique=False)
    price = db.Column(db.String(20), nullable=False, unique=False)
    price_range = db.Column(db.String(20), nullable=False, unique=False)


class claim(db.Model):
    __tablename__ = 'claim'
    id = db.Column(db.Integer,primary_key=True)
    insuranceid = db.Column(db.Integer, nullable=False, unique=False)
    userid = db.Column(db.Integer, nullable=False, unique=False)
    description = db.Column(db.String(120), nullable=False, unique=False)
    date = db.Column(db.String(40), nullable=False, unique=False)
    state = db.Column(db.String(30), nullable=False, unique=False)

class description(db.Model):
    __tablename__ = 'description'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=False)
    description = db.Column(db.String(200), nullable=False, unique=False)

db.create_all()