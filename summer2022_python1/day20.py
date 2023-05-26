#12     12 * (10 ** 0)
#120    12 * (10 ** 1)
#1200   12 * (10 ** 2)
#12000  12 * (10 ** 3)

# 12 + 120 + 1200 + 12000
inp1 = int(input())
inp2 = int(input())

s = 0
for num in range(inp2 + 1):

    eachNum = inp1 * (10 ** num)

    s += eachNum

print(s)