import pygame

SCREEN_SIZE = [1000,800]
WHITE = (255,255,255)

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

if __name__ == '__main__':
    init_game()
    game = Game()
    while game.running == True:
        update()
        game.screen.fill(WHITE)
        pygame.display.flip()
    pygame.quit()


