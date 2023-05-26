'''
class Node:
    def __init__(self,id,num):
        self.id = id
        self.data = num
        self.next = ''
        self.previous = ''

    def addNode(self,id,num):
        while self.next:
            self = self.next

        newNode = Node(id,num)
        self.next = newNode
        newNode.previous = self

    def insert(self,position):
        pass


root = Node(0,1)
root.addNode(1,2)
root.addNode(2,3)
root.addNode(3,4)

print(root.next.previous.data)
'''

def sayHello():05
    print('Hello World')

def addingFunc(num1,num2):
    print(num1 + num2)

def multiplyFunc(num1,num2):
    return num1 * num2

sayHello()
addingFunc(1,1)
print(multiplyFunc(3,4))

a = lambda : print('Hello World')
a()

b = lambda num1, num2: print(num1 + num2)
b(1,1)

c = lambda num1, num2: num1 * num2
print(c(3,4))

lst = [1,2,3,4,5,6,7,8,9.10]
def showEvenNumbers(lst):
    newLst = []
    for i in lst:
        if i % 2 == 0:
            newLst.append(i)
    return newLst
print(showEvenNumbers(lst))

print(list(filter(lambda num: num % 2 == 0, lst)))

# implements insert method in class Node
# practice lambda function