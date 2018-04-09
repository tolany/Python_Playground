class Settings():
    # 외계인 침공 게임의 설정을 저장하는 클래스 

    def __init__(self):
        # 게임설정 초기화 

        #화면설정 
        self.screen_width = 1200 
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #우주선 설정 
        self.ship_speed_factor = 1.5
        