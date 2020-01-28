class Settings():
    def __init__(self):
        self.screen_width=800
        self.screen_height=650
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1.5
        #子弹系数
        self.bullet_speed_factor=2
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=5
        #外星人移动
        self.alien_speed_factor=1.5
        self.fleet_drop_speed=2
        #fleet_direction 1 右移 -1左移
        self.fleet_direction=1
        self.alien_points=50
        self.ship_limit=3
        #节奏加快速度
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        #方向初始化
        self.fleet_direction=1
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)