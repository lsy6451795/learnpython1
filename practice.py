import pygame
import sys
from tutle import turtle
class new():
    def __init__(self):
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(0,191,243)
sc=new()

screen=pygame.display.set_mode((sc.screen_width,sc.screen_height))
turtle=turtle(screen)
pygame.display.set_caption("blues background")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(sc.bg_color)
    turtle.blitme()
    pygame.display.flip()
