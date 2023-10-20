from getNext import *

class Node:
    def __init__(self,data):
        self.data = data
        self.childrean = []
        self.parent = None
        self.level = 0

    def addChild(self,node):
        node.parent = self
        self.childrean.append(node)

    def printTree(self):
        print(self.data)
        if self.childrean:
            for i in self.childrean:
                i.printTree()

def addChildrean(parentNode,level):
    for i in nextLevel(parentNode.data):
        childNode = Node(i)
        childNode.level = parentNode.level + 1
        parentNode.addChild(childNode)

    if parentNode.level < level-1:
        lst = parentNode.childrean
        for i in lst:
            addChildrean(i,level)

def getResult(node,expect):
    if node.data == expect:
        print(node.data,node.level)
        while node.parent:
            node = node.parent
            print(node.data,node.level)
        print()
        return

    if node.childrean:
        lst = node.childrean
        for i in lst:
            getResult(i,expect)


root = Node('AB')
addChildrean(root,2)
#getResult(root,'AAAB')
root.printTree()
# root = Node('Electronic')
#
# node1 = Node('Apple')
# node2 = Node('Samsung')
# node3 = Node('Xiaomi')
#
# root.addChild(node1)
# root.addChild(node2)
# root.addChild(node3)
#
# root.printTree()
