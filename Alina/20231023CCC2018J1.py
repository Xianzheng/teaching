
# python program will wait you input
i1 = input('please type one digit:')
i2 = input('please type one digit:')
i3 = input('please type one digit:')
i4 = input('please type one digit:')


# compare operator, > , < ==(is equal)
# print(5 == 6)
# logic operator, or , and
# print(5 > 4 or 5 > 6)
# print(5 > 4 and 5 > 6)

cond1 = (i1 == '8' or i1 == '9')

cond2 = (i4 == '8' or i4 == '9')

cond3 = (i2 == i3)

if cond1 == True and cond2 == True and cond3 == True:
    print('ignore')
else:
    print('false')

'''
summary:

    how to do input: input()
    compare operator: >, <, ==
    logic operator, or , and

hw:

Do 2017J1:
link: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf
'''
