class Settings():
    '存储《外星人入侵》的所有设置的类'

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        # self.bg_color = (230, 230, 230)
        self.bg_color = (26, 41, 51)

        # 飞船的移动速度
        self.ship_speed_factor = 0.7

        # 子弹设置
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3