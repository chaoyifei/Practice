#coding=utf-8

class Employee:
    '''所有员工的基类'''
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print "Total Employee %d" %Employee.empCount

    def displayEmployee(self):
        print "Name:",self.name,", Salary:",self.salary


#创建Employee类的对象
emp1=Employee("zara",2000)
emp2=Employee("manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d"%Employee.empCount
