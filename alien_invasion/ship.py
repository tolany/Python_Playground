import pygame 

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen 
        self.ai_settings = ai_settings

        # Ship 이미지 로드, rect 가져오기 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 각 ship은 항상 화면의 바닥 중앙 부분에서 시작 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 10값 저장 
        self.center = float(self.rect.centerx)

        # Movement flags 
        self.moving_right = False 
        self.moving_left = False 


    def update(self):
        # movement flag에 기반해서 우주선의 위치 업데이트 
        # 우주선의 중앙값 업데이트
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor 
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # rect 객체 업데이트 
        self.rect.centerx = self.center        

    def blitme(self):
        # 우주선의 현재 위치 그리기 
        self.screen.blit(self.image, self.rect)


