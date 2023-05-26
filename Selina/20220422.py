class Account:
    def __init__(self,name):
        self.__accountHolder = name         #   accountHolder is a public attribute
        self.__cashAccount = 0            #__cashAccount make cashAccount attribute to private attribute

    def saveMoney(self,num):
        if num > 0:
            self.__cashAccount += num
            print('you saved ', num)
        else:
            print('your can not save that money')

    def withDraw(self,num):
        if num > 0 and num <= self.__cashAccount:
            self.__cashAccount -= num
        else:
            print('you can not withdraw that money')
    def getCashAccount(self):
        return self.__cashAccount

    def getAccountHolder(self):
        return self.__accountHolder

# private attribute: we only can access attribute inside in class
# make a instance of Account
AC = Account('Mark')
#
# AC.cashAccount # access the attribute of Account Class
# AC.__ashAccount += -100# you save negative account money
# print(AC.__cashAccount)
print(AC.getAccountHolder())
AC.saveMoney(100)
AC.withDraw(50)
print(AC.getCashAccount())

# base on your understanding
# what is class attribute
# what is class method
# how to make class attribute private
# why we need to makr class attribute private
#(rewrite this class)
