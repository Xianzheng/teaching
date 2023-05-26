'''
string = input()

counthappy = 0
countissad = 0

for i in range(len(string)):
    target = string[i:i+3]
    if target == ':-)':
        counthappy += 1
    if target == ':-(':
        countissad += 1

if counthappy == 0 and countissad == 0:
    print("none")
elif counthappy == countissad:
    print("unsure")
elif counthappy > countissad:
    print("happy")
else:
    print("sad")
'''
string = '9 +'
string1 = "12 A"

lst = string1.split(' ')
print(lst[0],type(lst[0]))
print(lst[1])
times = int(lst[0])
charac = lst[1]
print(times * charac)