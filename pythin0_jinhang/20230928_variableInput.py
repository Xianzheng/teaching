# print("Hello")

'''
# num1 is variable name
num1 = 10

print(num1)

# when program read input(), it will stop, and wait you input
# if you dont input, program will stop and wait you until you input
num2 = int(input('please type a num2:'))

print('num2 is',num2)

num3 = 30

print(num3)

print('wait you input, if you don \' t input, program won \'t terminate')

input()

print('program terminated')

'''


num1 = input() # input is a string '10', 10 is a number
num2 = input()


print('string concat',num1 + num2)

# whatever we input, input() always is a string


# if we want input() do mathmatic calucalation, we need to convert string input to int input

num3 = int(input()) # int(input()) to convert string input() to number

num4 = int(input())
print('math calculate',num3 + num4)
print(type(num1),type(num2))

print(type(num3),type(num4))


