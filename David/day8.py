'''
string = 'hello world'

print(type(string))

print(string.split())# if we put nothing it default fill ' '

print(string)
print(string.strip('123')) # remove front and end indicated characters
#print(string.join('Mark'))
lst = ['Mark','Selina','Kevin','David'] # this is a list
# convert list to string
# print(' '.join(lst))
# print Mark Selina Kevin David
string = ''
for i in range(len(lst)):
    string += lst[i]
    if i != len(lst) - 1:
        string += ' '

print('Hello {},Today\'s weather is {}'.format('Mark','good'))
print('Hello {}'.format('Selina'))
print('Hello {}'.format('David'))

string = 'hello mark today is beautiful'
#         0123456
string1 = 'mark'
print(string.index(string1))

a = '1'
print(a.isspace())
print(a.isdecimal())
# ask user to create a password, it must have one lower character, one big character one number,
# the length is bigger than 7

# if it satisfy condition print valid, else not valid


password = input()
if len(password) > 7:
    for i in range(len(password)):
        if password[i].isupper():
            for i in range(len(password)):
                if  password[i].islower():
                    for i in range(len(password)):
                        if password[i].isdecimal():
                            print("valid")
else:
    print("invalid")

if len(password) < 7:
    print("invalid")

flag = 0
password = input()

for i in password:
    if i.isupper():
        flag += 'c'
    if i.islower():
        flag += 'v'
    if i.isdecimal():
        flag += 'b'

if len(password) > 7 and 'c' in flag and 'v' in flag and 'b' in flag:

        print('it is valid')

else:
    print('it is not valid')

print(flag)


# homeword
string = 'Hello I am Mark'


# reverse String base on a giving string
string = 'abcde' #'edcba'
string = 'mark' # 'kram'

# string = 'markfang@live.com'
# if there a special characters in string ( if not lower characters, not big , not space, it is special)


Given string contains a combination of the lower and upper case letters.
Write a program to arrange the characters of a string so that all lowercase letters should come first.

input
str1 = PyNaTive

Output
yaivePNT
'''


