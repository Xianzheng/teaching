'''
num = int(input())
name = ''
bid = 0
for _ in range(num):
    key = input()
    value = int(input())
    # if name == '' is the fist time input
    if name == '':
        name = key
        bid = value

    else:

        if value > bid:
            bid = value
            name = key

print(name)


first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

rule1 = (first == 8 or first == 9) # if follows rule means rule should be True, else False
rule2 = (fourth == 8 or fourth == 9)
rule3 = (second == third)

if rule1 == True and rule2 == True and rule3 == True:
    print('ignore')
else:
    print('answer')

# how to make a


# if condition:
#     statement
#
# if condition is True, statement will be executed


a = True
b = False
c = True

if a  and b and c :
    print('this is true')
else:
    print('it it false')
'''

# boolean value(True/False)

# consider the logic sign(and , or)

# print(False and False and False)
# print(False or False or False)
# for each control statement(loop statement / if statement) we use boolean value/ type ,
# to determine whether statement executed or not

if 0:
    print('this is True')
else:
    print('this is False')
'''
hw:
TRY TO DO ccc 2017 J1

LINK: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf
'''