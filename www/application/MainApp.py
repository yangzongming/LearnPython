#/usr/bin/env python
#coding=utf-8

from bottle import get,post,request
from bottle import route,run
from bottle import template
from bottle import view
from bottle import static_file

@get('/register')
@view('register')
def register():
    pass

@post('/register')
def register_form():
    user_name = request.forms.get('username')
    e_mail = request.forms.get('email')
    return template('register_result',name=user_name,email=e_mail)

run(host='0.0.0.0',port=8080,debug=True)
