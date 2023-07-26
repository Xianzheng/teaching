'''
N = int(input())
yesterday_parking = input()
today_parking = input()

occupied = 0
for i in range(N):
    if yesterday_parking[i] == 'C' and today_parking[i] == 'C':
        occupied += 1

print(occupied)
'''
s = '3.1415555'
#in  0123456789
# print(s[0] == s[1])
# print(s[1] == s[2])
# print(s[2]==s[3])
# #we can create a loop, and go through s
#judge s[i], s[i + 1], if equal do some thing, if not equal do something, if it reaches to end to something
count = 1

def output(s):
    #print count
    print(count,end=" ")
    #print sign
    print(s[i],end=" ")


for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1

    if s[i] != s[i+1]:
        #print count
        output(s)
        # reinitialize count
        count = 1
        
    if i == len(s) - 2:
        output(s)

'''

# do full step of CCC 2019 J2

INPUT:
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555

OUTPUT
3 + 3 = 4 !
6 7 6 . 12 T
1 ( 2 A 2 B 1 C 1 )
1 3 1 . 1 1 1 4 1 1 4 5

'''

