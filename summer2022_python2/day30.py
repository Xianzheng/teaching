def isPal(string:str) -> bool:
    reversedStr = ''
    
    for i in range(len(string) -1, -1, -1):
        reversedStr += string[i]
    
    if reversedStr == string:
        return True
    else:
        return False

# banana
'''
b
ba
ban
bana
banan
banana

a
an
ana ->3
anan
anana -> 5
'''

string = input()

#         01234
# print(string[1:len(string)])
# print(string[0:4])
lst = []
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        slice = string[i:j]
        if isPal(slice):
            lst.append(len(slice))
print(max(lst))
