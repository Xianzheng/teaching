# nestrd loop
'''
homework
1.use for loop to get sum for all odd numbers between 90 - 190(one loop)

2. print pattern(nested loop)

***** firtst row prints 5 stars
****  second row prints 4 stars
***   third row prints 3 starts
**    fourth row prints 2 stars
*     fifth  row prints 1 stars

3. Determine how many prime numbers are between 101-200, and output all prime numbers.

sum = 0
for i in range(90,191):
    if i % 2 != 0:
        sum = sum + i
print(sum)
'''

# first loop determing how many row we need to print
# each row we need to print how many starts
# row and how many starts actually get some relationship

# print('*',end=' ')#print will change to next line automatically
# print('*',end=' ')
# print('*') # print()default end = '\n'
# print('hello world')

# '\n' means change to next line, '' cancel change

# *****
# ****
# ***
# **
# *

# row and how many starts actually get some relationship
for i in range(5): # how many row to print
    for j in range(5 - i): # determine the content of each row
        print('*',end='') # since each row starts connect with each other
    print() # when we finish printing one row change to next line

'''
first
*
* *
* * *
* * * *

second

* * * *
* * *
* *
*

third one
*
* *
* * *
* * * *
* * *
* *
*


'''