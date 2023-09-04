import pygame
import random

SCREEN_SIZE = [800,400]
WHITE = (255,255,255)
GREEN = (0,100,0)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)

UPDATE = pygame.USEREVENT + 1
FOOD = pygame.USEREVENT + 2

def init_game():
    pygame.init()
    pygame.display.set_caption("Snake")
    pygame.time.set_timer(UPDATE,200)
    #new
    pygame.time.set_timer(FOOD,3000)

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
    

    def update(self,direction):
        if direction == 'U':
            self.y -= CELL_RADIUS * 2
        elif direction == 'D':
            self.y += CELL_RADIUS * 2
        elif direction == 'L':
            self.x -= CELL_RADIUS * 2
        elif direction == 'R':
            self.x += CELL_RADIUS * 2

class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = SCREEN_SIZE[0]//2
        y = SCREEN_SIZE[1]//2 
        # print(x,y)
        
        self.body = [Cell(x,y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR
        self.direction = 'L'
    

    def update(self):
        head = self.body[0].copy()
        self.body.pop()
        head.update(self.direction)
        self.body.insert(0,head)


def generate_food():
    while game.food is None:
        cell_diameter = CELL_RADIUS * 2
        randX = random.randrange(CELL_RADIUS * 2,SCREEN_SIZE[0] ,CELL_RADIUS * 2)
        randY = random.randrange(CELL_RADIUS * 2,SCREEN_SIZE[1],CELL_RADIUS * 2)
        # print(randX,randY)
        if (randX,randY) not in [cell.to_tuple for cell in game.snake.body]:
            game.food = (randX,randY)


def check_keypressed():
    # 5 new 增加按键
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_UP] and not game.snake.direction == 'D':
        game.snake.direction = 'U'

    if pressed_key[pygame.K_DOWN] and not game.snake.direction == 'U':
        game.snake.direction = 'D'
    if pressed_key[pygame.K_LEFT] and not game.snake.direction == 'R':
        game.snake.direction = 'L'
    if pressed_key[pygame.K_RIGHT] and not game.snake.direction == 'L':
        game.snake.direction = 'R'

def is_snake_food_collide():
    head = game.snake.body[0].copy()
    head.update(game.snake.direction)
    return (game.food[0] - head.x) == 0 and (game.food[1] - head.y) == 0

def if_eatFood():
    if game.food is not None and is_snake_food_collide():
        cell = Cell(game.food[0],game.food[1])
        game.snake.body.insert(0,cell)
        game.food = None

def if_lose():
    if game.snake.body[0].to_tuple() in [cell.to_tuple() for cell in game.snake.body[1:]]:
        print('Game Over')
        game.running = False

    if game.snake.body[0].x >= SCREEN_SIZE[0] or  game.snake.body[0].x <= 0:
        print('Game Over')
        game.running = False
    
    if game.snake.body[0].y >= SCREEN_SIZE[1] or  game.snake.body[0].y <=0 :
        print('Game Over')
        game.running = False
        
def update():

    check_keypressed()

    if_eatFood()

    if_lose()
   
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        
        if event.type == UPDATE:
            game.snake.update()

        if event.type == UPDATE:
            generate_food()



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
        pygame.draw.circle(game.screen,GREEN,game.food,CELL_RADIUS)

if __name__ == '__main__':
    init_game()
    game = Game()
    while game.running == True:
        update()
        draw()
        pygame.display.flip()
    pygame.quit()

'''
    change snake color
    change snake size
'''