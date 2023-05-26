'''
4
1212111
222111qq
qqqqwwwweee
888666777666
'''

lst = []
def dealoneString(string):
    length = len(string)
    # print(length)
    num = 1
    for i in range(length - 1):
        if string[i] == string[i+1]:
            num += 1

        else:
            print(num,end = ' ')
            print(string[i],end = ' ')
            num = 1
        
        if i == length - 2:
            print(num, end =' ')
            print(string[i])

num = int(input())
for i in range(num):#lloop will run 4 time
    lst.append(input())

for string in lst:
    dealoneString(string)
   