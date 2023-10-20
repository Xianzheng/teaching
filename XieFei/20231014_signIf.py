'''
inp = input('please type something you want:')


print(inp)

#input() no matter you type in terminal , it is a string

numA = float(input('please type number A:'))

numB = float(input('please type number B:'))

print('number A add number B is', numA + numB)


# type is very important for python
a = 10
print(type(a))
# integer value
b = 10.0
# float value
print(type(b))
print(a == b)

# sign, 
# math sign, +, -, * , / ,%, //, **
# compare sign, >, <. <=, >=, ==(does equal)
# value give sign, =(give value to), +=, -=, /=, *=
num1 = 10
num2 = 20

# print(num1 < num2)

# print(num1 > num2)

# True or False is a boolean value
num3 = 40

num4 = 40

# print(num3 <= num4)
# print(num3 == num4)

print(num1)
num1 += 1
print(num1)
num1 *= 3
print(num1)
print(num1 + 2)
print(num1)


# int, float , boolean type(True,False)
'''
FinishHome = False


if FinishHome == True:
    print('you can go to watch TV')


if FinishHome == False:
    print('you have to finish homework first')

'''
if condition:
    statement

if condition is True, statement will be executed, if condition is False, statement will not be executed
'''

if FinishHome == True:
    print('you can go to watch TV')
else:
    print('you have to finish homework first')

'''
if condition:
    statement1
else:
    statement2

if condition is True, statement1 will be executed, if condition is False, statement2 will be executed
'''

# how to calculate area of circle\

# radius of a circle

# area = radius * pie(3.14) ** 2

# you need to input the radius of circle 

# calculate the area

# if area is bigger than 100 , we print this is a big circle, else we print this is a small circle

# radius = float(input('please type the radius of circle:'))

# area = radius * 3.14 ** 2

# if area > 100:
#     print('this is a big circle')
# else:
#     print('this is a small circle')



'''

calculate the area of triangle

you need to input base, height

# write a if statement , it is up to you(for example it is bigger than 100 do some else do another thing)
'''

base =  float(input('please type a number of the base'))
hight = float(input('please type a number of the hight'))

area = ((base * hight)/ 2)
if area < 153:
    print('This triangle is rather small')
else:
    print('This is a rather big triangle')

