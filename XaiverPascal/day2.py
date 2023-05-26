# sign naming variable,
# number

#number (int , float, boolean value) # True/False

# control statement

# if condition: # condition will be boolean value or condition has boolean attribution
#     statement
#
# when condition is True or boolean attribute is True, statement will be executed,
# when condition is False or boolean attribute is False, sstement will not be executed

'''
if 'a':
    print('Helalo World')


testScore = 80

if testScore > 80:
    print('you can go to watch TV')

if testScore < 80 or testScore == 80:
    print('you have to review your study stuff')

'''

'''
# if condition:
#     statement1
# else:
#     statement2
# # when condition is True or boolean attribute is True, statement1 will be executed,
# # when condition is False or boolean attribute is False, sstement2 will be executed


testScore = int(input('please type your testScore:'))# every thing is a object


if testScore > 80:
    print('you can go to watch TV')
else:
    print('you have to review your study stuff')
'''


'''
if condition:
    statement0
elif condition1:
    statement1
elif condition2:
    statement2
    
# s >= 80 level A
# 70 >= s < 80 level B
# 60 >= s < 70 level C
# s < 60 level D
# else if -> elif

s = 90

if s >= 80:
    print('level A')

elif s >= 70:

    print('level B')

elif s >= 60:
    print('level C')
else:
    print('level D')

# if s >= 80:
#     print('level A')
# 
# if s >= 70:
# 
#     print('level B')
# 
# if s >= 60:
#     print('level C')
# if s < 60:
#     print('level D')

print('please type your scores:')
s = int(input())

if s >= 80:
    print('level A')

elif s >= 70:

    print('level B')

elif s >= 60:
    print('level C')
else:
    print('level D')
'''

'''
example1
please type number A:
56
please type number B:
78
B is bigger

example2
please type number A:
2
please type number B:
1
A is bigger

example2
please type number A:
1
please type number B:
1
there are equal

print('please type number A:')
A = int(input())
print('please type number B:')
B = int(input())

if A > B:
    print('A is bigger')
elif A < B:
    print('B is bigger')
else:
    print('there are equal')

'''
# please type a number, let program to judge this number is a even or odd number
# print('please type a number')
# number = int(input())
# # % is to get reminder
# if number % 2 == 0:
#     print('this is a even number')
# else:
#     print('this is a odd number')


'''
89
11
80
this is a triangle

89
11
70
this is not a triangle

a + b + c == 180
'''

print('what is the first angle')
a = int(input())
print('what is the second angle')
b = int(input())
print('what is the third angle')
c = int(input())
if a + b + c == 180:
    print('it is a triangle')
else:
    print('it is not a triangle')


#homework

# 1. Write a program that prompts the user to input three integers and outputs the largest.

# 2.
# The marks obtained by a student in 3 different subjects are input by the user.
# Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
#
# Average	Grade
# 90-100	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F Solution

# 3. Write a program that prompts the user to input a number. Program should display the corresponding days to the number.
# For example if user type 1 the output should be sunday. If user type 7 the output should be saturday.