'''
print (numbers) times Hello World
'''

# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')

'''

num = 0

# condition = num < 10 # True

while num < 10:

    print('Hello World')

    #chang condition
    num += 1
   

print('condition is False right now, program terminated')


# mission : print 1 2 3 4 .... 10

num = 0

while num < 10:

    num += 1
    
    print(num)

# while condition:

#     statement

# statement will change condition



# mission: print all odd numbers between 1 - 10(1,3,5,7,9)

# judge a num is a odd or even %

# do you remember what is %

num = 9

if num % 2 == 0:
    print('this number is a even number')
else:
    print('this number is a odd number')

num = 0

while num < 10:
    
    num += 1
    if num % 2 == 0:
        pass
    else:
        print(num)


'''
# hw:

# print all even numbers between 1 to 10

# use while loop to get result 1 + 2 + 3 + ... 10


# computer generate a random number
# import random means import library, 
import random 

# print('generated random number is:',r)
r = random.randint(1,10)
print('python already generate a random number between 1 - 10')
print()# it will print a empty line
# input in terminal(we talked)


#how to give us 3 oppertunity to guess
i = 0

while i < 10:
    
    n = int(input('please type a integer to match random number:'))

    # if equals(practice : if r equals(==) with n , print win, else print lose)

    if r == n:# random equals input number
        print('win',end='\n\n')
        break
    else:
        print('lose')

    i += 1

print('random number is', r)



