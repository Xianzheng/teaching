'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(i,j,i*j),end = '')
    print()


ranslation: There are four numbers: 1, 2, 3, 4. 
How many different three-digit numbers can be formed 
without repeated numbers? What is each?

num = 1
print(num,type(num))
string = str(num)
print(string,type(string))
print(1 + 2 + 3)
print(str(1)+str(2)+str(3))
'''
count = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if x != y and y != z and x != z:
                print(x,y,z)
                count += 1
print('there are {} different number'.format(str(count)))


'''
homework:
Seeking = a + aa + aaa + aaaa + aa ... 
the value of a, where a is a number. 
For example, 2 + 22 + 222 + 2222 + 22222 
(5 numbers are added together at this time), 
and the addition of several numbers 
is controlled by the keyboard.

input:
2
5

ouput: 2 + 22 + 222 + 2222 + 22222 = ?
?
'''

# string can mutiply with number
print('2' * 2)
# number and string can be converted with eachother

# 1 + 2 + 3 + ... 10 = ?
sum = 0
for i in range(1,11):
    sum += i
print(sum)