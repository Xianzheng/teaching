
def isPal(string:str) -> bool:
    reversedStr = ''
    
    for i in range(len(string) -1, -1, -1):
        reversedStr += string[i]
    
    if reversedStr == string:
        return True
    else:
        return False

#print(isPal('abc'))# False
print(isPal('abccba'))# True

# print(isPal('abc'))

'''
homework:
#print 100 98 96 ... 0 use range
#string = 'markfang' print g a r m
# write isPal

'''