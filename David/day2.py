# sign : compare sign, operator sign, logic sign

# variable # don's use python key word as variable name

# numbers : int, float, boolean(True/False)

# boolean value is the key for control program

# condition statement

'''
#1 if

if condition:
    statement

condition is boolean value or contains boolean attribution
when condition or condition's attribute is True statement will be executed
when condition or condition's attribute is False statement will not be executed



a = int(input('please type your test score\n'))
if a > 90:
    print("go have fun")

if a <= 90:
    print('go study')


print('Hello\nWorld')
'''

'''
if condition:
    statement1
else:
    statement2
    
when condition or condition's attribute is True statement1 will be executed
when condition or condition's attribute is False statement2 will be executed
'''

# type score on console
# scores >= 80 Level A
# scores >= 70 and scores < 80 Level B
# scores >= 60 and scores < 60 Level C
# scores < 60 Level D

# testscore = int(input("your score:\n"))
# if testscore >= 80:
#     print("Level A")
# if testscore >= 70 and testscore < 80:
#     print("Level B")
# if testscore >= 60 and testscore < 70:
#     print("Level C")
# if testscore < 60:
#     print("Level D")

'''
if condition:
    statement
elif condition1:
    statement1
elif condition2:
    statement2
else:
    statement4

testscore = int(input("your score:\n"))
if testscore >= 80:
    print('Level A')
elif testscore >= 70:
    print('Level B')
elif testscore >= 60:
    print('Level C')
else:
    print('Level D')

# type dog's age, convert to human age
#1 years old dog equals 14 years old people
#2 years old dog equals 22 years old people
#above 3 years old dog equals 22 + (dogAge - 3) * 3 years old people

ageD = int(input("dog's age:\n"))
if ageD == 1:
    print("The human age is age 14")
elif ageD == 2:
    print("The human age is age 22")
else:
    print("The human age is", 22 + (ageD - 3) * 3)
    


TeamA_3pointscore = int(input())
TeamA_2pointscore = int(input())
TeamA_1pointscore = int(input())
At = TeamA_1pointscore * 1 + TeamA_2pointscore * 2 + TeamA_3pointscore * 3
# print("Team A total score is", At)

TeamB_3pointscore = int(input())
TeamB_2pointscore = int(input())
TeamB_1pointscore = int(input())
Bt = TeamB_1pointscore * 1 + TeamB_2pointscore * 2 + TeamB_3pointscore * 3
# print("Team A total score is", Bt)

if Bt > At:
    print("B")
elif Bt < At:
    print("A")
elif Bt == At:
    print("T")

'''

#homework

# 1. Write a program that prompts the user to input three integers and outputs the largest.

# 2.
# The marks obtained by a student in 3 different subjects are input by the user.
# Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
#
# Average	Grade
# 90-100	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F Solution

# 3. Write a program that prompts the user to input a number. Program should display the corresponding days to the number.
# For example if user type 1 the output should be sunday. If user type 7 the output should be saturday.

# CCC 2018 J1
#https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/juniorEF.pdf