# blue print
class Account:

    def __init__(self,hodername,balance):
        # self.balance means balance is public attribute
        # self.__balance means __balance is private attribute
        print(hodername,'\'s account was build')
        self.holdername = hodername
        self.__balance = balance
    
    # build a class method
    def deposite(self,coin):
        if coin <= 0:
            print('you don\'t have enough coin, you can not deposit')
        else:
            print(self.holdername,'deposites',coin,'coins')
            self.__balance += coin

    def withdraw(self,coin):
        if self.__balance >= coin:
            print(self.holdername,'withdraws',coin,'coins')
            self.__balance -=coin
        else:
             print('you don\'t have enough coin, you can not withdraw')
    
    def showBalance(self):
        print(self.holdername,'\'s balance remain',self.__balance)

# dont't repeat your self
# instance
jingxue = Account('Jingxue',0)
stephen = Account('Stephen',0)

stephen.deposite(-500)
stephen.withdraw(500)
stephen.showBalance()


jingxue.deposite(10)
jingxue.withdraw(2)
jingxue.showBalance()

'''
think some example in your real life
make a class and instance to practice 
using private , method
'''