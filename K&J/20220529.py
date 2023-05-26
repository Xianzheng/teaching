'''
time=[0,0]
#print(time)
for i in range(61):
    time[1]=i

    if i ==60:
        time[1]=0
        time[0]+=1
    print(time)
'''

hr = 12
min = 0
count = 0

for i in range(int(input())):
    min += 1

    if min == 60:
        min -= 60
        hr += 1

    if hr > 12:
        hr -= 12

    strhr = str(hr)

    if min < 10:
        strmin = str(0) + str(min)
    else:
        strmin = str(min)

    time = strhr + strmin

    if len(time) == 4:
        if int(time[3]) - int(time[2]) == int(time[2]) - int(time[1]) and int(time[2]) - int(time[1]) == int(
                time[1]) - int(time[0]):
            count += 1
    if len(time) == 3:
        if int(time[2]) - int(time[1]) == int(time[1]) - int(time[0]):
            count += 1

print(count)

# CCC 2016

