#coding=utf-8

#打开一个文件
fo=open("foo.txt","wb")
fo.write("www.runoob.com!\nVery good site!\n")
#关闭文件
fo.close()

#打开一个文件
fo=open("foo.txt","r+")
str=fo.read(10)
print "读取的字符串是：",str

#文件定位
position=fo.tell()
print "当前位置：",position

#把指针再次重新定位到文件开头
position=fo.seek(0,0)
str=fo.read(10)
print "重新读取字符串：",str


#关闭文件
fo.close()


#重命名和删除文件
import os

#重命名文件test1到test2
os.rename("test1.txt","test2.txt")

#删除test2.txt

os.remove("test2.txt")


#创建目录
os.mkdir("test")

#改变当前目录
os.chdir("/git/practice")

#获取当前目录
os.getcwd()

#删除目录
os.rmdir("test")




