class Account:
    def __init__(self,holderName,balance):
        self.holderName = holderName
        self.balance = balance


    # class method
    def deposite(self,coin):
        
        self.balance += coin
        print(self.holderName,'deposite',coin,'coin in Account')

    def withdraw(self,coin):
        
        self.balance -= coin
        print(self.holderName,'withdraw',coin,'coin out Account')

    def showBalance(self):
        print('{} holder balance : {} coin'.format(self.holderName,self.balance))


    

accountA = Account('Jingxue',0)

accountB = Account('Mark',0)

accountA.deposite(10)
accountA.withdraw(5)
# accountA.withdraw(5)
# # print(accountA.balance)
# accountA.showBalance()
# accountB.showBalance()

'''
create a class:

think some thing in your life
add some attribute to instance of class
add some method to instance of class

class Dog:
    # attribute
    # method

dogA = Dog(...)
'''