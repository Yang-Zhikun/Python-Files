# 导入必要的库
import pygame  # 用于游戏开发
import random  # 用于随机生成食物位置
import sys    # 用于系统退出

# 初始化pygame库
pygame.init()

# 定义游戏中使用到的颜色常量
WHITE = (255, 255, 255)  # 白色
BLACK = (0, 0, 0)        # 黑色
RED = (255, 0, 0)        # 红色，用于食物
GREEN = (0, 255, 0)      # 绿色，用于蛇身
BLUE = (0, 0, 255)       # 蓝色，用于标题
YELLOW = (255, 255, 0)   # 黄色，用于说明文字

# 游戏基本设置
WIDTH, HEIGHT = 800, 600  # 增大游戏窗口尺寸，提供更好的游戏体验
GRID_SIZE = 20            # 每个网格的大小(像素)
GRID_WIDTH = WIDTH // GRID_SIZE  # 水平方向网格数量
GRID_HEIGHT = HEIGHT // GRID_SIZE # 垂直方向网格数量
FPS = 10                  # 游戏帧率(每秒更新次数)

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 设置窗口大小
pygame.display.set_caption("贪吃蛇游戏")           # 设置窗口标题
clock = pygame.time.Clock()                       # 创建时钟对象用于控制游戏速度

# 蛇类
class Snake:
    def __init__(self):
        """初始化蛇的初始状态
        - positions: 蛇身各节的位置列表，初始在屏幕中央
        - direction: 蛇的移动方向，初始向右
        - length: 蛇的长度，初始为1
        - score: 玩家得分，初始为0
        """
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1
        self.score = 0
    
    def get_head_position(self):
        """获取蛇头的位置
        返回: 蛇头的坐标(x,y)
        """
        return self.positions[0]
    
    def move(self):
        """移动蛇
        1. 计算新的蛇头位置
        2. 检查是否撞到自己
        3. 更新蛇的位置
        返回: True-移动成功 False-撞到自己游戏结束
        """
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_x = head_x + dir_x
        new_y = head_y + dir_y
        
        # 检测是否撞到边缘
        if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
            return False  # 撞到边缘游戏结束
            
        if (new_x, new_y) in self.positions[1:]:
            return False  # 撞到自己
            
        self.positions.insert(0, (new_x, new_y))
        if len(self.positions) > self.length:
            self.positions.pop()  # 如果蛇没有吃到食物，移除尾部
        return True
    
    def grow(self):
        """蛇增长
        吃到食物后调用，增加蛇的长度和玩家得分
        """
        self.length += 1
        self.score += 1
    
    def change_direction(self, direction):
        """改变蛇的移动方向
        参数: direction - 新的方向向量
        限制: 不能直接反向移动(如不能从右转左)
        """
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
    
    def draw(self, surface):
        """绘制蛇
        参数: surface - 要绘制到的pygame表面
        蛇头使用蓝色显示，身体部分保持绿色
        """
        for i, position in enumerate(self.positions):
            rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = BLUE if i == 0 else GREEN  # 蛇头用蓝色，身体用绿色
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

# 食物类
class Food:
    def __init__(self):
        """初始化食物
        - position: 食物的位置坐标
        创建时随机生成初始位置
        """
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        """随机生成食物位置
        在网格范围内随机选择一个位置
        """
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def draw(self, surface):
        """绘制食物
        参数: surface - 要绘制到的pygame表面
        绘制一个红色方块和黑色边框
        """
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)

# 显示开始界面
def show_start_screen(surface):
    """显示游戏开始界面"""
    surface.fill(BLACK)
    
    # 游戏标题
    title_font = pygame.font.SysFont('SimHei', 64)
    title_text = title_font.render("贪吃蛇游戏", True, BLUE)
    title_rect = title_text.get_rect(center=(WIDTH//2, HEIGHT//3))
    surface.blit(title_text, title_rect)
    
    # 操作说明
    instruction_font = pygame.font.SysFont('SimHei', 24)
    instruction_text = instruction_font.render("按空格键开始游戏", True, YELLOW)
    instruction_rect = instruction_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    surface.blit(instruction_text, instruction_rect)
    
    # 控制说明
    controls_text = instruction_font.render("使用方向键控制蛇的移动", True, WHITE)
    controls_rect = controls_text.get_rect(center=(WIDTH//2, HEIGHT*2//3))
    surface.blit(controls_text, controls_rect)
    
    pygame.display.update()

# 游戏主循环
def main():
    """
    游戏主循环函数
    1. 显示开始界面
    2. 初始化蛇和食物对象
    3. 处理用户输入
    4. 更新游戏状态
    5. 渲染游戏画面
    """
    # 显示开始界面
    show_start_screen(screen)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
    
    snake = Snake()  # 创建蛇对象
    food = Food()    # 创建食物对象
    game_over = False  # 游戏结束标志
    
    while True:
        # 处理游戏事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 窗口关闭事件
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 键盘按下事件
                if not game_over:  # 游戏进行中处理方向控制
                    if event.key == pygame.K_UP:
                        snake.change_direction((0, -1))  # 向上
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction((0, 1))   # 向下
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction((-1, 0))  # 向左
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction((1, 0))   # 向右
                elif event.key == pygame.K_SPACE:  # 空格键重新开始
                    snake = Snake()
                    food = Food()
                    game_over = False
        
        # 游戏逻辑更新
        if not game_over:
            if not snake.move():  # 移动蛇，如果撞到自己则游戏结束
                game_over = True
            
            # 检测是否吃到食物
            if snake.get_head_position() == food.position:
                snake.grow()  # 蛇增长
                food.randomize_position()  # 重新生成食物
                # 确保食物不会生成在蛇身上
                while food.position in snake.positions:
                    food.randomize_position()
        
        # 渲染游戏画面
        screen.fill(BLACK)  # 清空屏幕为黑色
        snake.draw(screen)  # 绘制蛇
        food.draw(screen)   # 绘制食物
        
        # 显示分数
        font = pygame.font.SysFont('SimHei', 24)
        score_text = font.render(f"分数: {snake.score}", True, YELLOW)
        screen.blit(score_text, (10, 10))  # 在左上角显示分数
        
        # 游戏结束显示
        if game_over:
            font = pygame.font.SysFont('SimHei', 36)
            game_over_text = font.render("游戏结束! 按空格键重新开始", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(game_over_text, text_rect)  # 在屏幕中央显示游戏结束文字
        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()