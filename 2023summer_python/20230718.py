# Email = "soleil_li@icloud.com"
#
# name = Email.split("@")[0].split("_")
# first_name = name[0]
# last_name = name[1]
# Email = Email.split("@")[1]
# print("First Name:", first_name)
# print("Last Name:", last_name)
# print("Email:", Email)

# for _ in range(14):
#     print("x" * 14)
#     if _ in [1, 7, 13]:
#         print("x" * 14)

'''
*
**
***
****
*****

# for i in range(1,7):
#     for j in range(i):
#         print("*",end="")
#     print()

for i in range(1,7):
    for j in range(i):
        print('*', end=' ')
    print('')

for i in range(1,7):
    print('*')



# *****
# ****
# ***
# **
# *
# range(5) is [0,1,2,3,4], length is 6
for i in range(5):
    for _ in range(5-i):
        print('*',end='8') # end='', don't jump to next line, follow last *
    print()# jump to next line

#Pyramid Pattern in python
    *
   ***
  *****
 *******
*********
'''
n = 5 # how many line for pyramid

for i in range(1,n+1): # how many line we will print
    for j in range(n - i):
        print(' ',end='') # how many spaces we will print for each line
    for k in range(2 * i - 1):
        print('*',end='')# how many stars we will print for each line
    print()

'''
#Hollow Pyramid Pattern 
    *
   * *
  *   *
 *     *
*********

# diamond star 
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
'''

hw:
build pattern
square:
*****
*****
*****
*****
*****

Left Triangle Star Pattern
1
11
111
1111
11111

Right Triangle Star Pattern
    2
   22
  222
 2222
22222
'''