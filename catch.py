import sys
import pygame
from catch_settings import Settings
from catch_pika import Hand
import catch_functions as gf
from catch_ball import Ball
from pygame.sprite import Group
from catch_stats import GameStats
from catch_button import Button

def run_game():
    #initialize game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Catch!')

    #make the button
    play_button = Button(ai_settings, screen, 'Pika Catch!')

    hand = Hand(screen)
    stats = GameStats(ai_settings)
    hands = Group()
    balls = Group()
    voltorbs = Group()
    gf.create_ball(ai_settings, screen, balls)
    gf.create_vol(ai_settings, screen, voltorbs, stats)
    #start the game!
    while True:

        #watch for key and mouse
        gf.check_events(hand, stats, play_button)
        if stats.game_active:
            hand.update()
            gf.update_balls(ai_settings, balls, screen, hand, stats, voltorbs)
            gf.update_vol(ai_settings, screen, hand, voltorbs, balls, stats)



        gf.update_screen(ai_settings, screen, hand, balls, stats, play_button, voltorbs)

run_game()
