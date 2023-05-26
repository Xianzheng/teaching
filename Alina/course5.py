# write a program, given variable score1 with a value 231
# given variable score2 with a value 322
# judge whether score1 * score2 is bigger than score1 power 1.5 , or smaller than score1 power 1.5
'''
score1 = 231 # create variable score1

score2 = 322

print('score1 is',score1)

print('score2 is',score2)

a = score1 * score2

b = score1 ** 1.5

if(a > b):
    print(1)
else:
    print(2)

print(a)

print(b)

# value given sign
a = 321

print(a + 5)

print(a)

a += 5
print(a)

a -= 3

a *= 3

a /= 3

print(a)


# and or or

FinishedHw = False
PassTest = True

if FinishedHw or PassTest:
    print('you can go to watch TV')
else:
    print('you can not go to watch TV')

print(not FinishedHw)

print(not PassTest)

'''

# homework
# copy and run
a = 10
b = 20

if (a and b):
    print("1 - variables a and b are both true")
else:
    print("1 - one of the variables a and b is not true")

if (a or b):
    print("2 - variables a and b are both true, or one of the variables is true")
else:
    print("2 - neither variable a nor b is true")

# Modify the value of variable a
a = 0
if (a and b):
    print("3 - variables a and b are both true")
else:
    print("3 - Either variable a or b is not true")

if (a or b):
    print("4 - variables a and b are both true, or one of the variables is true")
else:
    print("4 - neither variable a nor b is true")

if not (a and b):
    print("5 - variables a and b are both false, or one of the variables is false")
else:
    print("5 - variables a and b are both true")

