'''
# condition statement

# if , if else, if elif elif else
quizScore = int(input('please type your quiz scores\n'))

condition1 = quizScore >= 80
condition2 = quizScore >= 70
condition3 =  quizScore >= 60
condition4 = quizScore < 60

if condition1:
    print('A')
elif condition2:
    print('B')
elif condition3:
    print('C')
else:
    print('D')

# if condition1:
#     print('A')
# if condition2:
#     print('B')
# if condition3:
#     print('C')
# else:
#     print('D')
'''
# if dog age == 1: equals 14 years age people
# if dog age == 2: equals 22 years age people
# if dog age > 2: equals (22 + (dog's age - 2) * 5) years age people

dogAge = int(input('please type dog age\n'))

if dogAge == 1:
    print('equals 14 years old people')

elif dogAge == 2:
    print('equals 22 years old people')

elif dogAge > 2:
    humanAge = 22 + ( dogAge - 2) * 5
    print('equals',humanAge,'years old people' )

# homework:
# practice today's code
# type a number, try to judge this number is a even number or a odd number
# 22 -> even 11 -> odd if number % 2 == 0