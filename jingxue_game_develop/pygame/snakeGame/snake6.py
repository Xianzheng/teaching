import pygame
# pip install pygame
# global variable
SCREEN_SIZE = (1200,800)
WHITE = (255,255,255)
GREEN = (0,128,0)
SNAKE_COLOR = (0,0,0)
CELL_RADIUS = 20

#游戏的刷新
UPDATE = pygame.USEREVENT + 1

def init_game():
    pygame.init()
    pygame.display.set_caption('Snake game')
    pygame.time.set_timer(UPDATE,200) # 200 will indicate the speed of snake


def monitorKeyPress():
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_UP] and game.snake.direction != 'D':
        game.snake.direction = 'U'
    
    if pressed_key[pygame.K_LEFT] and game.snake.direction != 'R':

        game.snake.direction = 'L'

    if pressed_key[pygame.K_RIGHT]  and game.snake.direction != 'L':
        game.snake.direction = 'R'
    
    if pressed_key[pygame.K_DOWN] and game.snake.direction != 'U' :

        game.snake.direction = 'D'
#(*)  这个方法用来检测 屏幕按钮或键盘按键被按下

def is_snake_food_collide1():
    # fx: game.food[0], fy: game.food[1]
    # x: game.snake.body[0].x, y:game.snake.body[0].y
    if game.snake.body[0].x - game.food[0] == 0 and game.snake.body[0].y - game.food[1] == 0:
        return True
    else:
        return False

def is_snake_food_collide():
    # fx: game.food[0], fy: game.food[1]
    # x: game.snake.body[0].x, y:game.snake.body[0].y
    head = game.snake.body[0].copy()
    head.update(game.snake.direction)
    return (game.food[0] - head.x) == 0 and (game.food[1] - head.y) == 0

def if_eatFood():
    # if food is not Not and is_snake_food_collide
    if game.food is not None and is_snake_food_collide():
        # print('got it')
        #make a cell , and its position is (x, y) is food's x position and y position
        cell = Cell(game.food[0],game.food[1])
        #let snake add a Cell, and this cell is snake's head
        game.snake.body.insert(0,cell)

        #reset food
        game.food = None
        
def if_lose():
    head = game.snake.body[0]  
    '''
    over left or right game over
    '''
    if head.x <= 0 + CELL_RADIUS or head.x >= SCREEN_SIZE[0] - CELL_RADIUS * 2:
        print('over left or right,game over')
        game.running = False
    '''
    over top or bottom , game over
    '''

    if head.y <= 0 +CELL_RADIUS or head.y >= SCREEN_SIZE[1] - CELL_RADIUS * 2:
        print('over top or bottom,game over')
        game.running = False
    
    '''
    touch snake's body, game over
    '''
    if head.to_tuple() in [cell.to_tuple() for cell in game.snake.body[1:]]:
        game.running = False

    


        
def update():


    monitorKeyPress()

    if_eatFood()

    if_lose()

    # pygame will moniter if we enter some key, expecially quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
    
        if event.type == UPDATE:
            game.snake.update()

        if event.type == UPDATE:
            generateFood()

# 画出蛇中每一个细胞到屏幕上
def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,game.snake.color,
                           cell.to_tuple(),
                           game.snake.cell_size)

def draw_food():
    if game.food is not None:
        pygame.draw.circle(game.screen,GREEN,game.food,CELL_RADIUS)

def generateFood():
    import random
    while game.food is None:

        foodSize = CELL_RADIUS * 2
        randX = random.randrange(foodSize ,SCREEN_SIZE[0],foodSize)
        randY = random.randrange(foodSize,SCREEN_SIZE[1],foodSize)

        game.food = (randX,randY)




def draw():
    game.screen.fill(WHITE)
    draw_snake()
    draw_food()
    #不断刷新我们的界面
    pygame.display.flip()

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()
        self.food = None

class Cell:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def to_tuple(self):
        return (self.x,self.y)
    
    def copy(self):
        return Cell(self.x,self.y)
    
    def update(self, direction):
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

class Snake:

    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = SCREEN_SIZE[0] // 2
        y = SCREEN_SIZE[1] // 2
        # determine the size of each Cell
        self.direction = 'U'
        self.body  = [Cell(x,y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR 

    def update(self):
        #copy snake's Head
        head = self.body[0].copy()
        #pop out snake's tail
        self.body.pop()
        #head should update follow direction
        head.update(self.direction)
        #insert updated head to body first position
        self.body.insert(0,head)

if __name__ == '__main__':
    # 初始化我们的pygame,并且给屏幕一个标题
    init_game()
    # 创建 game类 的一个实体，这个实体主要控制这个游戏的流程
    game = Game()
    #在class game 有一个attribute running， if running is True,游戏运行， else 游戏结束
    while game.running == True:
        # 给我们游戏屏幕画一个颜色
        draw()
        update()
    
    #退出我们的游戏
    
    pygame.quit()

'''
next class:

use keyboard to control dot moving

hw:

read whole code:
display the confusion part

and write in txt file

we will explain in next class


'''