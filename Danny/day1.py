'''
# 1 years old dog == 14 years old people

# 2 years old dog == 22 years old people

# above 3 years old dog == 22 + (dog age - 2 ) * 5 years old people


# please type dog's age -> equals how many years old poeple
# input can not small than one, input must be a integer 

dogAge = 0
humanAge = 0

dogAge = int(input())

if dogAge == 1:
    humanAge += 14

elif dogAge == 2:
    humanAge += 22 

elif dogAge >= 3:
    humanAge += 22 + (dogAge - 2)* 5


print(humanAge)


# get sum of all odd nums between 1 - 100  #  1 + 3 + 5 + ... + 99 = ? 
num = 0
sum = 0

while num < 101:
    if num % 2 != 0:
        sum += num
    num += 1

print(sum)


sum = 0

for i in range(1,100,2):
    sum += i
    
print(sum)
'''

'''
#input
1
2
3
4
0

#output
10

#input
99
100
0

#output
199

# key word is break
loop = 1

total = 0

while loop != 0:
    num = int(input())
    total += num
    if num == 0:
        break

print(total)

'''