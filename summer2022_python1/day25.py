'''
ask you input your testScore

if testScore is in 80 - 100 A
if testScore is in 70 - 80 B
if testScore is in 60 - 70 C
else < 60 D
'''

testScore = int(input('please type your test score\n'))

if testScore >= 80 and testScore < 100:
    print('A')

if testScore >= 70 and testScore < 80:
    print('B')

if testScore >= 60 and testScore < 70:
    print('C')

if testScore < 60:
    print('D')