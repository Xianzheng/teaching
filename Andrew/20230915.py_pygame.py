# create virtual environment

#create pygame virtual env

# python -m venv [name]

# python -m venv pygameenv

# .\pygameenv\Scripts\avtivate

# ctrl + shift + p

# pip install pygame

import pygame

pygame.init()
pygame.display.set_caption("Snake")
WHITE = (255,255,255) # RGB 
BRO = (121, 38, 38)

running = True
screen = pygame.display.set_mode((1000,800))
while running:

    screen.fill(BRO)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
    

#
'''
HW
DONT SEE THE CODE I MADE IN CLASS

CHANGE THE SIZE TO SCREEN
CHANGE THE COLOR TO SCREEN
CHANGE THE CAPTION FOR SCRREN
'''

