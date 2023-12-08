'''
def getbigger(arg1, arg2):
    if arg1 < arg2:
        return arg2
    elif arg1 > arg2:
        return arg1
    else:
        return arg1 or arg2
print(getbigger(10,20))

print(getbigger(3,4))

print(getbigger(3,3))


def getsequence(arg1, arg2):
    for i in range(arg1, arg2 + 1):
        print(i)

getsequence(10,20) # it will print 10 to 20 
getsequence(1,10) # it will print 1 to 10 



# def getsequence(arg1, arg2):
#     for i in range(arg1, arg2 + 1):
#         print(getsequence(10, 20))
#         print(getsequence(1, 10))


# use recursive how to print 1 to 10


def rPrint(n):
    print(n)
    if n == 10:
        return
    rPrint(n + 1)

rPrint(1)

'''
inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()

str1 = inp1
lst1 = str1.split()
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])

str2 = inp2
lst2 = str2.split()
for i in range(len(lst2)):
    lst2[i] = int(lst2[i])

str3 = inp3
lst3 = str3.split()
for i in range(len(lst3)):
    lst3[i] = int(lst3[i])

str4 = inp4
lst4 = str4.split()
for i in range(len(lst4)):
    lst4[i] = int(lst4[i])


print(lst1)
print(lst2)
print(lst3)
print(lst4)

'''
hw:
find out each rows's sum and each columns sum is equal:
make CCC 2016 J2 
'''