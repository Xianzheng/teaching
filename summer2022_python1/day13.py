'''
# range

range(6) # 0,1,2,3,4,5 [0,6) start from 0, stopby 6 default start from 0 stopby 6 default step is 1

range(1,6) # it has two arguments, start from 1 stopby 6 default step is 1

for item in range(3,6):
    print(item)

#print 1,3,5,7,9

# print(list(range(1,6,2)))
for item in range(1,5,2): # start from 1 , stopby 5 , step is 2
    print(item)

# use for loop to count 1 + 2 + 3 + ... + 100 = ?

sum = 0
for nums in range(1,101):
    print(sum,'+',nums,'=',sum + nums)
    sum += nums

print(sum)


# print all odd numbers between 1 to 100



# for num in range(101):
    
#     if num % 2 != 0:

#         print(num) 

# for num in range(1,100,2):

#     print(num)

'''
# interpret language

# compile language

# get sum of all odd numbers between 1 to 100

sum = 0

for nums in range(1,100,2):
    print(sum,'+',nums,'=',sum + nums)
    sum += nums# sum = sum + num

print(sum)

# homework
# use for loop to do:
# print all odd numbers between 1 to 100
# print all even number between 0 - 100
# get sum of all all even number between 0 - 100

#