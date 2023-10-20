import pygame

SCREEN_SIZE = [800,800]
WHITE = (255,255,255)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)# BLACK


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()

class Snake:
    def __init__(self):
        x = SCREEN_SIZE[0] // 2
        y = SCREEN_SIZE[0] // 2

        self.body = [Cell(x,y),Cell(x + 2 * CELL_RADIUS,y),Cell(x + 4 * CELL_RADIUS,y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x,self.y)

def init_game():
    pygame.init()
    pygame.display.set_caption("Snake")

def draw():
    game.screen.fill(WHITE)
    draw_snake()
    pygame.display.flip()

def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,game.snake.color,cell.to_tuple(),game.snake.cell_size)


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


'''
hw:
    read code 
    write each comment for each line of this code.
    display the confusion part

    try to build rectangle using dot

next: let our snake move, control direction
'''

