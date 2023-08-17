import pygame

SCREEN_SIZE = [1000,800]
WHITE = (255,255,255)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)

#3 new
UPDATE = pygame.USEREVENT + 1

def init_game():
    pygame.init()
    pygame.display.set_caption("Snake")
    # new
    pygame.time.set_timer(UPDATE,200)

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def to_tuple(self):
        return (self.x,self.y)
    
    #new
    def copy(self):
        return Cell(self.x,self.y)
    
    #new
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
        # new
        self.direction = 'L'
    
    # new
    def update(self):
        head = self.body[0].copy()
        self.body.pop()
        head.update(self.direction)
        self.body.insert(0,head)





def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        
        if event.type == UPDATE:
            game.snake.update()


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