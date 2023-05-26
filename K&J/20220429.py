class Node:
    def __init__(self,num):
        self.data = num
        self.next = ''

    def addNode(self,num):
        while self.next:
            self = self.next

        newNode = Node(num)
        self.next = newNode

    def loopPrint(self):
        while self.next:
            print(self.data)
            self = self.next
        print(self.data)

    def update(self, num, num1):
        while self.next:
            self = self.next
            if self.data == num:
                self.data = num1

    def delete(self,num):
        while self.next:
            self = self.next
            if self.data == num - 1:
                self.next = self.next.next


root = Node(1)

for i in range(2,11):
    root.addNode(i)


# root.next.next = root.next.next.next
# node2 = root.next
#
# node4 = node2.next.next
#
# node2.next = node4
root.delete(3)

root.loopPrint()

#  write update method : not change data of node, change node's next

#  add new node