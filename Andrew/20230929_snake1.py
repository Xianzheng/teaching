# importing Pygame
import pygame

# Colors, Positions and Radiuses

WHITE = (255,255,255)
BRO = (121, 38, 38)
POSITION = (500, 400)
RADIUS = 20
SHOW = 0
#setting captions

def init_game():
    #stating pygame
    pygame.init()
    pygame.display.set_caption("main")

#asigning self with running and screen. Running to run the program and screen for the dimentions and color.

class Game:
    #making def
    def __init__(self):
        #now easier to use (Ex.: game.running = False, Ex.: game.screen.fill(255,255,255))
        self.running = True
        self.screen = screen = pygame.display.set_mode((1000, 800))

#To be able to quit the program

def update():
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_UP]:
        print('up pressed')
        global SHOW
        SHOW = 1        
    if pressed_key[pygame.K_DOWN]:
        print('down was pressed')
    if pressed_key[pygame.K_LEFT]:
        print('left was pressed')
    if pressed_key[pygame.K_RIGHT]:
        print('right was pressed')    
    #X button will close the program
    for event in pygame.event.get():
        if event.type == (pygame.QUIT):
            game.running = False

# To add objects to the game and set colors

def drawCircle():
    pygame.draw.circle(game.screen, BRO, (700,700), RADIUS)


def draw():
    #fill screen with WHITE (color white)
    game.screen.fill(WHITE)
    #Drawing a brown circle by giving it the color, position and radius of the circle
    pygame.draw.circle(game.screen, BRO, (500,400), RADIUS)
    pygame.draw.circle(game.screen, BRO, (500,400+ 2 * RADIUS), RADIUS)

    if SHOW == 0:
        pass
    else:
        pygame.draw.circle(game.screen, BRO, (700,700), RADIUS)
if __name__ == "__main__":
    #starting
    init_game()
    #game will be able to use .running and .screen
    game = Game()
    
    #if game.running is  True
    while game.running == True:
        #able to use X button
        update()
        #adding circle and colors
        draw()
        #the screen will be updated constantly
        pygame.display.flip()
    #game will close after all has been finished
    pygame.quit()

'''

hw:

    when you press the key make circle move
    
'''