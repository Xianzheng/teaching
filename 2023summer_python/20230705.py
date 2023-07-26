'''
# what is boolean type, why this is important
# boolean type determine where code to go

# add control statement
# intro demo
a = 1
b = 2
c = 3

# we just want to show the number above or equal two

if a >= 2: # a >= 2 -> False
    print(a)

if b >= 2: # b >= 2 -> True
    print(b)

if c >= 2: # c >= 2 -> True
    print(c)


'''
'''
#basic 1 template:
#1 tap = 4 space = 1 indentation
if condition:
    statement
    
#  if condition is True statement will be executed, else statement will not be worked

b = 3

print('b is',b)
print('b < 2 is', b < 2)

if b < 2:
    print(1)

if b < 2:
    print(2)
    
#basic 2 template:

if condition:
    statement1
else:
    statement2

    
#  if condition is True statement1 will be executed, else statement2 will  be executed

# number must be different
a = 41230970+ 12314215619
b = b= 11328568931796- 1204708751

if a > b: # a > b is False
    print('a is bigger')
else:
    print('b is bigger or there are qual')
    
# basice template 3

if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3

# elif is short hand write for else if

a = 12
b = 12

if a > b:
    print('a is bigger')
elif a < b:
    print('b is bigger')
else:
    print('there are same')
'''

# your score in
# scores >= 90 -> A level
# scores >= 80 and scores < 90 -> B level
# scores >= 70 and scores < 80 -> C level
# else -> D level

scores = 88

if scores >= 90:
    print('A')
elif scores >= 80: # same with >= 80 and < 90
    print('B')
elif scores >= 70:
    print('C')
else:
    print('D')

'''
hw:
1.
number1 = ?# you can decide 
# hint: use control statement
write a code tell me if this number1 is a positive number or negative number or 0 

2.
you have mission to do:
Monday: you will attend math class
Tuesday: you will attend math class
Friday: you will attend python class
else : you are Free

you can use 1,2,3,4,5,6,7 to represent the day
write a code tell me which day you will do 


'''


