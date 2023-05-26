from math import ceil

vict = 0

for i in range(6):
    inp = input()
    if inp == 'W':
        vict += 1

dic = {1:3,2:2,3:1}
vict /= 2
vict = ceil(vict)

try:
    print(dic[vict])
except:
    print(-1)

# print(ceil(1.5))
# REDO CCC 2016 J1 BY YOUR UNDERSTANDING