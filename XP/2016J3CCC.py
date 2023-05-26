'''
def isPal(string):
    
    if string == string[::-1]:
        return True
    else:
        return False


print(isPal('abc'))# it will print False
print(isPal('ana'))# it will print True
print(isPal('banana'))# False
print(isPal('anana'))# True

# string = 'ana'
# # print(string)
# #pascal method
# print(string[::-1])
# rString1 = string[::-1]
# print(string == rString1)


string = 'banana' # using slicing to get 'ana' from 'banana'
#         012345
#string[start:stopby:step]

sliceString = string[1:4:1]
print(sliceString)
#using slice to get 'an' from 'banana'

#'banana' # 'b','ba','ban'

def isPal(string):
    
    if string == string[::-1]:
        return True
    else:
        return False
    
string = input()
collector = []
for i in range(len(string)):
    for j in range(len(string)+1):
        piece = string[i:j]
        # if piece is no empty we do something
        if piece:
            # if piece is palindrome do something
            if isPal(piece):
                # put length of palindrome piece to collector
                collector.append(len(piece))

print(max(collector))
'''
# how to do palidrome function
# how to use slice to cute
# how to use nested loop

# there is a box, it has a 4 digit password, we want to option this box
# each digit is integer digit betweem 0 to 9
import random
password = ''
for i in range(4):
    password += str(random.randint(0,9))

for i in range(10):
    for j in range(10):
        for z in range(10):
            for k in range(10):
                if str(i)+str(j) +str(z) + str(k) == password:
                    print(str(i)+str(j) +str(z) + str(k))
                    break

print('realPassword is', password)