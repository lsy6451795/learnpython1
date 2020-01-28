import pygame
from pygame.sprite import  Sprite
class Ship(Sprite):
    def __init__(self,ai_settiongs,screen):
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settiongs
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #初始化位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.centerx=float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        #移动标志
        self.moving_right=False
        self.moving_left =False
        self.moving_up = False
        self.moving_down = False
    def center_ship(self):
        self.center=self.screen_rect.centerx
        self.bottom=self.screen_rect.bottom

    def update(self):
        #更新飞船的center值
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centerx -=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
             self.bottom-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.bottom+=self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.bottom=self.bottom
        self.rect.centerx=self.centerx
    def blitme(self):
        self.screen.blit(self.image,self.rect)