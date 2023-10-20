#change
#enter virtual environment （.\venv\Script\activate）
import pygame

SCREEN_SIZE = [800,800]

WHITE = (255,255,255) #RGB
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,100,0)
CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0) #RGB (0,0,0) represent black

UPDATE = pygame.USEREVENT + 1

FOOD = pygame.USEREVENT + 2

# 1000 / 2 = 500.0
# 1000 // 2 = 500
# 5 / 2 = 2.5
# 5 // 2 = 2

#function
def init_game():
    pygame.init()
    pygame.display.set_caption("Snake game")
    pygame.time.set_timer(UPDATE,200)
    pygame.time.set_timer(FOOD,3000)

# class
class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()
        self.food = None
# def draw_blackDot():
#     pygame.draw.circle(game.screen,BLACK,POSITION,CELL_RADIUS * 2)

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
            self.x += CELL_RADIUS * 2 




class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = SCREEN_SIZE[0] // 2
        # x = 500
        y = SCREEN_SIZE[1] // 2
        # y = 400
        self.direction = 'L'
        self.body = [Cell(x,y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR

    def update(self):
        head = self.body[0].copy()
        self.body.pop()
        head.update(self.direction)
        self.body.insert(0,head)


def draw():
    game.screen.fill(WHITE)
    draw_snake()
    draw_food()
    pygame.display.flip()

def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,
                           game.snake.color,
                           cell.to_tuple(),
                           game.snake.cell_size)
        
def draw_food():
    if game.food is not None:
        pygame.draw.circle(game.screen,GREEN, game.food,CELL_RADIUS)
    # import random
    
    # foodSize = CELL_RADIUS * 2
    # #randX will pick a value from [40,80,120,160,200 , ... 960]
    # randX = random.randrange(foodSize, SCREEN_SIZE[0], foodSize)
    # randY = random.randrange(foodSize, SCREEN_SIZE[1], foodSize)

def generate_food():
    import random
    while game.food is None:
        foodSize = CELL_RADIUS * 2
        #randX will pick a value from [40,80,120,160,200 , ... 960]
        randX = random.randrange(foodSize, SCREEN_SIZE[0], foodSize)
        randY = random.randrange(foodSize, SCREEN_SIZE[1], foodSize)
        game.food = (randX, randY)

        
def moniterKeyPress():
    pressed_key = pygame.key.get_pressed()
    # if up arraw was pressed
    
    if pressed_key[pygame.K_UP] and game.snake.direction != 'D':
        game.snake.direction = 'U' 
    if pressed_key[pygame.K_LEFT] and game.snake.direction != 'R':
        game.snake.direction = 'L'
    if pressed_key[pygame.K_RIGHT] and game.snake.direction != 'L':
        game.snake.direction = 'R'
    if pressed_key[pygame.K_DOWN] and game.snake.direction != 'U':
        game.snake.direction = 'D'

def is_snake_food_collide():
    head = game.snake.body[0].copy()
    head.update(game.snake.direction)
    return (game.food[0]-head.x) == 0 and (game.food[1]-head.y) == 0

def if_eatFood():
    if game.food is not None and is_snake_food_collide():
        cell = Cell(game.food[0],game.food[1])
        game.snake.body.insert(0,cell)
        game.food = None

def gameOver():

    if game.snake.body[0].to_tuple() in [cell.to_tuple() for cell in game.snake.body[1:]]:
        print('game over')
        game.running = False

    if game.snake.body[0].x >= SCREEN_SIZE[0] or game.snake.body[0].x < 0:
        print('game over')
        game.running = False
    
    if game.snake.body[0].y >= SCREEN_SIZE[1] or game.snake.body[0].y < 0:
        print('game over')
        game.running = False

    
# function
def update():
    # it will moniter which key was pressed
    # pressed_key = pygame.key.get_pressed()
        
    # R and D consider how to move down and right
    moniterKeyPress()

    if_eatFood()

    gameOver()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        
        if event.type == UPDATE:
            # print('1')
            game.snake.update()
        
        if event.type == UPDATE:
            generate_food()

        

if __name__ == '__main__':
    init_game()
    game = Game()
    while game.running == True:
        update()
        draw()

        
    pygame.quit()



'''
next/ hw

1. consider how to make a white screen

2. draw a circle in screen #pygame.draw.circle()

3. try to use key to control move( consider change circle's position to change)

4. let circle move in certain area
'''
