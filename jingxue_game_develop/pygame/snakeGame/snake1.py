import pygame

SCREEN_SIZE = (1000,800)
WHITE = (255,255,255)
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

if __name__ == '__main__':
    # 初始化我们的pygame,并且给屏幕一个标题
    init_game()
    # 创建 game类 的一个实体，这个实体主要控制这个游戏的流程
    game = Game()
    
    #在class game 有一个attribute running， if running is True,游戏运行， else 游戏结束
    while game.running == True:
        # 给我们游戏屏幕画一个颜色
        game.screen.fill(WHITE)
        
        # #检测我们是否有按键被按下
        update()

        #不断刷新我们的界面
        pygame.display.flip()
    
    #退出我们的游戏
    pygame.quit()


'''
修改代码， 
    1.更换屏幕颜色（选择自己喜欢的颜色）
    2.更换屏幕标题
    3.复刻编写屏幕框架的流程，（可以考虑写一个文本发给我，或者写一个可运行的代码，最好不要和我写的一摸一样）


'''