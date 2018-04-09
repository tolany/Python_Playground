import pygame

class Ship():
    def __init__(self,screen):
        #우주선을 초기화하고 시작 위치를 지정합니다.
        self.screen = screen
        self.ai_settings = ai_settings

        #우주선 이미지를 불러오고, 이미지의 객체를 설정합니다. 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #우주선을 새로 만들 때는 항상 화면 아래 & 중앙에 만듭니다. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottem = self.screen_rect.bottem

        #우주선 중앙 좌표의 가로 좌표를 부동소수점 숫자로 저장합니다. 
        self.center = float(self.rect.centerx)

        #이동 플래그 
        self.moving_right = False
        self.moving_light = False
    
    def update(self):
        #이동 플래그에 따라 위치를 업데이트 합니다. 
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_light:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        
        #rect 객체를 self.center에 따라 업데이트 합니다 
        self.rect.centerx = self.center

    def blitme(self):
        #우주선의 현재 위치에 우주선을 그립니다. 
        self.screen.blit(self.image, self.rect)