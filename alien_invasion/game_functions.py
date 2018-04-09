import sys 

import pygame
from bullet import Bullet


 
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
                ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 새로운 볼릿을 만들고, 그걸 그룹에 더한다.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False 

def check_events(ai_settings, screen, ship, bullets):
    # 키보드와 마우스 작동에 대한 반응 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
def update_screen(ai_settings, screen, ship, bullets):
    
    #루프가 실행될 때마다 스크린 다시 그려줌 
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    
    # 가장 최근에 그려진 스크린 화면을 표시.
    pygame.display.flip()

