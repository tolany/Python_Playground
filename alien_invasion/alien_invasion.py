import sys
import pygame

from settings import Settings
from ship import Ship

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

        #키보드와 마우스 이벤트를 주시합니다. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #루프를 실행할 때마다 화면을 다시 그립니다. 
        screen.fill(
            (ai_settings.bg_color)
        )
        ship.blitme()

        #가장 최근에 그린 화면을 표시합니다. 
        pygame.display.flip()

run_game()


