class Settings():
    # 게임의 모든 설정을 저장하기 위한 클래스 

    def __init__(self):
        # 스크린 설정 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5 

        # 볼릿 설정 
        self.bullet_speed_factor = 1 
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
