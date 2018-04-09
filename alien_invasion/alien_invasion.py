import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #게임을 초기화하고 화면 객체를 만든다. 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #배경색을 지정합니다. 
    # bg_color = (230,230,230)

    #게임 루프를 시작합니다.  
    while Trun:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
       

run_game()


