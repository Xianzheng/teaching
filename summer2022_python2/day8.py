'''
string = 'beautafulday'
#index    0123456789
# use to access each character

print(string.replace('beautiful','great'))

# slicing

print(string[4:7])
'''

string = 'beaaheaerea'

print(string.count('ea'))

count = 0

for i in range(len(string)):
    target = string[i:i+2]
    if target == 'ea':
        count += 1

print(count)

