'''
count = 1
lst = []
for i in range(int(input())):
    string = input()
    length = len(string)
    
    for i in range(length - 1):
        if string[i] == string[i+1]:
            count += 1
        if string[i] != string[i+1]:
            lst.append(count)
            lst.append(string[i]) # end=''
            count = 1
        if i == length - 2:
            
            lst.append(count)
            lst.append(string[i + 1])
            lst.append('end')
            count = 1
for i in lst:
    if i != 'end':
        print(i, end=' ')
    if i == 'end':
        print()

# shift + ctrl/command + ~ 
'''
# for i in range(5):
#     for j in range(5):
#         print(i)

#  There are four numbers: 1, 2, 3, 4.
#  How many different three-digit numbers can be formed without repeated numbers?
#  What is each?
# for hundred in range(4):
#     for ten in range(4):
#         for one in range(4):
#             print(str(hundred+1)+str(ten+1)+str(one+1))

count = 0
for i in range(1,5): # range(start,stopby,adding)
    for j in range(1,5): 
        for z in range(1,5): 
            if i != j and j != z and i != z:
                count += 1
                print(i,j,z)
print('there are ',count,' different three-digit numbers without repeated numbers')

'''
hw:
1.
Determine how many prime numbers are between 101-200, 
and output all prime numbers.
(using nested loop)

2.
Output 9 * 9 multiplication formula table.

'''

'''
1x1=1    
1x2=2    2x2=4    
1x3=3    2x3=6    3x3=9    
1x4=4    2x4=8    3x4=12    4x4=16    
1x5=5    2x5=10    3x5=15    4x5=20    5x5=25    
1x6=6    2x6=12    3x6=18    4x6=24    5x6=30    6x6=36    
1x7=7    2x7=14    3x7=21    4x7=28    5x7=35    6x7=42    7x7=49    
1x8=8    2x8=16    3x8=24    4x8=32    5x8=40    6x8=48    7x8=56    8x8=64    
1x9=9    2x9=18    3x9=27    4x9=36    5x9=45    6x9=54    7x9=63    8x9=72    9x9=81
'''

# print(1,'*',1,'=',1)

# print('{} * {} = {}'.format(1,1,1))

for i in range(1,10):
    for j in range(1,i + 1):
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print()