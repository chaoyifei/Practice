#coding=utf-8
#python操作数据库

import MySQLdb

#打开数据库链接

db=MySQLdb.connect(host="localhost",user="root",db="mysql",passwd="123456")
#使用cursor（）方法获取操作游标
cursor=db.cursor()
#使用execute方法执行sql语句
cursor.execute("select version()")
#使用fetchone()方法获取一条数据库
data=cursor.fetchone()
print "Database version: %s" %data

#关闭数据库
db.close()
