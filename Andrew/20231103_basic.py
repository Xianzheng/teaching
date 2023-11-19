'''

pick random number from 1,3,5,7,9,11 geometric sequnce

snake's x will be 40,80,120,160,200 ....
snake's y will be 40,80,120,160,200 ....
'''
import random
 
#print(random.randint(1,10))
for i in range(20):
    print(random.randrange(1,11,2))


class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x,self.y)
    
c = Cell(1,2)

print(c.to_tuple())

# list []
# dictionary {1:2}
# set {1,2}
# tuple (1,2)

# lst = []
# for i in range(1,11):
#     lst.append(i)
# print(lst)

#syntax surgar
lst = [i for i in range(1,11)]
print(lst)