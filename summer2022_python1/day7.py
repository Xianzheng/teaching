'''
number = int(input('please type any number\n'))

print('the number you type is',number)

# 22 -> even 11 -> odd if number % 2 == 0

# if true will be executed, if false will not be executed\

# if condition:
#   statement1
# else:
#   statement2  
# when condition is True statement1 will be executed, when condition is 
# False statement2 will be excuted

if number % 2 == 0:
    print(number,'is a even number')
else:
    print(number,'is a odd number')

# condition statement
'''
#   loop statement # while loop , for loop
#   print 1 to 100, print 1 - 10000
# 1
# 2
# .
# .
# .
# 5
# print all even numbers in 1 to 10
# 2 4 6 8 10
i = 0

while i < 10:
    i = i + 1

    if i % 2 == 0:
        print(i,'is even')

i = 0
while i < 10:
    i += 2
    print(i,'is even')

# boolean value is to control program

# homework
# print all even numbers between 1 to 10
# print all odd numbers between 1 to 10
