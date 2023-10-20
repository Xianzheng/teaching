
inp = input()

# '3 10 12 5' => ['3','10','12','5'] => [3,10,12,5]

lst = inp.split()

# convert all element from lst to int
# for i in range(len(lst)):
#     lst[i] = int(lst[i])

lst = list(map(int,lst))

print(lst)

# [3, 10, 12, 5] => [0, 3, 13, 25, 30]

result = [0]
sum = 0
for i in lst:
    sum += i
    result.append(sum)

print(result)

'''
hw:
1 . try to finish 2018 problem J3

2 . DO 2016 PROBLEM J2
https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
'''