'''
# 1 + 2 + 3 + ... + 100 = ?

sum = 0

i = 0

while i < 100:

    i += 1

    sum += i

print(sum)
'''

'''
eample1
input
1
2
3
4
0

output:
10

example2:
1
5
9

output:
you can not add 9, program is end

sum = 0
while True:

    inp = int(input())

    sum += inp

    if inp == 0:

        print(sum)

        break

    if inp == 9:

        print('you can not add 9, program is end')

        break
'''

# for loop
# let loop run how many times, print Hello World 3 times
# get sum 0 + 1 + 2 + ... + 10 = ?
sum = 0 # we can use variable to get sum

for item in range(11):

    if item % 2 == 0:


        sum += item

# print(list(range(10)))
print(sum)

# range(10) -> start from 0 stopby 10 , but not stop at 10 so it goes through 0, 1, 2, 3 4 ... , 9

# range(11) -> start from 0 stopby 11 , but not stop at 11 so it goes through 0, 1, 2, 3 4 ... , 10

# use for loop to count 1 + 2 + 3 + ... + 100 = ?

# print all odd numbers between 1 to 100

# get sum of all odd numbers between 1 to 100