# we already draw snake

# right now we need to consider how to move

# lst = ['A','B','C']

# head = lst[0]

# print(lst)
# print(head)
# lst.insert(0,head)
# print(lst)
# lst.pop()
# print(lst)
CELL_RADIUS = 20
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def to_tuple(self):
        return (self.x,self.y)
    
    def copy(self):
        return Cell(self.x,self.y)
    
    def move(self, direction):
        if direction == 'U':
            self.y -= CELL_RADIUS * 2
        if direction == 'L':
            self.x -= CELL_RADIUS * 2


lst= [Cell(100,200)]
head = lst[0].copy()
lst.pop()
head.move('U')
lst.insert(0,head)
print(lst[0].to_tuple())

head = lst[0].copy()
lst.pop()
head.move('P')
lst.insert(0,head)
print(lst[0].to_tuple()) # will get (140,160)


#  print pattern in screen

'''
hw:
(* represent Cell)
1.
****
   *

2.
***
*
*
3.
*
*
*

continue build on method
it also can move down and  right

'''
    
