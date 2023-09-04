#change
#enter virtual environment （.\venv\Script\activate）
import pygame

SCREEN_SIZE = [1000,800]
WHITE = (255,255,255) #RGB
RED = (255,0,0)
BLACK = (0,0,0)
CELL_RADIUS = 20
POSITION = (500,400)


#function
def init_game():
    pygame.init()
    pygame.display.set_caption("Snake game")

# class
class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

def draw_blackDot():
    pygame.draw.circle(game.screen,BLACK,POSITION,CELL_RADIUS * 2)

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
        game.screen.fill(WHITE)
        # game.screen.fill(RED)
        # game.screen.fill(BLACK)
        draw_blackDot()
        pygame.display.flip() # update our screen
    pygame.quit()


'''
hw
1. 
    add class Snake, class Cell to snake1.py

2. Drwe Red Dot to position 800, 600 to screen

3. build class PencilBox, in Pencil Box include instance of Class Pen, Pencil, Eraser
'''