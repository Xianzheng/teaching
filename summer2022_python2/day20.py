# string = '+++===!!!!' # 3 + 3 = 4 !

string = '3.1415555' # 1 3 1 . 1 1 1 4 1 1 4 5

#undo ctrl + z
#copy ctrl + c paste ctrl + v
# algorithm
# print(string.count('+'))
# print(string.count('='))
# print(string.count('!'))

length = len(string)
# print(length)
num = 1
for i in range(length - 1):
    if string[i] == string[i+1]:
        num += 1

    else:
        print(num,end = ' ')
        print(string[i],end = ' ')
        num = 1
    
    if i == length - 2:
        print(num, end =' ')
        print(string[i])