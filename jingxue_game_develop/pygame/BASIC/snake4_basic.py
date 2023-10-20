def info( arg1):

    print('arg1 is',arg1)

def info1(*arg): #可变参数

    argLen = len(arg)
    for i in range(argLen):
        print(arg[i])

#字典参数
def info2(**arg): #指定字典参数
    arg1 = arg['arg1']
    arg2 = arg['arg2']
    arg3 = arg['arg3']
    print(arg1)
    print(arg2)
    print(arg3)



# info('this is info')

# info1('1','2','3')

# info2(arg1='1',arg2='2',arg3='3')

class Info:
    #attribute

    def __init__(self,cost):
        self.cost = cost
    
    def __str__(self):
        # you must return a string
        return str(self.cost)


# def __specifName__(self, *arg) is magi method with indicated function


# __init__ method means when a instance of class was created ,
# __init__ magic method will run once

# a = Info() # a is instance of class, Info() is a instance of class
# print(id(a))
# b = Info()
# print(id(b))

# __str__ magic method means when you want to print instance you can
# get value rather than a address
a = Info(1)
print(a.cost)

print(a)