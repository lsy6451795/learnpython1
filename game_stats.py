import pygame

class GameStats():
    def __init__(self,ai_settings,highscore):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
        self.high_score = highscore
    def reset_stats(self):
        #初始化在游戏运行期间的统计信息
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1

