# 2x + 3y = 10
# 3x + 2y = 15
# x, y = ?
# change path cd 

def solveMathQuestion():
    for x in range(0,101):
        for y in range(0,101):
            if 2*x + 3*y == 10 and 3*x + 2*y == 15:
                return x,y
