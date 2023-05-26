'''
string = 'hello world'

#index    012345678910

print(string[6])#w

print(string[10])#d
'''
# input
num = int(input())
today = input()
yesterday = input()
answer = 0
for i in range(num):
    if today[i] == yesterday[i] == 'C':
        answer += 1
print(answer)
