'''
class Dog:

    name = ''
    age = 0

# instance of class Dog
dog1 = Dog()
dog1.name = 'Pet'
dog1.age = 5

dog2 = Dog()
dog1.name = 'Bobi'
dog1.age = 6


# magic methoc

class Dog():

    def __init__(self):
        print('one of Dog instance was created')

class Dog():

    # class parameters
    
    #class method
    def __init__(self,name,age):
        
        self.name = name

        self.age = age

dog1 = Dog('Pet',6)
dog2 = Dog('Bobi',7)

print(dog1.name)
print(dog2.name)



class DigitAccount():

    def __init__(self,holderName):

        self.holderName = holderName
        # __account right now is a private attribute
        self.__account = 0

    def deposit(self, amount):

        self.__account += amount

    def remove(self, amount):
        self.__account -= amount

    def showAccount(self):
        return self.__account

a = DigitAccount('xiaoming')
b = DigitAccount('xiaohong')

a.deposit(50)
print(a.showAccount())

a.remove(25)
print(a.showAccount())

1. AA → AB
2. AB → BB
3. B → AA

AA
'''

class Node():
    def __init__(self,val):
        self.val = val

        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n5
n4.next = n5

def printList(head):
    print(head.val)
    if head.next == None:
        return
    else:
        printList(head.next)


def makeList(lst):
    '''
    parameters : [1,2,3,4,5]

    make a node list: node1 -> node2 -> node3 -> node4 -> node5

    return nodeList's Head
    '''
    for index in range(len(lst) - 1):

        currVal = lst[index]
        currNode = Node(currVal)
        nextVal = lst[index + 1]
        nextNode = Node(nextVal)
        currNode.next = nextNode

printList(makeList(1,2,3,4,5)) # 1 2 3 4 5

printList(makeList(1,2,3)) # 1 2 3



