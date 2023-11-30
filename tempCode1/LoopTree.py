class Node:
    def __init__(self,val):
        self.val = val
        self.next = []


def next(n):
    if n.next == []:
        return
    while len(n.next) != 0:

        b = n.next.pop()
        print(b.val)
        next(b)

def printNext(n):
    print(n.val)
    if n.next:
        for i in n.next:
            printNext(i)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next.append(b)
a.next.append(c)
a.next.append(d)
e = Node(5)
f = Node(6)
b.next.append(e)
b.next.append(f)

#next(a)
# printNext(a)

def BFS(root):
    queue = []
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        for i in temp.next:
            queue.append(i)
        print(temp.val)
BFS(a)