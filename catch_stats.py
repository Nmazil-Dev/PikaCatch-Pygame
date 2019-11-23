class GameStats():
    #track stats

    def __init__(self, ai_settings):
        #initialize stats
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        #init stats that can change during the game
        self.balls_left = self.ai_settings.ball_limit
        self.hits_left = self.ai_settings.hits_left
        self.caught = self.ai_settings.caught
        self.vol_speed = self.ai_settings.voltorb_speed_factor