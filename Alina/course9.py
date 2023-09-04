'''
control statement
'''



'''

score > 90 : A

90 > score >= 80 : B

80 > score >= 70 : C

70 > score >= 60 : D
'''

'''
score = 99

if score > 90:
    print('A')

if 90 > score >= 80:
    print('B')

if 80 > score >= 70:
    print('C')

if 70 > score >= 60:
    print('D')

'''
'''

if condition:

    statement

# if condition is True, statement will be executed

# if condition is False, statement will not be executed


score = 77

condition = 80 > score >= 70

condition1 = score > 90

print(condition1)

if condition1:
    print('C')


score =int(input('please type your score:'))

if score >= 90:
    print('A')

if 90 > score >= 80:
    print('B')

if 80 > score >= 70:
    print('C')

if 70 > score >= 60:
    print('D')

if score < 60:
    print('E')

'''

# please type two number, ask if the sum of two numbers is bigger than 10

# if it is bigger print yes, else print no

num1 = int(input('please type number1: '))

num2 = int(input('please type number2: '))

if num1 + num2 > 10:
    print('yes')

if num1 + num2 <= 10:
    print('no')
