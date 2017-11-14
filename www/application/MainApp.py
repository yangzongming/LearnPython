#/usr/bin/env python
#coding=utf-8
import MySQLdb
from bottle import get,post,request
from bottle import route,run
from bottle import template
from bottle import view

import hashlib

@get('/register')
@view('register')
def register():
    pass

@post('/register')
def register_form():
    user_name = request.forms.get('username')
    password = request.forms.get('password')
    #处理用户注册请求

    db = MySQLdb.connect("localhost","root","12345678","ilovecar" )
    cursor = db.cursor()

    md5 = hashlib.md5()
    md5.update(password)

    newname = user_name.encode('utf-8')
    sql = "INSERT INTO user(NAME,PASSWORD)VALUES ('%s', '%s');" % (newname,md5.hexdigest())
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        print("插入用户信息失败了")
    return template('register_result',name='ok')


@get('/login')
@view('login')
def login():
    pass


@post('/login')
def login_post():

    username = request.forms.get('username')
    password = request.forms.get('password')

    db = MySQLdb.connect("localhost","root","12345678","ilovecar" )
    cursor = db.cursor()

    md5 = hashlib.md5()
    md5.update(password)

    resultMsg = None
    #查询客户信息
    # SQL 查询语句
    sql = "SELECT * FROM user WHERE name='%s'" % (username)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        name = None
        pw = None
        for row in results:
            id = row[0]
            name = row[1]
            pw = row[2]
            # 打印结果
            print "姓名：name=%s" % \
            (name)
        if name != None and pw != None:
            if pw == md5.hexdigest():
                resultMsg = '登录成功了'
        db.commit()
    except:
        print "Error: unable to fecth data"
        resultMsg = '密码错误'
        db.rollback()
    return template('login_result',result=resultMsg)

run(host='0.0.0.0',port=8080,debug=True)
