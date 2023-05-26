#Determine how many prime numbers are between 101-200, and output all prime numbers.
'''
for i in range(101,200):
    if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0 and i%13 != 0:
        print(i)
        sum+=1

print(sum)

sum = 0
for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
        sum += 1
print('there is ',sum,'prime number')



def fun1():
    pass
#class
# in class we have attributes , method
class Account:
    name = ''
    balance = 0

    def saveMoney(self,money):
        self.balance += money

    def withdraw(self,money):
        self.balance -= money



kevinAccount = Account()
kevinAccount.name = 'Kevin'

justinAccount = Account()
justinAccount.name = 'Justin'

justinAccount.saveMoney(100)
kevinAccount.saveMoney(100)

print(justinAccount.balance)
print(kevinAccount.balance)

justinAccount.withdraw(80)
kevinAccount.withdraw(20)

print(justinAccount.balance)
print(kevinAccount.balance)

'''












