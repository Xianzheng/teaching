import pygame

BACKGROUND_COLOR = (0,0,0) # RGB

class Game:
    def __init__(self):
        
        self.running = True
        # pygame.display.set_mode((100,200))
        # # create a screen wight is 100, height is 200
        self.screen = pygame.display.set_mode((100,200))
        # give game add more attrite
        self.backGround = BACKGROUND_COLOR

    def initPygame(self):
        pygame.init()
        pygame.display.set_caption('game')
        self.screen.fill(self.backGround)

if __name__ == '__main__':

    game = Game()
    game.initPygame()
    

    while game.running == True:
        
        #screen will constantly update
        pygame.display.flip()

# hw:

# write command for each line refer to class Game,

# do CCC question 2019 J4
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
