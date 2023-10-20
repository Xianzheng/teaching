CELL_RADIUS = 1

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x,self.y)
    
    def copy(self):
        return Cell(self.x,self.y)
    
    def update(self,direction):

        if direction == 'U':
            self.y -= CELL_RADIUS * 2
        
        if direction == 'L':

            self.x -= CELL_RADIUS * 2

        if direction == 'D':
            self.y += CELL_RADIUS * 2

        if direction == 'R':
            self.x + CELL_RADIUS * 2 

    def __str__(self):
        return 'x:'+str(self.x) +', y:'+ str(self.y)
    

# cell = Cell(50,50)
# print(cell)
# cell.update('U')
# print(cell)
# cell.update('L')
# print(cell)

lst = [Cell(50,50),Cell(48,50),Cell(46,50)]

# copy head
# pop the last element of tail
# update head
# insert updated head to first index
for i in lst:
    print(i,end=' ')
print()
head = lst[0]
lst.pop()
head.update('L')
lst.insert(0,head)
for i in lst:
    print(i,end=' ')

# hw
# lst = []
# apend 'A','B','C','D'
# let it move
# 'B','C','D','A'
# 'C','D','A','B'

# consider the game of airwar
# consider control move direction
# press 'W','A','S',''D move up,LEFT,DOWN,RIGHT
