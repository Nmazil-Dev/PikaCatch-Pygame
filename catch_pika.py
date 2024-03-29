import pygame

class Hand():

        def __init__(self, screen):
            #initialize the pika
            self.screen = screen

            #load the ship image and get its rect
            self.image = pygame.image.load('images/pika.bmp')
            self.rect = self.image.get_rect()
            self.screen_rect = self.screen.get_rect()

            #start each ship at the bottom center of the screen
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom

            #move flag
            self.moving_right = False
            self.moving_left = False

        def blitme(self):
            #draw pika at location
            self.screen.blit(self.image, self.rect)

        def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.centerx += 1
            elif self.moving_left and self.rect.left > 0:
                self.rect.centerx -= 1
