'''
# string '', list [],dictionary{'key':'value'},set{'apple',1,2,3}, tuple


def add(a,b):
    return a + b


# make a unlimited argument
def add1(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum


def myPrint(**kw):
    sum = 0
    for key in kw:
        sum += kw[key]
    return sum


def add(any):
    print(any)
    sum = 0
    for i in any:
        sum += i
    return(sum)

'''

#function class
# this is function
def functionName(a, b):
    return a + b

# class
class Student():
    name = ''
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def goHome(self):
        return 'go home'
# create space in memory
# create a instance of class Student
andrew = Student('Andrew',13)
# create a instance of class Student
kevin = Student('Kevin',14)

print(kevin.age)
print(andrew.age)

print('after one year')

kevin.age += 1
andrew.age += 1

print(kevin.age)
print(andrew.age)

print(kevin.name, kevin.goHome())# with a brucket , it is a method
print(andrew.name, andrew.goHome())

class Animal:

    name = ''
    age = 0

    def bark(self,voice):
        print(voice)

cat = Animal()
cat.name = 'Cat'
cat.age = 10
cat.bark('mow mow')


dog = Animal()
dog.name = 'Dog'
dog.age = 5
dog.bark('wow wow')
'''
open ending homework
build function unlimited argument with *args, **kw do  pactice

build class House, you can think what you have to make attribute, build a method for functionality
of youe house
'''



