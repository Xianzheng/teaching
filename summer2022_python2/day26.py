#
lst = [6,7,1,7,3,9] # from smallest to biggest

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]

print(lst)

#[6,7,1,7,3,9]
#[1,3,6,7,7,9]



# python bubble sort

# https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf