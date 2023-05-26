'''
question : get answer 1 + 2 + 3 ... + 100 = ?
ctrl + c -> end


# solution1
sum = 0
i = 0

while i < 100:
    i += 1
    sum += i
    

print(sum)

# deadly loop 


solution2 = (100 + 1) * (100 / 2)
print(solution2)

a = 10
# if elif else while
# name guess number
# library
import random

i = 0

while i < 10:
    number = random.randint(1,10)

    print(number)

    i += 1

'''
import random # load a library to python program

randomNumber = random.randint(1,10) # rn means randomNumber
print('random is given')

ourNumber= int(input('please type your guess:')) # if we get 3 times to guess

#if else
if randomNumber == ourNumber:
    print('you get me')
else:
    print('you did not get me')
    print('correct answer is', randomNumber)

