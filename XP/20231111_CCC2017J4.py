"""
string1 = 'apple'
string2 = 'banana'
result = string1 + string2
print(result)


str1 = '0'
str2 = '1'
print(str1 + str2)

int1 = 0
int2 = 1
print(str(int1) + str(int2))


# simulate clock working
'''
# practice use a loop to show 00 - 20
min:
00
01
02
03
04
05
06
07
08
09
10
'
.
.
20
'''
"""
hrPointer = 12
minPointer = 0
count = 0
for k in range(0,int(input()) + 1):

    
    # if minPointer >= 60 minPointer it will restart to 0 , hrPointer will add 1
    if minPointer >= 60:
        minPointer = 0
        hrPointer += 1

     # if hrPointer >= 13 hrPointer it will restart to 1
    if hrPointer >= 13:
        hrPointer -= 12

    if minPointer < 10:
        strMinPointer = str(0) + str(minPointer)
    else:
        strMinPointer = str(minPointer)

    minPointer += 1

    strHrPointer = str(hrPointer)
    totalTime = strHrPointer + strMinPointer

    if len(totalTime) == 4:
      if int(totalTime[3]) - int(totalTime[2]) == int(totalTime[2]) - int(totalTime[1]) and int(totalTime[2]) - int(totalTime[1]) == int(totalTime[1]) - int(totalTime[0]):
        count += 1

    if len(totalTime) == 3:
       if int(totalTime[2]) - int(totalTime[1]) == int(totalTime[1]) - int(totalTime[0]):
          count += 1

    # print(totalTime)

print(count)

# practice: if minPointer >= 60, minPointwe will restart from 0 and hrPointer will add 1


'''
hw:

1. write comment for CCC 2017 j4 for each line and see if you understand every thing

2. try to CCC 2016 J4
Problem J4: Arrival Time
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
'''