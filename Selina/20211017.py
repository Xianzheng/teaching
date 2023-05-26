
def function_name(): # no argument
    print('Hello World')
    return 100

#print(function_name()) # print function actually is print return value

def get_length(string):
    # functionality: get the length of string
    # expect passing argument is string
    # return value is the length of string
    num = 0
    for i in string:
        num += 1
    return num


string1 = 'abcd'
string2 = 'it is a good day'
string3 = 'it is not bad'
# print(get_length(string1)) # expect 4
# print(get_length(string2)) # expect 16
# print(get_length(string3)) # expect 13

#1.  get_max implementing the function, the function eventually returns the maximum value of the list lst

def get_max(lst):
    # functionality: get the max value of lst
    # expect passing argument is a list
    # return value is the max value of lst
    # print(lst)
    max = 0
    for i in lst:
        if max < i:
            max = i
    return max


a = get_max([2,9,2,6])
b = get_max([1,2,3,4,5,6,7,8])
# print(a) # it will get 9
# print(b)

def getSpaceNum(string):
    # functionality: get how many space in string
    # expect passing argument is a string
    # return value is space number of string
    #print(string)

    spaceNum = 0
    for i in string:
        if i.isspace():
            spaceNum += 1

    return spaceNum

print(getSpaceNum('Hi I am Mark')) # 3
print(getSpaceNum('There is Selina')) # 2
print(getSpaceNum('Beautiful')) # 0

# implements function getSpact Num

# homework

dic = {'Chinese':94,'English':96,'Math':98}

def getHignScoreSubject(dic):
    #functionality: get the highest scores course Name
    #passing argument is dictionary
    #return a string which is highest scores course Name
    pass

print(getHignScoreSubject(dic)) # 'Math'

