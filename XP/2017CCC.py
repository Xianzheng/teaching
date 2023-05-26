"""
#J1
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
if x < 0 and y > 0:
    print(2)
if x < 0 and y < 0:
    print(3)
if x > 0 and y < 0:
    print(4)

J2
# thinking 1

# print(12 * (10 ** 0) + 12 * (10 ** 1) + 12 * (10 ** 2) + 12 * (10 ** 3))

# for i in range(4):
#     print(i)

base = int(input())
num = int(input())
sum = 0
for i in range(num + 1):
    sum += base * (10 ** i)
print(sum)

# thinking2

# print(12 + 0)
# print('12' + '0', type('12' + '0'))
# print(int('12' + '0'), type(int('12' + '0')))
# print('0' * 2)
base = input()
num = int(input())
sum = 0
for i in range(num + 1):
    sum += int(base + '0' * i)
print(sum)

inp1 = input()
inp2 = input()
step = int(input())

x1,y1 = list(map(int,inp1.split()))
x2,y2 = list(map(int,inp2.split()))

distance = abs(x1 - x2) + abs(y1 - y2)

if (step % 2 == 0 and distance % 2 == 0) or (step % 2 != 0 and distance % 2 != 0):
    print('Y')
else:
    print('N')


write command(note) for Junior 2017 J1,J2,J3

Seeking = a + aa + aaa + aaaa + aa ... the value of a, where a is a number. 
For example, 2 + 22 + 222 + 2222 + 22222 (5 numbers are added together at this time), and the addition of several numbers is controlled by the keyboard.

2
2
2 + 22


inp1 = input()
num = int(input())

sum = 0
for i in range(1,num+1):
    # print(int(inp1 * i))
    sum += int(inp1 * i)
print(sum)

using while loop to do it again
2
4

1
2
3
4

using while loop to print 1 2 3 4

"""
inp1 = input()
num = int(input())
i = 0
sum = 0
while i < num:

    i += 1
    sum += int(inp1 * i)

print(sum)
    