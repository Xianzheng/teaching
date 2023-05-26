'''
x = int(input())
y = int(input())

int(1)


if x > 0 and y > 0:
    print(1)
if x > 0 and y < 0:
    print(4)
'''
#  convert dog age to people's age

# 1 years old dog equals 14 years old people
# 2 years old dog equals 22 years old people
# above 3 years old old yeard (dog's age - 2) * 1.5 + 22 years old people

#input dog's age => equals how many years old people

dA = int(input())

if dA == 1:
    print('equals 14 years old people')

if dA == 2:
    print('equals 22 years old people')

if dA > 2:
    print('equal' ,(dA - 2) * 1.5 + 22 , 'years old people')