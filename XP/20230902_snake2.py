#change
#enter virtual environment （.\venv\Script\activate）
import pygame

SCREEN_SIZE = [1000,800]

WHITE = (255,255,255) #RGB
RED = (255,0,0)
BLACK = (0,0,0)
CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0) #RGB (0,0,0) represent black

# 1000 / 2 = 500.0
# 1000 // 2 = 500
# 5 / 2 = 2.5
# 5 // 2 = 2

#function
def init_game():
    pygame.init()
    pygame.display.set_caption("Snake game")

# class
class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()
# def draw_blackDot():
#     pygame.draw.circle(game.screen,BLACK,POSITION,CELL_RADIUS * 2)

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x,self.y)


class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = SCREEN_SIZE[0] // 2
        # x = 500
        y = SCREEN_SIZE[1] // 2
        # y = 400
        self.body = [Cell(x,y),Cell(x+cell_diameter,y),Cell(x, y+cell_diameter)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR

def draw():
    game.screen.fill(WHITE)
    draw_snake()
    pygame.display.flip()

def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,
                           game.snake.color,
                           cell.to_tuple(),
                           game.snake.cell_size)

# function
def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

if __name__ == '__main__':
    init_game()
    game = Game()
    while game.running == True:
        update()
        draw()
        
    pygame.quit()
