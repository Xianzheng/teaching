inp1 = input()# string
inp2 = input()
inp3 = input()
inp4 = input()

lst = []

lst1 = list(map(int,inp1.split()))
lst2 = list(map(int,inp2.split()))
lst3 = list(map(int,inp3.split()))
lst4 = list(map(int,inp4.split()))

lst.append(lst1)
lst.append(lst2)
lst.append(lst3)
lst.append(lst4)

resultLst = []
for eachRow in lst:
    resultLst.append(sum(eachRow))

columnLst = [] 

for i in range(4):
    temp = []
    for j in range(4):
        temp.append(lst[j][i])
    columnLst.append(temp)

for eachCol in columnLst:
    resultLst.append(sum(eachCol))

print(resultLst)

# homework
# judge all content in resultLst are same

