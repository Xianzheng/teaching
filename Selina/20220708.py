'''
# inp * 8 = ?

inp = int(input('please type a number'))

result = inp * 8

print(inp,'* 8 = ',result)
'''

# 1 years old dog equals 14 yeas old people

# 2 years old dog equals 22 years old people

# above or equals 3 years old dog equals 22 + (dogAge - 2) * 5 year old people

# if elif elif

dogAge = int(input('please type dog age'))

if dogAge == 1:
    print('equals 14 yeas old people')

elif dogAge == 2:
    print('equals 22 years old people')

elif dogAge >= 3:
    print('equals',22 + (dogAge - 3) * 5,'year old people')

# write a small program, type a number, judge this number is a even number or odd number
# number % 2 == 0 -> this is a even number, number % 2 == 1 -> odd number


