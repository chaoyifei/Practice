#coding=utf-8
import re
line="cat are smarter than dogs"
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
    print "group():",matchObj.group()
    print "group（1）:",matchObj.group(1)
    print "group(2):",matchObj.group(2)
else:
    print "nothing found"



#re.match 和 re.search的区别

matchObj=re.match(r'dogs',line,re.M|re.I)
if matchObj:
    print "match-->",matchObj.group()
else:
    print "No match"
matchObj=re.search(r'dogs',line,re.M|re.I)
if matchObj:
    print "serch-->",matchObj.group()
else:
    print "No match!!"



#检索和替换

phone="2004-959-559#电话号码"
#删除电话号码中的注释
num=re.sub(r'#.*$',"",phone)
print "电话号码是：",num
#删除非数字字符串
num=re.sub(r'\D',"",phone)  
print "电话号码是：",num


#repl参数是个函数

#将匹配的数字乘2
def double(matched):
    value=int(matched.group('value'))
    return str(value*2)
s='A23G4HF123'
#此处?P<value>命名的group
print (re.sub('(?P<value>\d+)',double,s))