import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建 Settings 实例并使用它来访问设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 调用监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船的坐标位置
        ship.update()
        gf.update_bullets(bullets)
        # 调用函数：设置背景色； 每次循环都重绘屏幕； 将飞船绘制在背景前面； 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
