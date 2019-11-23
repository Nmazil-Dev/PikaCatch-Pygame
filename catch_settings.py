class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ball_speed_factor = .4
        #how many pokeballs can you miss
        self.ball_limit = 3
        #voltorb speed
        self.voltorb_speed_factor = .6
        #how many voltorb hits before gameover
        self.hits_left = 3
        #how many pokeballs were caught
        self.caught = 0
