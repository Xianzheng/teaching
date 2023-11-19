

'''

print('index 0 of str1 and str2')

print(str1[0])

print(str2[0])

print('index 1 of str1 and str2')

print(str1[1])

print(str2[1])

print('index 2 of str1 and str2')

print(str1[2])

print(str2[2])

print('index 3 of str1 and str2')

print(str1[3])

print(str2[3])

print('index 4 of str1 and str2')

print(str1[4])

print(str2[4])

'''
num = int(input())

str1 = input()

str2 = input()

count = 0
for index in range(num):
    
    # print('index', index ,'of str1 and str2')

    # print(str1[index])

    # print(str2[index])
    if str1[index] == str2[index] == 'C':

        count += 1

print(count)
