string = '24533424534564356'

'''
#index    0123456

# print 8 9 7 6 7 8 5 in console
#since string is iterable, we can print
for i in string:

    print(i,end = ' ')

# use index to print each character, how to print

length = len(string)

print('the length of string is',length)

# print each index

for index in range(length):
    # use index to access the string
    print(string[index])
'''
# get sum for each character
s = 0

for char in string:

    #print(char, type(char))

    # we need to convert string to integer

    num = int(char) # convert string to integer

    #print(num, type(num))

    s += num # collect each character to get sum

print(s)

# string = '368358063'
# print even character in string
# get sum for all even chracters