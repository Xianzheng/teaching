import pygame

# 屏幕大小
SCREEN_SIZE = (1000, 800)
# 定义白色的RGB颜色值
WHITE = (255, 255, 255)
# 定义蛇的颜色
SNAKE_COLOR = (0, 0, 0)
# 定义细胞半径
CELL_RADIUS = 20

# 定时更新游戏
UPDATE = pygame.USEREVENT + 1


def init_game():
    pygame.init()
    # 游戏窗口的标题
    pygame.display.set_caption("Snake game")
    # UPDATE事件的定时器，每1000毫秒触发一次
    pygame.time.set_timer(UPDATE, 1000)


def update():
    # 检查所有的pygame事件
    for event in pygame.event.get():
        # 如果用户关闭窗口，将游戏状态为不运行
        if event.type == pygame.QUIT:
            game.running = False

        # 当UPDATE事件触发时，更新蛇的位置
        if event.type == UPDATE:
            game.snake.update()


class Game:
    def __init__(self):
        # 初始化游戏状态为运行
        self.running = True
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # 创建蛇对象
        self.snake = Snake()


class Cell:
    def __init__(self, x, y):
        # 初始化细胞的坐标
        self.x = x
        self.y = y

    def to_tuple(self):
        # 将细胞的坐标转换为元组
        return (self.x, self.y)

    def copy(self):
        # 复制细胞对象并返回一个新的细胞对象
        return Cell(self.x, self.y)

    def move(self, direction):
        # 'U' = MOVE UP
        # 'L' = MOVE LEFT
        # 'R' = MOVE RIGHT
        # 'D' = MOVE DOWN
        if direction == "U":
            self.y -= CELL_RADIUS * 2
        if direction == "D":
            self.y += CELL_RADIUS * 2
        if direction == "R":
            self.y += CELL_RADIUS * 2
        if direction == "L":
            self.X -= CELL_RADIUS * 2


class Snake:
    def __init__(self):
        # 蛇身细胞直径
        cell_diameter = CELL_RADIUS * 2
        # 蛇头的初始位置为屏幕中心
        x = SCREEN_SIZE[0] // 2
        y = SCREEN_SIZE[1] // 2
        # 创建蛇身的初始细胞列表
        self.body = [
            Cell(x, y),
            Cell(x + cell_diameter, y),
            Cell(x + cell_diameter * 2, y),
            Cell(x + cell_diameter * 2, y + cell_diameter),
        ]
        # 蛇细胞的大小
        self.cell_size = CELL_RADIUS
        # 蛇的颜色
        self.color = SNAKE_COLOR

    def update(self):
        # 复制蛇头的位置
        head = self.body[0].copy()
        # 移除蛇尾
        self.body.pop()
        # 根据当前移动方向更新蛇头的位置
        head.update(self.direction)
        # 将新的蛇头插入到蛇身的起始位置
        self.body.insert(0, head)


def draw_snake():
    # 绘制蛇身上的每个细胞
    for cell in game.snake.body:
        pygame.draw.circle(
            game.screen, game.snake.color, cell.to_tuple(), game.snake.cell_size
        )


if __name__ == "__main__":
    # 初始化的pygame,并且给屏幕一个标题
    init_game()
    # 创建game类的一个实体，这个实体主要控制这个游戏的流程
    game = Game()

    # 在class game 有一个attribute running， if running is True,游戏运行， else 游戏结束
    while game.running == True:
        # 给我们游戏屏幕画一个颜色
        game.screen.fill(WHITE)
        draw_snake()
        # pygame.draw.line(game.screen, (0, 0, 0), (10, 10), (10, 500))
        # pygame.draw.circle(game.screen, (102, 51, 51), (500, 400), 40)

        # #检测我们是否有按键被按下
        update()

        # 不断刷新我们的界面
        pygame.display.flip()

    # 退出我们的游戏
    pygame.quit()

'''
next class:

funtion

class

梳理下这个游戏的结构

通过上下左右控制移动

HW:
 
看这段代码， 告诉我目前这段代码史怎么运行的，

给每段代码做一个注释

分析下每个class 和 function是怎么连接的
'''

