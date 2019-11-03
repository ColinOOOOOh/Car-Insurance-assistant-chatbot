from app import app
from flask import render_template,request
from app.__init__ import user,db,insurance,business,company,company_business,company_insurance,company_user,detail_insurance
import json
from app.forms import registerForm,loginform





@app.route('/')
def zhuye():

    return render_template('Main.html')
@app.route('/login',methods = ['GET','POST'])
def login():

    username = request.form.get('User')
    passwd = request.form.get('password')

    print(username,passwd)
    a= user.query.filter(user.username==username,user.pwd==passwd).first()
    if a:
        print('yes')
        return render_template('Main.html')
    else:
        print('no')
        return render_template('Login.html')

@app.route('/register',methods = ['GET','POST'])
def regist():
    form = registerForm()
    if form.validate_on_submit():
        username = request.values.get("username")
        passwd = request.values.get("pwd")
        userid = request.values.get("userid")

        roleid = request.values.get("roleid")

        gender = request.values.get("gender")

        birthday = request.values.get("birthday")
        email = request.values.get("email")
        telephone = request.values.get("telephone")
        image = request.values.get('image')

        # 先查询。在插入或删除或更新
        a = user.query.filter(user.userid == userid,user.username==username).all()
        if len(a)==0:
            me = user(userid = userid,username = username,email = email,birthday = birthday,gender = gender,
                  telephone = telephone,pwd = passwd,image=image,roleid=roleid)
            db.session.add(me)
            db.session.commit()

            return render_template('Login.html')
        else:
            #返回注册界面说明 用户名和userid 已存在
            return render_template('Register.html')

    else:
        return render_template('Register.html')


