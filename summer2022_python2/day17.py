'''
*
**
***
****

****
***~
**
*

# use nested loop to print
for i in range(1,5): # it control how many lines
    
    for j in range(i): # it will control how many time to run in eachline

        print('*', end= ' ')

    print()

lst1 = ['Mark','Kevin','Jack']

lst2 = ['white','black','red']

# it will print
# Mark likes white
# Mark likes black
# Mark likes red

for name in lst1:
    for color in lst2:
        print(name,'likes',color)

# 9 * 9 form

1 * 1 = 1

'''
'''
use nested loop to print
1x1=1    
1x2=2    2x2=4    
1x3=3    2x3=6    3x3=9    
1x4=4    2x4=8    3x4=12    4x4=16    
1x5=5    2x5=10    3x5=15    4x5=20    5x5=25    
1x6=6    2x6=12    3x6=18    4x6=24    5x6=30    6x6=36    
1x7=7    2x7=14    3x7=21    4x7=28    5x7=35    6x7=42    7x7=49    
1x8=8    2x8=16    3x8=24    4x8=32    5x8=40    6x8=48    7x8=56    8x8=64    
1x9=9    2x9=18    3x9=27    4x9=36    5x9=45    6x9=54    7x9=63    8x9=72    9x9=81

you can refer to 

1
1 2
1 2 3
1 2 3 4

for i in range(1,5):
    
    for j in range(1, i+1):

        print(j, end= ' ')

    print()
'''
r = range(1,5)# [1,2,3,4,5]

print(list(r))