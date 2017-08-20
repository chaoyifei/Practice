#coding=utf-8
import MySQLdb
#打开数据库
db=MySQLdb.connect(host="localhost",user="root",db="test",passwd="123456")
cursor=db.cursor()
#如果数据表已经存在就删除
cursor.execute("drop table if exists employee")
#创建数据表

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

#插入数据
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
#查询
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
try:
    cursor.execute(sql)
    #获取所有列表
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
    # 打印结果
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income)
except:
    print "Error"

#数据库更新操作
sql="update employee set age=age+1 where sex='%c'"%('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#删除操作
sql="delete from employee where age>'%d'"%(20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
