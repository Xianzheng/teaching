'''
# operator sign: + - * / % // ** it will get a number
# compare sign : > < == >= <= != it will get a boolean value(True/False)
# logic sign : and , or , not,  it will get a boolean value

# and it needs all conditions are True, it will get a True, else False
c1 = 5 > 3
c2 = 2 < 4
c3 = 5 == 5
print(c1 and c2 and c3)

# or it needs one of conditions is True, it will get a True, else False

c1 = True
c2 = False
c3 = False
print(c1 or c2 or c3)

c1 = False
c2 = not c1
print(c2)

# 0 1
# False True(0 means False, not 0 is True)
# why boolean value is important for programming(python)

# boolean value is a key to control program

# statement condition
# 0 -> you did not finish today's homework
# 1 -> you finish today's homework
condition = 1
statement = 'you can watch TV'

if condition:
    statement

# if condition is True statement will be execute, if false it will not

# print will put what you write to console
# 0 -> you did not finish today's homework
# 1 -> you finish today's homework
condition = 1

statement1 = 'you can go to watch TV'
statement2 = 'you must finish today\'s homework'

if condition:
    print(statement1)
else:
    print(statement2)

'''

# condition is more than 2

# > = 80  => A level
# 70 - 80 => B level
# < 70 => C level
quizScore = 60

condition1 = quizScore >= 80
condition2 = 70 <= quizScore < 80
condition3 = quizScore < 70

if condition1:
    print('A')
elif condition2:
    print('B')
elif condition3:
    print('C')

#homework: find scenarior in real life：
# write if statement, if else statement, if elif elif statement
# send me homework at mark.ffang@gmail.com