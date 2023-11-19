import pygame
import random

SCREEN_SIZE = [800,800]
WHITE = (255,255,255)
GREEN = (0,100,0)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)# BLACK

# event
UPDATE = pygame.USEREVENT + 1


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()
        self.food = None

class Snake:
    def __init__(self):
        x = SCREEN_SIZE[0] // 2
        y = SCREEN_SIZE[0] // 2

        self.body = [Cell(x,y),Cell(x + 2 * CELL_RADIUS,y),Cell(x + 4 * CELL_RADIUS,y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR
        self.direction = 'D'
    
    def update(self):
        head = self.body[0].copy()
        self.body.pop()
        head.update(self.direction)
        self.body.insert(0,head)

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
        if direction == 'D':
            self.y += CELL_RADIUS * 2
        if direction == 'L':
            self.x -= CELL_RADIUS * 2
        if direction == 'R':
            self.x += CELL_RADIUS * 2

def init_game():
    pygame.init()
    pygame.display.set_caption("Snake")
    pygame.time.set_timer(UPDATE,500)

def draw():
    game.screen.fill(WHITE)
    draw_snake()
    draw_food()
    pygame.display.flip()
    

def draw_snake():
    # head = game.snake.body[0]
    # print(head.x)
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,game.snake.color,cell.to_tuple(),game.snake.cell_size)

def draw_snake():
    # head = game.snake.body[0]
    # print(head.x)
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,game.snake.color,cell.to_tuple(),game.snake.cell_size)

def generate_food():
    while game.food == None:
        foodX = random.randrange(CELL_RADIUS * 2, SCREEN_SIZE[0], CELL_RADIUS * 2)
        foodY = random.randrange(CELL_RADIUS * 2, SCREEN_SIZE[1], CELL_RADIUS * 2)
        game.food = (foodX, foodY)

def draw_food():
    if game.food != None:
        pygame.draw.circle(game.screen,GREEN,game.food,CELL_RADIUS)

def is_snake_food_collide():
    if game.food != None:
        head = game.snake.body[0].copy()
        head.update(game.snake.direction)
        result = (head.x - game.food[0] == 0 and head.y - game.food[1] == 0)
        return result

def if_eatFood():
   if is_snake_food_collide() == True:
        cell = Cell(game.food[0], game.food[1])
        game.snake.body.insert(0, cell)
        game.food = None

def check_keyPressed():
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_UP] and game.snake.direction != 'D':
        game.snake.direction = 'U'
    if pressed_key[pygame.K_DOWN] and game.snake.direction != 'U':
        game.snake.direction = 'D'
    if pressed_key[pygame.K_LEFT] and game.snake.direction != 'R':
        game.snake.direction = 'L'
    if pressed_key[pygame.K_RIGHT] and game.snake.direction != 'L':
        game.snake.direction = 'R'

def update():
    check_keyPressed()

    if_eatFood()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        
        if event.type == UPDATE:
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


# GENERATE FOOD

# EAT FOOD MAKE SNAKE BIGGER

'''
hw:

    1.implements the function make works by your coding

    2. draw a picture about how the game works


next:

    we will add more restriction for this game

    we will finish this game

    and do review for data structure
'''