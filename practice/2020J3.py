num = int(input())
xlst = []
ylst = []
for i in range(num):

    xStr, yStr = input().split(',')
    xInt, yInt = int(xStr), int(yStr)
    xlst.append(xInt)
    ylst.append(yInt)

print(xlst)
print(ylst)
# h1
# find min value of xlst - 1,find min value of ylst - 1
# find max value of xlst + 1,find max value of ylst + 1

# h2
# write comment for aircraft, point on how we can get collide