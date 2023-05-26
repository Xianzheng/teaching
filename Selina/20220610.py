'''
string = 'Selina'
#         012345
#use two method

# for eachChar in string:
#     print(eachChar)

for eachCharIndex in range(0,6):
    print(eachCharIndex)


string = 'S e l i n a M a r k'
#         012345678910

for eachCharIndex in range(0,len(string),2):
    print(eachCharIndex, string[eachCharIndex])

print('the length of string is',len(string))
# range(start, stopby, step)
# len(sequence) -> get the length of sequence
'''
# function



def getEvenIndexCharaters(str1):
    """
    :param str1:
    :print all characters of even index
    """
    for eachCharIndex in range(0, len(str1), 2):
        print(eachCharIndex, str1[eachCharIndex])


string = 'S e l i n a M a r k'
string1 = 'H e l l o , I t i s a g o o d d a y '
getEvenIndexCharaters(string1)


homeworkString = ' T H I S I S H O M E W O R K'
# step1: print all characters of homeworkString
# step2: use for loop to print all characters of homeworkString
# step3: make a function to do it