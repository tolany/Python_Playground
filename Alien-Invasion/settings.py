# Class to store all settings for AI 
class Settings():

    #initial settings 
    def __init__(self):

        #screen 
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        
        #ship
        #self.ship_speed_factor = 1.5 
        self.ship_limit = 3 

        #Bullet 
        #self.bullet_speed_factor = 1 
        self.bullet_width = 300 
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 

        #Alien 
        self.fleet_drop_speed = 50 

        #game speed up 
        self.speed_scale = 1.1

        #alien increase 
        self.score_scale = 1.5 
        self.initalize_dynamic_settings()
    
    # settings that changing ones 
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5 
        self.bullet_speed_factor = 3 
        self.alien_speed_factor = 1 

        self.fleet_direction = 1 
        self.alien_points = 50 

    # increase speed and alien point value 
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)


        
