# input 3 10 12 5 -> 0 3 13 25 30

# input 3 10 12 5 -> [3, 10, 12, 5]

string = input()


lst = string.split() # the method split will put all characters in list but there are string

# numlst = list(map(int,lst)) # convert all string element to int element

# print(numlst)

# numlst = list(map(int,input().split()))
# print(numlst)

print(lst)

for i in range(len(lst)): # i will be each index of lst
    lst[i] = int(lst[i]) # if we want to update list we must use index to update
print(lst)

#[3,10,12,5] =>  [0,3,13,25,30]

'''
future print
0 3 13 25 30
3 0 10 22 27
13 10 0 12 17
25 22 12 0 5
30 27 17 5 0
'''