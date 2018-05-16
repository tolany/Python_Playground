import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 게임을 시작하고, 스크린 오브젝트를 생성.
    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Make the Play button
    play_button = Button(ai_settings, screen, "Play")
    
    #create an instance to store game statistics and create a scoreboard 
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    # 우주선 만들기 
    ship = Ship(ai_settings, screen)
    
    # 볼릿을 저장할 그룹을 만들기 
    bullets = Group()
    
    # make a group of aliens 
    aliens = Group()

    # 게임 메인 루프 시작 
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)
        gf.update_screen(ai_settings, screen, stats, sb,  ship, aliens, bullets, play_button)
     
run_game()
