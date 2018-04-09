import pygame

class Ship():
    def __init__(self,screen):
        #우주선을 초기화하고 시작 위치를 지정합니다.
        self.screen = screen

        #우주선 이미지를 불러오고, 이미지의 객체를 설정합니다. 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #우주선을 새로 만들 때는 항상 화면 아래 & 중앙에 만듭니다. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottem = self.screen_rect.bottem

    def blitme(self):
        #우주선의 현재 위치에 우주선을 그립니다. 
        self.screen.blit(self.image, self.rect)