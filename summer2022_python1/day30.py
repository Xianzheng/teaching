'''
can you use for loop to print 1 to 10?

#we talk slicing today

#for example we want to take weather out of string

# we should know where we start and where we end
'''
string = 'Today\'s weather is good'
print(string.find('w')) # the index of 'w' is 8
print(string.find('r')) # the ondex of 'r' is 14

# the weather out of string
print(string[8:15]) # it should print weather is consol

# question how to get 'is' from string

print(string.find('i')) # the index of 'i' is 16
# print(string.find('s')) # the ondex of 'r' is 17

# the is out of string
print(string[16:18]) # 