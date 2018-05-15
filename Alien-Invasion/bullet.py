import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings, screen, ship ):
        # 볼릿 오브젝트 생성, 현재 우주선 위치에 
        super(Bullet, self).__init__()
        self.screen = screen

        # 볼릿 rect 생성 (0,0)위치에, 
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 볼릿의 포지션을 10진수로 저장 
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #볼릿 오브젝트를 스크린에서 위로 움직이도록 
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        #볼릿 오브젝트를 스크린에서 아래로 움직이도록 
        pygame.draw.rect(self.screen, self.color, self.rect)    

