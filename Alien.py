import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #加载外星人图像，设置rect图像
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #每个外星人最初都在屏幕左上角出现
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)

    def blitme(self):
        #绘制
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
