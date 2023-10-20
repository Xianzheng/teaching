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
        # 'U' -> MOVE UP
        # 'L' -> MOVE LEFT
        # 'R' -> MOVE RIGHT
        # 'D' -> MOVE DOWN
        if direction == 'U':
            self.y -= CELL_RADIUS * 2
        if direction == 'D':
            self.y += CELL_RADIUS * 2
        if direction == 'R':
            self.x += CELL_RADIUS * 2
        if direction == 'L':
            self.x -= CELL_RADIUS * 2
        
    

body = [Cell(60,100),Cell(100,100),Cell(140,100)]

for cell in body:
    print(cell.to_tuple())

head = body[0].copy()
body.pop()
head.move('U')
body.insert(0,head)

print('After move up')

for cell in body:
    print(cell.to_tuple())



# move left