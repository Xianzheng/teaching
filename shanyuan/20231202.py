dic = {
    'AA' : 'AB',
    'AB' :'BB',
    'B' :'AA'
}

def allPossibleSlice(string):
    all = []
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            all.append([string[i:j],(i,j)])
    return all


# print(allPossibleSlice('AB')) # [['A',(0,1)],['B',(1,2)],['AB',(0:2)]]

def parse(string):
    lst = allPossibleSlice(string)
    possibleChange = []
    for item in lst:
        if change(string,item) != None:
            possibleChange.append(change(string,item))
    return possibleChange

def change(string,lst):
    '''
    receive all possible slice and it position 

    return changd string
    '''
    if lst[0] in dic:
        lstring = list(string)
        lstring[lst[1][0]:lst[1][1]] = dic[lst[0]]
        return ''.join(lstring)
    else: return None
        


# print(parse('BB')) # [BB,AAA]

class Node:

    def __init__(self,value):
        self.value = value
        self.next = []
        self.level = 0
        

n1 = Node('Device')

n2 = Node('Apple')
n3 = Node('Sumsong')
n4 = Node('Xiaomi')

n5 = Node('Ipad')
n6 = Node('Iphone')
n7 = Node('Itouch')

n8 = Node('NodePhone')
n9 = Node('SumsongTv')

n10 = Node('Xiaomi14')



n1.next.append(n2)
n1.next.append(n3)
n1.next.append(n4)

n2.next.append(n5)
n2.next.append(n6)
n2.next.append(n7)

n3.next.append(n8)
n3.next.append(n9)

n4.next.append(n10)

# how to loop this tree

#BFS, DFS
# lst = [1]
# n = lst.pop(0)
# print(n)
# lst.append(2)
# lst.append(3)
# n = lst.pop(0)
# print(n)
# n = lst.pop(0)
# print(n)


def BFS(root):

    queue = []
    queue.append(root)

    while queue:

        tempNode = queue.pop(0)

        for i in tempNode.next:
            
            queue.append(i)

        print(tempNode.value)


def printTree(root):

    
    if root.next == []:
        return
    
    while len(root.next) != 0:

        b = root.next.pop(0)
        print(b.value)
        printTree(b)

printTree(n1)

# root = Node('AB')
# for i in parse('AB'):
#     root.next.append(Node(i))

# queue = []

# queue.append(root)

# while queue:
#     tempNode = queue.pop(0)
#     for i in parse(tempNode.value):
#         tempNode.next.append(Node(i))
#     for i in tempNode.next:
#         queue.append(i)
#     print(tempNode.value)
#     if tempNode.value == 'AAAA':
#         break
    

'''
according to img

build tree1, tree2,tree3

tree1, tree3 do loop all leaf use BFS, DFS

loop all leaf tree4 get value sum of all leaf.
'''
