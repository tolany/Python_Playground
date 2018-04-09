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
    
    # 우주선 만들기 
    ship = Ship(ai_settings, screen)
    
    # 볼릿을 저장할 그룹을 만들기 
    bullets = Group()

    # 게임 메인 루프 시작 
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
     
run_game()