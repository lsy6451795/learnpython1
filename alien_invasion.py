import pygame
from ship import Ship
from settings import  Settings
import game_functions as gf
import bullet
from Alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button=Button(ai_settings,screen,"Play")
    bg_color=(230,230,230)
    ship=Ship(ai_settings,screen)
    bullets = Group()
    aliens=Group()
    try :
        with open('score.txt') as f1:
            highscore=f1.readline()
        if not highscore.strip() :
            highscore=0
        highscore=int(float(highscore))
    except FileNotFoundError:
        highscore=0

    stats=GameStats(ai_settings,highscore)
    sb=Scoreboard(ai_settings,screen,stats)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_bullets(ai_settings,screen, stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()