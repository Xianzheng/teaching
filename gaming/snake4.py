import pygame
import random

SCREEN_SIZE = [1000,800]
WHITE = (255,255,255)
GREEN = (0,100,0)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)

UPDATE = pygame.USEREVENT + 1
FOOD = pygame.USEREVENT + 2

def init_game():
    pygame.init()
    pygame.display.set_caption("Snake")
    pygame.time.set_timer(UPDATE,500)
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
        randX = random.randint(5,SCREEN_SIZE[0] - 5)
        randY = random.randint(5,SCREEN_SIZE[1] - 5)
        if (randX,randY) not in [cell.to_tuple for cell in game.snake.body]:
            game.food = (randX,randY)



def update():
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