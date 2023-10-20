# importing Pygame
import pygame

# Colors, Positions and Radiuses

WHITE = (255,255,255)
BRO = (121, 38, 38)
POSITION = (500, 400)
RADIUS = 20
SCREEN_SIZE = (1000, 800)

#default
x = 500
y = 400

# global SHOW
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
        self.screen = screen = pygame.display.set_mode(SCREEN_SIZE )

#To be able to quit the program

def update():
    global x
    global y


    pressed_key = pygame.key.get_pressed()
              
    if pressed_key[pygame.K_DOWN]:
        # print('down was pressed')
        
        y += 1
        # print(y)
        # pygame.draw.circle(game.screen, BRO, (x,y), RADIUS)

    if pressed_key[pygame.K_LEFT]:
        # print('left was pressed')
        
        if x > 0 + RADIUS:
            x -= 1
        # pygame.draw.circle(game.screen, BRO, (x,y), RADIUS)

    if pressed_key[pygame.K_RIGHT]:
        # print('right was pressed')
        if x < SCREEN_SIZE[0] - RADIUS:
            x += 1
        # pygame.draw.circle(game.screen, BRO, (x,y), RADIUS)

    if pressed_key[pygame.K_UP]:
        # print('up was pressed')
      
        y -= 1
        # pygame.draw.circle(game.screen, BRO, (x,y), RADIUS)    
    
    #X button will close the program
    for event in pygame.event.get():
        if event.type == (pygame.QUIT):
            game.running = False

# To add objects to the game and set colors

def drawLine():
    pygame.draw.aalines(game.screen,BRO,(100,300),(500,300),3)


def draw():
    #fill screen with WHITE (color white)
    game.screen.fill(WHITE)
    #Drawing a brown circle by giving it the color, position and radius of the circle
    pygame.draw.circle(game.screen, BRO, (x,y), RADIUS)
    pygame.draw.circle(game.screen, BRO, (x,y+ 2 * RADIUS), RADIUS)

    

    if SHOW == 0:
        pass
    else:
        pygame.draw.circle(game.screen, BRO, (700,700), RADIUS)
    #starting
    init_game()
    #game will be able to use .running and .screen
    game = Game()
    
    #if game.running is  True
    while game.running == True:
        #able to use X button
        drawLine()
        update()
        #adding circle and colors
        draw()
        #the screen will be updated constantly
        pygame.display.flip()
    #game will close after all has been finished
    pygame.quit()

'''

hw:

    how to make a rectangle move
    
'''