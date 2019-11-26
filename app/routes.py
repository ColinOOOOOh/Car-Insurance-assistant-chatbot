from app import app
from flask import render_template,request,session
from app.__init__ import user,db,insurance,detail_insurance,car_insurance,claim,description
import json
import time
import requests
import datetime


global userdeid
userdeid = -1

@app.route('/main')
def zhuye():

    return render_template('Main.html')
@app.route('/login',methods = ['GET','POST'])
def login():

    if request.method =="POST":


        username = request.form.get('User')
        passwd = request.form.get('password')
        print(username,passwd)
        a = user.query.filter(user.username == username, user.pwd == passwd).all()

        if a:
            global userdeid
            userdeid = a[0].userid
            session['userdeid']=userdeid
            question = 'uid '+str(userdeid)
            chat(question)
            return render_template('Main.html', userid=a[0].userid)
        else:
            return render_template('Login.html')
    if request.method =="GET":
        return render_template('Login.html')

@app.route('/register',methods = ['GET','POST'])
def regist():

    if request.method == "GET":
        return render_template('Register.html')
    if request.method == "POST":
        username = request.form.get("username")
        passwd = request.form.get("password")


        gender = request.values.get("gender")
        birthday = request.form.get("birthday")
        email = request.form.get("email")
        telephone = request.form.get("mobilenumber")

        occupation=request.form.get("occupation")
        age=request.form.get("age")
        car_model=request.form.get("car_model")
        prev_accidents=request.form.get("previous_accidents")

        cur_time = datetime.datetime.now().year
        if username==None or passwd==None or gender==None or birthday==None or email==None \
                or telephone==None or occupation ==None or occupation==age or car_model==None or prev_accidents==None:
            return render_template(('Register.html'))





        a = user.query.filter(user.username == username,user.email==email,user.gender==gender,
                              user.birthday==birthday,user.telephone==telephone).all()
        if len(a) == 0:
            me = user(username=username, email=email, birthday=birthday, gender=gender,
                      telephone=telephone, pwd=passwd, image = 'None',occupation=occupation,age=age,prev_accidents=prev_accidents,
                      car_model=car_model)
            db.session.add(me)
            db.session.commit()

            return render_template('Login.html')
        else:
            return render_template(('Register.html'))

@app.route('/username_exist',methods = ['GET'])
def username_exit():
    username = request.values.get('username')
    c = user.query.filter(user.username == username).all()

    if len(c)!=0:
        data = {
            'result': 'no',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'result': 'yes',
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/email_exit',methods = ['GET'])
def email_exit():
    email = request.values.get('email')
    if '@' in email:
        data = {
            'result': 'yes',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'result': 'no',
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/answer_question',methods = ['GET','POST'])
def answer_question():
    userid = session.get('userdeid')
    print('chat________________chat________________chat________________chat________________chat________________',userid)
    message = request.get_json()
    question = message['message']
    print(question)
    data = {
        'response':  chat(question)[0]
    }
    jstr = json.dumps(data)
    print(jstr)
    return jstr


def chat(message):

        print("Sending message now...")
        r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})
        responses = []
        print("Bot says, ")
        for i in r.json():
                bot_message = i['text']
                responses.append(bot_message)
                print(f"{i['text']}")
        if responses==[]:
            responses.append("Sorry, could you rephrase again?")
        return responses

@app.route('/edit_personal_info',methods = ['GET','POST'])
def edit_personal_info():
    global userdeid
    userid =session.get('userdeid')
    if request.method=="GET":
        return render_template("Profile.html")
    else:
        username = request.form.get("username")
        email = request.form.get('email')
        telephone = request.form.get('mobilenumber')
        gender = request.form.get('gender')
        birthday = request.form.get('birthday')
        user_info = user.query.filter(user.userid == userid).all()


        if len(user_info)!=0:
            user_info[0].email = email
            user_info[0].telephone = telephone
            user_info[0].gender = gender
            user_info[0].birthday = birthday
            user_info[0].username = username
            db.session.commit()

        a = user.query.filter(user.userid == userid,user.email==email, user.telephone == telephone, user.gender == gender,
                              user.birthday ==birthday).all()

        if len(a)!=0:
            data = {
                'msg': 'yes'
            }
            return render_template('Management.html')
        else:
            data = {
                'msg': 'no'
            }
            return render_template('Management.html')

