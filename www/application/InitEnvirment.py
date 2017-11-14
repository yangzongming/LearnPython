# -*- coding: UTF-8 -*-
#coding: UTF-8

#初始化数据库 数据库名 ilovecar


import MySQLdb
import json

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Main:
    pass
    def init(self):
        db = MySQLdb.connect("localhost","root","12345678","ilovecar")
        cursor = db.cursor()
        #创建员工数据表

        sql = """CREATE TABLE user (
         ID INT(20) not null AUTO_INCREMENT,
         NAME  TEXT,
         PASSWORD TEXT,
         PHONE varchar(11),
         ADDRESS TEXT )"""
        try:
            cursor.execute("DROP TABLE IF EXISTS user")
            cursor.execute(sql)
            db.commit()
        except:
            print("创建user数据库失败了")

        #插入数据
        #create table employee(ID INT(20) not null AUTO_INCREMENT,NAME  TEXT,NUMBER INT,PHONE varchar(11),ADDRESS TEXT ,primary key (id));
        #alter table employee modify NAME text character set utf8;
        #alter table employee modify ADDRESS text character set utf8;
        #alter table employee modify PHONE varchar(11) character set utf8;

        #创建表
        #create table customer(ID INT(20) not null AUTO_INCREMENT,NAME TEXT ,PHONE varchar(11),RECOMMENDID INT,RECOMMENDNAME TEXT ,TIMEVALUE TEXT,primary key (id));
        #alter table customer modify NAME text character set utf8;
        #alter table customer modify PHONE varchar(11) character set utf8;
        #alter table customer modify RECOMMENDNAME TEXT character set utf8;
        #alter table customer modify TIMEVALUE TEXT character set utf8;


        #例子
        #sql = "INSERT INTO customer(NAME,PHONE,RECOMMEND)VALUES ('%s', %d, %d);" % (name,int(phone),int(employeeid))
        #alter table users modify username char(20) character set utf8;
        db.close()


if __name__ == "__main__":
    print('开始初始化数据库')

    m = Main()
    m.init()

    print('数据库初始化完毕')