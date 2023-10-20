# OOP(oritented objected program)
'''
class Info:
    # name = name
    # price = price
    def __init__(self, name, price):
        self.name = name

        self.price = price
        print('Hello I was created')

    def __str__(self):
        return self.name + 'price is' + self.price
# def __init__(self): magic method. a instance of this class was created, __init__ magic method will call onece

# how to add attribute to class, seft.name = ? self.price = ?

# def __str__ is another magic method, use to print string rather than address:

a = Info('Pen','1$') # class Info's instance was created
b = Info('Pencil', '2$')


print(a)
print(b)

# practice :

# try to build a class Animal

# class will have attribute, name, age, size

# when we print instance of class, it will show all info of this instance

class Animal:

    def __init__(self,n,a,s):
        self.name = n # self.name is class attribute, n is argument
        self.age = a
        self.size = s

    def __str__(self):
        return 'name is {} age is {} size is{}'.format(self.name,self.age,self.size)
    
cat = Animal('cat1','5 years old','10 ')
dog = Animal('dog1','6 years old','16 ')

print(cat)
print(dog)
'''

# input three lines

# 12 +
# 13 #
# 10 *

#output
 
# +++... +
# ###...  #
# ***...*

def a(string):
    lst = string.split()
    print(int(lst[0])* lst[1])

#call function we just make
a('12 +')
a('13 #')
a('10 *')

# str2 = '123456789'
# reverse print str2
# outout put should be 987654321
str2 = '123456789'
str3 = 'qwertyuiop'

#DRY(DON'T TRY YOURSELF)
#index  012345678
# length = len(str2)
# for i in range(length - 1,-1,-1):
#     print(str2[i],end = '')

# length = len(str3)
# for i in range(length - 1,-1,-1):
#     print(str3[i],end = '')

def reversePrint(string):
    length = len(string)
    for i in range(length - 1,-1,-1):
        print(string[i],end = '')
    print()

reversePrint(str2)
reversePrint(str3)

# save code
# make code readable
#1.
# using class or function to do 2019CCC question J1, J2
# CCC 2019 URL
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf

#2.
# DO FUNCTION JUDGE IF STRING IS PALINDROME
# 'abcde' is not palindrom
# 'abccba is palindrom
def isPal(string):
    pass
    # hw content

isPal('abcde') # it will print False
isPal('abccba') # it will print True