@app.route('/check_telephone_number',methods = ['GET','POST'])
def check_telephone_number():
    telephone = request.values.get('mobile_number')
    if telephone.isdigit() and len(telephone)==10:
        if telephone[:2]=='04':
            data = {
                'result': 'yes'
            }
            jstr = json.dumps(data)
            return jstr
        else:
            data = {
                'result': 'no'
            }
            jstr = json.dumps(data)
            return jstr
    else:
        data = {
            'result': 'no'
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/add_insurance',methods = ['POST'])
def add_insurance():
    info = request.get_json()
    userid = info['userid']
    insurance_name = info['insurance_name']
    insurance_des = info['insurance_description']
    companyname = info['company']
    business_name = info['business_name']
    business_des = info['business_description']


    a = detail_insurance.query.filter(detail_insurance.insurancename==insurance_name,
                                      detail_insurance.insurance_description==insurance_des,
                                      detail_insurance.company==companyname,
                                      detail_insurance.business_description==business_des,
                                      detail_insurance.businessname==business_name).all()
    if len(a)!=0:
        data = {
            'result': 'no'
        }
        jstr = json.dumps(data)
        return jstr


    me = detail_insurance(userid=userid,insurancename=insurance_name, businessname=business_name,company=companyname
                   ,insurance_description=insurance_des,business_description=business_des,insurance=1)
    db.session.add(me)
    db.session.commit()

    data = {
        'result': 'yes'
    }
    jstr = json.dumps(data)
    return jstr

@app.route('/edit_insurance',methods = ['POST'])
def edit_insurance():
    info = request.get_json()
    insuranceid = info['insurance_id']
    insurance_name = info['insurance_name']
    insurance_des = info['insurance_description']
    companyname = info['company']
    business_name = info['business_name']
    business_des = info['business_description']

    a = detail_insurance.query.filter(detail_insurance.insuranceid==insuranceid).all()
    if len(a)!= 0:
        a[0].insurancename=insurance_name
        a[0].insurance_description = insurance_des
        a[0].company = companyname
        a[0].businessname = business_name
        a[0].business_description = business_des
        db.session.commit()

    check = detail_insurance.query.filter(detail_insurance.insuranceid==insuranceid,
                                          detail_insurance.insurancename == insurance_name,
                                          detail_insurance.insurance_description == insurance_des,
                                          detail_insurance.company == companyname,
                                          detail_insurance.businessname == business_name,
                                          detail_insurance.business_description == business_des,).all()

    if len(check)!=0:
        data = {
            'result': 'yes',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'result': 'no',
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/get_management_info',methods = ['GET','POST'])
def get_management_info():
    global userdeid
    userid = session.get('userdeid')
    if request.method=='GET':
        return render_template('Management.html')
    if request.method == 'POST':
        c = detail_insurance.query.filter(detail_insurance.userid==userid).all()
        result = []
        for i in c:
            data = {
                "serial_id":i.insuranceid,
                "insurance_id":i.insurance,
                "insurance_name" : i.name,
                "coverage" : i.coverage,
                "duration" : i.duration,
                "price" : i.price,
                "price_range" : i.price_range,
                "date":i.date
            }
            result.append(data)

        data = {
            "result":result
        }
        jstr = json.dumps(data)
        print(jstr)
        return jstr

@app.route('/remove_insurance_info',methods = ['DELETE'])
def delete_insurance():

    insuranceid_info = request.get_json()
    insuranceid = insuranceid_info['insurance_id']

    a_check = detail_insurance.query.filter(detail_insurance.insuranceid == insuranceid).all()
    if len(a_check)==0:
        data = {
            'result': 'no',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        a = detail_insurance.query.filter_by(insuranceid = insuranceid).first()
        db.session.delete(a)
        db.session.commit()


    ins_info = insurance.query.filter(insurance.insuranceid==insuranceid).all()
    if len(ins_info)!=0:
        data = {
            'result': 'no',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'result': 'yes',
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/chat_bot',methods = ['POST'])
def chat_bot():

    json = request.get_json()
    message = json['message']
    item = json['attribute']
    if message == 'query_insurance':
        msg = insurance_list()
    elif message =='query_insurance_with_price':
        msg = query_insurance_with_price(item)
    else:
        msg = query_insurance_with_name(item)
    return msg

def insurance_list():
    car_insurance_list = car_insurance.query.filter().all()
    print(len(car_insurance_list))
    result = []
    for i in car_insurance_list:
        data = {
            "id":i.id,
            "name":i.name,
            "coverage":i.coverage,
            "duration":i.duration,
            "price":i.price,
            "price_range":i.price_range
        }
        result.append(data)
    data = {
        "car_insurance": result
    }
    jstr = json.dumps(data)
    return jstr

def query_insurance_with_price(price):
    car_insurance_list = car_insurance.query.filter(car_insurance.price_range==price).all()
    result = []
    for i in car_insurance_list:
        data = {
            "id":i.id,
            "name":i.name,
            "coverage":i.coverage,
            "duration":i.duration,
            "price":i.price,
            "price_range":i.price_range
        }
        result.append(data)
    data = {
        "car_insurance": result
    }
    jstr = json.dumps(data)
    return jstr

def query_insurance_with_name(name):

    car_insurance_list = description.query.filter(description.name==name).all()
    result = []
    l = []
    for i in car_insurance_list:
        if i.description not in l:
            data = {
                "description":i.description
            }
            result.append(data)
            l.append(i.description)
            
    data = {
        "car_insurance": result
    }
    jstr = json.dumps(data)
    return jstr


@app.route('/get_price',methods = ['POST'])
def get_price():
    jsons = request.get_json()
    name = jsons['name']
    coverage = jsons['coverage']
    duration = jsons['duration']

    car_insurance_price = car_insurance.query.filter(car_insurance.name==name,car_insurance.coverage==coverage,
                                                     car_insurance.duration==duration).all()
    if len(car_insurance_price)!=0:
        data = {
            "price": car_insurance_price[0].price
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            "price": "none"
        }

        jstr = json.dumps(data)
        return jstr


@app.route('/buy_ins',methods = ['GET','POST'])
def buy_ins():
    global userdeid

    jsons = request.get_json()
    userid = jsons['uid']
    name = jsons['name']
    coverage = jsons['coverage']
    duration = jsons['duration']
    localtime = time.asctime(time.localtime(time.time()))

    c = car_insurance.query.filter(car_insurance.name == name,car_insurance.coverage==coverage,
                                   car_insurance.duration==duration).all()
    price = c[0].price
    price_range = c[0].price_range
    insurance = c[0].id
    me = detail_insurance(insurance=insurance,userid=userid,name=name, duration=duration,coverage=coverage
                   ,price=price,price_range=price_range,date = localtime)



    db.session.add(me)
    db.session.commit()

    d = detail_insurance.query.filter(detail_insurance.name == name,detail_insurance.coverage==coverage,
                                   detail_insurance.duration==duration,detail_insurance.price_range==price_range,
                                   detail_insurance.price==price,detail_insurance.userid==userid,
                                      detail_insurance.insurance==insurance).all()

    data = {
        "id": d[0].insuranceid
    }
    jstr = json.dumps(data)
    return jstr


@app.route('/sign_out',methods = ['POST','GET'])
def sign_out():
    global userdeid
    session.pop('userdeid',None)
    return render_template('Login.html')

#
@app.route('/order',methods = ['GET','POST'])
def order():
    global userdeid
    jsons = request.get_json()
    userid = jsons['uid']
    deteil_table_insuranceid = jsons['iid']
    description = jsons['description']

    localtime = time.asctime(time.localtime(time.time()))
    me = claim(insuranceid=deteil_table_insuranceid,description=description,userid = userid,date=localtime,
               state = 'Processing')

    db.session.add(me)
    db.session.commit()

    d = claim.query.filter(claim.insuranceid == deteil_table_insuranceid,claim.description==description).all()

    data = {
        "id": d[0].id
    }
    jstr = json.dumps(data)
    return jstr


@app.route('/insurance_m',methods = ['GET','POST'])
def insurance_m():
    global userdeid

    userid = session.get('userdeid')
    if request.method=='GET':
        return render_template('Insurance_management.html')
    if request.method == 'POST':
        c = claim.query.filter(claim.userid==userid).all()
        result = []
        for i in c:
            data = {
                "insuranceid":i.insuranceid,
                "description":i.description,
                "date" : i.date,
                "state" : i.state,
            }
            result.append(data)

        data = {
            "result":result
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/login_app',methods = ['GET','POST'])
def login_app():

    if request.method =="POST":

        msg = request.get_json()
        username = msg['username']
        passwd = msg['password']
        a = user.query.filter(user.username == username, user.pwd == passwd).all()

        if a:
            global userdeid
            userdeid = a[0].userid

            data = {
                'userid': a[0].userid
            }
            jstr = json.dumps(data)

            return jstr
        else:
            data = {
                'userid': '-1'
            }
            jstr = json.dumps(data)
            return jstr





@app.route('/check_des',methods = ['GET','POST'])
def check_des():
    msg = request.get_json()
    name = msg['name']
    a = description.query.filter(description.name == name).all()
    if len(a)!=0:
        descript = a[0].description
        data = {
            'description': descript
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'description': "Sorry, we don't have this kind of insurance."
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/profile',methods = ['POST'])
def profile():


    userid = session['userdeid']

    a = user.query.filter(user.userid == userid).all()
    if len(a)!=0:
        username = a[0].username
        email = a[0].email
        birthday = a[0].birthday
        gender =  a[0].gender
        telephone =  a[0].telephone
        data = {
            'username' : username,
            'email' : email,
            'birthday' : birthday,
            'gender': gender,
            'telephone' : telephone
        }
        jstr = json.dumps(data)

        return jstr
    else:
        data = {
            'username':'',
            'email':'',
            'birthday': '',
            'gender': '',
            'telephone': ''
        }
        jstr = json.dumps(data)
        return jstr