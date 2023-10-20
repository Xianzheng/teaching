import pygame
# pip install pygame
SCREEN_SIZE = (1000,800)
WHITE = (255,255,255)
SNAKE_COLOR = (0,0,0)
CELL_RADIUS = 20

def init_game():
    pygame.init()
    pygame.display.set_caption('Snake game')


def update():
    # pygame will moniter if we enter some key, expecially quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        

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
    


class Snake:

    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        # SCREEN_SZIE = (1000,800)
        #                 0    1
        # x, y represent first cell position
        x = SCREEN_SIZE[0] // 2
        y = SCREEN_SIZE[1] // 2
        # determine the size of each Cell
        self.body  = [Cell(x,y),Cell(x+cell_diameter,y),Cell(x+cell_diameter*2,y),
                      Cell(x+cell_diameter*2,y+cell_diameter)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR 

def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen,game.snake.color,
                           cell.to_tuple(),
                           game.snake.cell_size)
if __name__ == '__main__':
    # 初始化我们的pygame,并且给屏幕一个标题
    init_game()
    # 创建 game类 的一个实体，这个实体主要控制这个游戏的流程
    game = Game()
    
    #在class game 有一个attribute running， if running is True,游戏运行， else 游戏结束
    while game.running == True:
        # 给我们游戏屏幕画一个颜色
        game.screen.fill(WHITE)
        draw_snake()
        # pygame.draw.line(game.screen,(0,0,0),(10,10),(10,500))

        #(pygame screen, Color,Position, diameter)
        # pygame.draw.circle(game.screen, 
        #                    (102, 51, 51),
        #                    (500,400),
        #                    40)
        
        # #检测我们是否有按键被按下
        update()

        #不断刷新我们的界面
        pygame.display.flip()
    
    #退出我们的游戏
    
    pygame.quit()
'''
hw:
(* represent Cell)
1.
****
   *

2.
***
*
*
3.
*
*
*
'''