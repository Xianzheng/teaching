"""
# 1. Making 'ABCDE' TO 'EABCD

string = 'ABCDE' 

lst = list(string)


# kick  the last element out of list
popedElement = lst.pop()


lst.insert(0,popedElement)

string = ''.join(lst)
print(string)






def moveString(string):
    '''
        make a list collect all possible cyclic shift
        and return this list
    '''
    totalPossible = []

    for i in range(5):

        lst = list(string)


        # kick  the last element out of list
        popedElement = lst.pop()


        lst.insert(0,popedElement)

        string = ''.join(lst)

        totalPossible.append(string)
        
    return totalPossible
    
    

    # return string

# practice implement function moveString()
print(moveString('ABCDE')) # ['EABCD' ,'DEABC','CDEAB','BCDEA','ABCDE']
"""

string = 'Hello Mark Mark' # change Hello Pascal

#index    0123456789

lst = list(string)

lst[6:10] = 'Pascal'

string = ''.join(lst)

print(string)

'''
string = 'AB' # B -> AA, AB -> BB

def change(string):
    pass
    
print(change('AB')) => ['AAA'.'BB']
'''

'''
HW:
1.

replace:

string = 'Mark Fang'

rotateStrintBack(string) =》 'ark FangM','rk FangMa' ....

get all possible change

2. string = 'Hi Justin Justin Kevin'

change first 'Justin' to 'Mark' string will be Hi Mark Justin Kevin'

change second 'Justin' to 'Pascal'string will be Hi Justin Pascal Kevin'
'''

