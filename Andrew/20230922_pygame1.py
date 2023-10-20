# pip install pygame
import pygame

WHITE = (255,255,255) # RGB
SCREEN_SIZE = (1000, 800) 
BRO = (121, 38, 38)
POSITION = (500,400)
RADIUS = 20

def init_game():
    pygame.init()
    pygame.display.set_caption("Snake")

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False 

def draw():
    game.screen.fill(WHITE)   
    pygame.draw.circle(game.screen,BRO,POSITION,RADIUS)


if __name__ == '__main__':
    init_game()
    game = Game()

    while game.running == True:
        update()
        draw()
        pygame.display.flip()
    pygame.quit()

'''
HW:

1. WRITE COMMENT FOR EACH LINE, SHOW WHAT IS YOUR UNDERSTAND

    SPECIALLY IN MAIN METHOD

2. CREATE CLASS WITH __INIT__ __STR__ MAGIC METHOD
    AND MAKE INSTANCE

3. USE DOT TO RENDER A pattern like rectangle


'''