@app.route('/username_exit',methods = ['GET','POST'])
def username_exit():
    username = request.values.get('username')
    print(username)
    a = user.query.filter(user.username == username).all()
    print('changdu',len(a))
    if len(a)!=0:
        data = {
            'msg': 'yes',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'msg': 'no',
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/email_exit',methods = ['GET','POST'])
def email_exit():
    email = request.values.get('email')
    a = user.query.filter(user.email == email).all()
    if len(a)!=0:
        data = {
            'msg': 'yes',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'msg': 'no',
        }
        jstr = json.dumps(data)
        return jstr


@app.route('/mobilenumber_exit',methods = ['GET','POST'])
def mobilenumber_exit():
    telephone = request.values.get('mobile_number')
    a = user.query.filter(user.telephone == telephone).all()
    if len(a)!=0:
        data = {
            'msg': 'yes',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'msg': 'no',
        }
        jstr = json.dumps(data)
        return jstr


@app.route('/answer_question',methods = ['GET','POST'])
def answer_question():
    question = request.values.get('question')
    # 调用 ouzhu 算法
    data = {
        'msg': question
    }
    jstr = json.dumps(data)
    return jstr


@app.route('/remove_insurance_info',methods = ['GET','POST'])
def remove_insurance_info():
    insuranceid = request.values.get('insuranceid')

    a = insurance.query.filter(insurance.insuranceid == insuranceid).all()
    if len(a)==0:
        # 数据库本就不存在这个id的数据
        data = {
            'msg': 'no data found'
        }
        jstr = json.dumps(data)

        return jstr
    else:
        ins_info = insurance.query.filter_by(insuranceid = insuranceid).first()
        db.session.delete(ins_info)
        db.session.commit()
        # check again
        aa = insurance.query.filter(insurance.insuranceid == insuranceid).all()
        if len(aa)==0:
            data = {
                'msg': 'yes'
            }
            jstr = json.dumps(data)
            return jstr
        else:
            data = {
                'msg': 'no'
            }
            jstr = json.dumps(data)
            return jstr



@app.route('/edit_personal_info',methods = ['GET','POST'])
def edit_personal_info():
    userid = request.values.get('userid')
    email = request.values.get('email')
    telephone = request.values.get('mobile_number')
    gender = request.values.get('gender')
    birthday = request.values.get('birthday')
    image = request.values.get('image')
    user_info = user.query.filter(user.userid == userid).all()


    if len(user_info)!=0:
        user_info[0].email = email
        user_info[0].telephone = telephone
        user_info[0].gender = gender
        user_info[0].birthday = birthday
        user_info[0].image = image
        db.session.commit()

    # check 是否更新成功
    a = user.query.filter(user.userid == userid,user.email==email, user.telephone == telephone, user.gender == gender,
                          user.birthday ==birthday,user.image==image).all()

    if len(a)!=0:
        data = {
            'msg': 'yes'
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'msg': 'no'
        }
        jstr = json.dumps(data)
        return jstr


@app.route('/check_telephone_number',methods = ['GET','POST'])
def check_telephone():
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

@app.route('/add_insurance',methods = ['GET'])
def add_insurance():
    # insurance_name = request.values.get('insurance_name')
    # insurance_des = request.values.get('insurance_description')
    # a = insurance.query.filter(insurance.insurancename==insurance_name,insurance.insdescription==insurance_des).all()
    # if len(a)!=0:
    #     data = {
    #         'result': 'no'
    #     }
    #     jstr = json.dumps(data)
    #     return jstr
    #
    # me = insurance(insdescription=insurance_des, insurancename=insurance_name)
    # db.session.add(me)
    # db.session.commit()
    # a = insurance.query.filter(insurance.insurancename == insurance_name,
    #                            insurance.insdescription == insurance_des).all()
    # print('---------------',a[0].insuranceid)
    #
    # # 先插到insurance表得到insurance id
    #
    # companyname = request.values.get('company')
    #
    # business_name = request.values.get('business_name')
    # business_des = request.values.get('business_description')
    #
    # be = business(busdescription=business_des, businessname=business_name)
    # db.session.add(be)
    # db.session.commit()
    #
    # b = business.query.filter(business.businessname == business_name,
    #                            business.busdescription == business_des).all()
    # print('---------------',b[0].businessid)
    #
    # #再插到business 表，得到business id
    #
    # c= company.query.filter(company.companyname == companyname).all()
    # print(c[0].companyid)
    #
    # c_b = company_business(companyid =c[0].companyid,businessid =b[0].businessid)
    # db.session.add(c_b)
    # db.session.commit()
    #
    # c_i = company_insurance(companyid =c[0].companyid,insuranceid =a[0].insuranceid)
    # db.session.add(c_i)
    # db.session.commit()
    #
    # data = {
    #     'result': 'yes',
    #     'insuranceid':a[0].insuranceid
    # }
    # jstr = json.dumps(data)
    # return jstr
    insurance_name = request.values.get('insurance_name')
    insurance_des = request.values.get('insurance_description')
    companyname = request.values.get('company')
    business_name = request.values.get('business_name')
    business_des = request.values.get('business_description')

    me = detail_insurance(insurancename=insurance_name, businessname=business_name,company=companyname
                   ,insurance_description=insurance_des,business_description=business_des)
    db.session.add(me)
    db.session.commit()
    c = detail_insurance.query.filter(detail_insurance.insurancename == insurance_name,
                                      detail_insurance.businessname == business_name,
                                      detail_insurance.company == companyname,
                                      detail_insurance.insurance_description == insurance_des,
                                      detail_insurance.business_description == business_des).all()
    if len(c)!=0:
        data = {
            'result': 'yes',
            'insuranceid':c[0].insuranceid
        }
        jstr = json.dumps(data)
        return jstr
    else:
        data = {
            'result': 'no'
        }
        jstr = json.dumps(data)
        return jstr

@app.route('/delete_insurance',methods = ['GET'])
def delete_insurance():
    insuranceid = request.values.get('insurance_id')
    a_check = insurance.query.filter(insurance.insuranceid == insuranceid).all()
    if len(a_check)==0:
        data = {
            'result': 'no',
        }
        jstr = json.dumps(data)
        return jstr
    else:
        # 先删外键关联的记录
        company_ins = company_insurance.query.filter_by(insuranceid=insuranceid).first()
        db.session.delete(company_ins)
        db.session.commit()

        # 再删insurance
        a = insurance.query.filter_by(insuranceid = insuranceid).first()
        db.session.delete(a)
        db.session.commit()



    #check
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

@app.route('/edit_insurance',methods = ['GET'])
def edit_insurance():
    # insuranceid = request.values.get('insurance_id')
    # insurance_name = request.values.get('insurance_name')
    # insurance_des = request.values.get('insurance_description')
    # companyname = request.values.get('company')
    # businessid = request.values.get('business_id')
    # business_name = request.values.get('business_name')
    # business_des = request.values.get('business_description')
    #
    # a = insurance.query.filter(insurance.insuranceid==insuranceid).all()
    # if len(a)!=0:
    #     a[0].insurancename=insurance_name
    #     a[0].insdescription = insurance_des
    #     db.session.commit()
    #
    # # b = company_insurance.query.filter(company_insurance.insuranceid == insuranceid).all()
    # # if len(b)!=0:
    # #     companyid = b[0].companyid
    # #
    # #     c = company.query.filter(company.companyid == companyid).all()
    # #     if len(c) != 0:
    # #         c[0].companyname = companyname
    # #         db.session.commit()
    #
    # # b_c = company_insurance.query.filter(company_insurance.insuranceid == insuranceid).all()
    # # b = business.query.filter(business.businessid==businessid).all()
    # # if len(a)!=0:
    # #     a[0].insurancename=insurance_name
    # #     a[0].insdescription = insurance_des
    # #     db.session.commit()
    #
    # b = business.query.filter(business.businessid==businessid).all()
    # if len(a)!=0:
    #     b[0].businessname=business_name
    #     b[0].busdescription = business_des
    #     db.session.commit()
    #
    #
    # check = insurance.query.filter(insurance.insuranceid==insuranceid,insurance.insurancename==insurance_name,
    #                                insurance.insdescription==insurance_des).all()
    # checkb = business.query.filter(business.businessid==businessid,business.businessname==business_name,
    #                                business.busdescription==business_des).all()
    # if len(check)!=0 and len(checkb)!=0:
    #     data = {
    #         'result': 'yes',
    #     }
    #     jstr = json.dumps(data)
    #     return jstr
    # else:
    #     data = {
    #         'result': 'no',
    #     }
    #     jstr = json.dumps(data)
    #     return jstr


    insuranceid = request.values.get('insurance_id')
    insurance_name = request.values.get('insurance_name')
    insurance_des = request.values.get('insurance_description')
    companyname = request.values.get('company')
    businessid = request.values.get('business_id')
    business_name = request.values.get('business_name')
    business_des = request.values.get('business_description')

    a = detail_insurance.query.filter(detail_insurance.insuranceid==insuranceid).all()
    print(insuranceid)
    if len(a)!=0:
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
