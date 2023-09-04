# pseudocode（伪代码）

'''
# requirement : write a programe to judge a sum of two number is bigger than 10

# if a + b is bigger than 10, then print out it is bigger

# if a + b is smaller than 10, then print out it is smaller

# requirement : write a function to  to judge a sum of two number is bigger than 10

#write a function which receive two arguments 

if if argument1 + argument2 is bigger than 10, then print out it is bigger/ return it is bigger

# practice write pseudocode / programe consider

# create a list, to make list have apple banana cherry

'''


# function（函数）

'''
type:
#write a function which receive two arguments 
def (functionName)(([argument1,argument2])):

    #if if argument1 + argument2 is bigger than 10, then print out it is bigger/ return it is bigger

#we need to cal functionName to make it invoke

'''
'''
def adding(arg1,arg2):
    if arg1 + arg2 > 10:
        print('it is bigger')
    if arg1 + arg2 < 10:
        print('it is smaller')
    if arg1 + arg2 == 10:
        print('it is equal')


adding(int(input()),int(input()))
adding(int(input()),int(input()))
adding(int(input()),int(input()))
adding(int(input()),int(input()))

# function can make code eaier to write
# DRY(don't repeat yourself)

'''


# class(类)


class Box:
    def __init__(self):
        
        self.pen1 = Pen('pen1')
        self.pencil1 = Pencil('pencil1')
        self.pen2 = Pen('pen2')

class Pen:
    def __init__(self,name):
        self.name = name

class Pencil:
    def __init__(self,name):
        self.name = name

#initialize Box

if __name__ == '__main__':
    box = Box()
    print(box.pen1.name)
    print(box.pencil1.name)
    print(box.pen2.name)
   


'''
consider write two function:

write plus/time function using pseudocode to show

write class Zoom, it has several animal Dog, Animal, elephant

add two animal to Zoom

consider to activate venv and running snake1.py 
'''
# instance/method(方法)

# practice打开视频

# 2

class Zoom:
    def __init__(self):
        print('Hello')
    