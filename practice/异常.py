#coding=utf-8
#try-finally语句
try:
    fh=open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常！！！")
finally:
    print "Error:没有找到改文件"


#except语句捕获异常的参数

#定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError,Argument:
        print "参数没有包含数字\n",Argument

#调用函数
temp_convert("xyz")

#异常触发

def mye(level):
    if level<1:
        raise Exception("Invalid level!",level)
try:
    mye(0)
except "Invalid level!":
    print 1
else:
    print 2
