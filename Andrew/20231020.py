#body is a lst
body = [1,2,3,4,5,6] # we want to add 1 to all item, [2,3,4,5,6,7]
#index  0 1 2 3 4 5

# if we want to change list, we must use index
for i in range(len(body)):
    body[i] += 1

print(body)

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # def __str__(self):

    #     return '({},{})'.format(str(self.x),str(self.y))

    def __repr__(self):
        return str((self.x,self.y))

# Cell(10,0) is in instance of Cell

# a = Cell(10,0)
# b = Cell(20,0)

# print(a.x)
# print(b.x)
# body = [Cell(10,0),Cell(20,0),Cell(30,0),Cell(40,0)]

slots = [Cell(10,0), Cell(20, 0), Cell(30,0), Cell(40, 0), Cell(50, 0), Cell(10, 10), Cell(20, 10), Cell(30, 10), Cell(40, 10), Cell(50,10)]

for i in range(len(slots)):
    slots[i].y += 10
print(slots)

# :, -> is comment in code for people to read
# : is expected arument type, -> return type

def add(a:int,b:int) :
    # defense measure
    if (type(a) != type(int) ):
        return 'this is not expected argument'
    
    return a + b

print(add(1 , 2))   
class Triangle():
    def __init__(self, base, height) -> None:
        pass

# home make a triangle class, triangle should have base , height as parameter,
# purpose in a street, we have five triangle, base number, and height number is up to you
# you need to sume all triangle 's area in a street.

# try to do CCC2019 question, J2 
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
