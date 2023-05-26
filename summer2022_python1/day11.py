'''
import random # load a library to python program

randomNumber = random.randint(1,100) # rn means randomNumber
print('random is given')

# if we get 5 times to guess

i = 0

while True:
    ourNumber= int(input('please type your guess:')) 
    #if else
    if ourNumber > randomNumber:
        print('it is bigger than mine')
    elif ourNumber < randomNumber:
        print('it is smaller than mine')
    else:
        print('you get me')
        break


print('correct answer is', randomNumber)

# it will give us more better response

# if our guess guess number is bigger than  random number, it will print it is bigger

# if our guess guess number is smaller than  random number, it will print it is smaller

# if our guess guess number is equal with random number, it will print you got me , break this loop

# we get unlimited time to guess until we make it



while True:

    inp = input('input:')

    if inp == 'q' or inp == 'quit':
        print('program is end')
        break

    else:
        print('output:',inp)

'''

# practice today's code

#write small program

# add number : we can add any numbers but not 9, 0 means you want get result
# input(), int(input)
# eample
'''
eample1
input
1
2
3
4
0

output:
10

example2:
1
5
9

output:
you can not add 9, program is end
'''