
string = 'Hello Selina'
#index    0123456789
# loop all characters of string

# use two method
'''
for eachChar in string:

    print(eachChar)


print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])
print(string[8])
print(string[9])
print(string[10])
print(string[11])

# use index to access each characters of string

# ? 12345678.... range()

for i in range(0,12):
    print('i =',i,string[i])

'''
def ifContainsSpace(string):
    '''

    if string contains space return True, else return False

    '''
    flag = 0 # 0 represent False, 1 represents True

    for eachChar in string:
        if eachChar == ' ':
            flag = 1

    if flag == 1:
        return True
    else:
        return False

print(ifContainsSpace('mark fang')) # True
print(ifContainsSpace('markfang')) # False

# memorize twe methods to loop string
# try to finish ifContainsPace with out see the demo code