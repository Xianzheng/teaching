'''
version1
#class

# blueprint
class Student():
    # attribute
    name = ''
    age = 0
    id = ''

# instance of class
student1 = Student()
student2 = Student()
student3 = Student()

student1.name = 'Jingxue'
student1.age = 5;
student1.id = '123'

student2.name = 'Stephen'
student2.age = 4;
student2.id = '124'

student3.name = 'Andrien'
student3.age = 4;
student3.id = '125'

print(student3.name)
print(student3.age)
'''

#version2

class Student:
    # __init__ is a constructor, when a instance was build it will run once
    def __init__(self,name,age,id,pocketMoney,happy):
        print('{} was build with pocketMoney {} dolloars, {} happy point '
              .format(name,pocketMoney,happy))
        self.name = name
        self.age = age
        self.id = id
        self.pocketMoney = pocketMoney
        self.happy = happy

    # create class method
    def buyIcecream(self):
        self.pocketMoney -= 1
        self.happy += 2



stu1 = Student('Jingxue',5,'123',10,10)
stu2 = Student('Stephen',4,'124',10,10)
stu3 = Student('Andrien',4,'125',10,10)

# buy icecream once
stu2.buyIcecream()
# buy icecream once
stu2.buyIcecream()
print('{} pocketMoney is {}'.format(stu2.name,stu2.pocketMoney))
print('{} happy point is {}'.format(stu2.name,stu2.happy))

'''
hw:
create class  without see class demo

create instance and use class method

option
Jingxue buy three icecream
Andrien buy one icecream

see how many pocket money left and how many
happy point they have
'''

