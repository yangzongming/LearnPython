#/usr/bin/env python
#coding=utf-8

from bottle import get,post,request
from bottle import route,run
from bottle import template
from bottle import view

import bottle
from os.path import abspath, dirname, join
#指定的模板路径
CUSTOM_TPL_PATH = abspath(join(dirname(__file__), "www/views/"))
#静态文件
WEB_Bin_PATH = abspath(join(dirname(__file__), "web_bin/"))

bottle.TEMPLATE_PATH.insert(0, CUSTOM_TPL_PATH)  # 加载templates路径
bottle.TEMPLATE_PATH.insert(0, WEB_Bin_PATH)

@get('/register')
@view('register')
def register():
    pass

@post('/register')
def register_form():
    pass


run(host='0.0.0.0',port=8080,debug=True)
