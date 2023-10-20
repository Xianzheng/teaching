#change
#enter virtual environment （.\venv\Script\activate）
import pygame

SCREEN_SIZE = [1000,800]

WHITE = (255,255,255) #RGB
RED = (255,0,0)
BLACK = (0,0,0)
CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0) #RGB (0,0,0) represent black

UPDATE = pygame.USEREVENT + 1

# 1000 / 2 = 500.0
# 1000 // 2 = 500
# 5 / 2 = 2.5
# 5 // 2 = 2

#function
def init_game():
    pygame.init()
    pygame.display.set_caption("Snake game")
    pygame.time.set_timer(UPDATE,200)

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
            self.x + CELL_RADIUS * 2 




class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = SCREEN_SIZE[0] // 2
        # x = 500
        y = SCREEN_SIZE[1] // 2
        # y = 400
        self.direction = 'U'
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
    pygame.display.flip()

def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,
                           game.snake.color,
                           cell.to_tuple(),
                           game.snake.cell_size)

# function
def update():
    # it will moniter which key was pressed
    # pressed_key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        
        if event.type == UPDATE:
            print('1')
            game.snake.update()


if __name__ == '__main__':
    init_game()
    game = Game()
    while game.running == True:
        update()
        draw()
        
    pygame.quit()
