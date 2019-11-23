import pygame
from pygame.sprite import Sprite
from random import randint

class Voltorb(Sprite):
    #class to rep a Ball
    def __init__(self, ai_settings, screen, stats):
        super(Voltorb, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        # load the ball and set its rect
        self.image = pygame.image.load('images/voltorb.bmp')
        self.rect = self.image.get_rect()

        self.random = randint(10, 790)
        #start each at a random x at the top of the screen
        self.rect.x = self.rect.centerx + self.random
        self.rect.y = self.rect.top

        #store position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        #draw ball at location
        self.screen.blit(self.image, self.rect)

    def update(self):
        #move down
        self.y += self.stats.vol_speed
        self.rect.y = self.y


    def check_edges(self):
        #return true if ball is at bottom
        if self.y >= 800:
            return True

        else:
            False






