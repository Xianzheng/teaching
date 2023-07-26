'''
Left Triangle Star Pattern
1
11
111
1111
11111

for i in range(1,6):
    for j in range(i):
        print('1',end='')
    print()

for i in range(1,6):
    print('1'* i)

Right Triangle Star Pattern
    2
   22
  222
 2222
22222

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "2" * i)

n= 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ',end="")
    for j in range(i):
        print('2',end='')
    print()


print('*' * 5)
string = "5 *"
print(int(string[0]) * string[2])
# full pyramid Pattern
    *
   ***
  *****
 *******
*********
#Hollow Pyramid Pattern
    *
   * *
  *   *
 *     *
*********

n = 10 # how many line for pyramid

for i in range(1,n+1): # how many line we will print
    for j in range(n - i):
        print(' ',end='') # how many spaces we will print for each line
    for k in range(2 * i - 1):
        if k == 0 or k == (2 * i - 2):
            print('*',end = '')
        else:
           if i == n:
               print('*',end='')
           else:
               print(' ',end='')

        # print(k,end='')# how many stars we will print for each line
        #do some if statement
    print()

num = 10
for i in range(num):
    if i == 0 or i == (num - 1):
        print(i)

*
**
***
****
*****
****
***
**
*



for i in range(1,6):
    print('*' * i)

for i in range(4,0,-1):
    print('*' * i)

i = 3
print(i * '*')
[1,2,3,4,5]
for i in range(1,6):
    print(i,end=':')
    print(i * '*')

#Reverse Pyramid Pattern

*********
 *******
  *****
   ***
    *


# Diamond Star Pattern
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


'''








