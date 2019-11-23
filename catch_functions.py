import sys
import pygame
from catch_ball import Ball
from time import sleep
from catch_voltorb import Voltorb

def check_keydown(event, hand):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            hand.moving_right = True
        elif event.key == pygame.K_LEFT:
            hand.moving_left = True

def check_keyup(event, hand):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            hand.moving_right = False
        elif event.key == pygame.K_LEFT:
            hand.moving_left = False



def check_events(hand, stats, play_button):
    #respond to keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, hand)
        elif event.type == pygame.KEYUP:
            check_keyup(event, hand)



def check_play_button(stats, play_button, mouse_x, mouse_y):
    #start a new game if player clicks play
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True



def create_ball(ai_settings, screen, balls):
    ball = Ball(ai_settings, screen)
    balls.add(ball)

def create_vol(ai_settings, screen, voltorbs, stats):
    voltorb = Voltorb(ai_settings, screen, stats)
    voltorbs.add(voltorb)


def update_screen(ai_settings, screen, hand, balls, stats, play_button, voltorbs):
    screen.fill(ai_settings.bg_color)
    hand.blitme()
    balls.draw(screen)
    voltorbs.draw(screen)


    #draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()


    pygame.display.flip()

def update_balls(ai_settings, balls, screen, hand, stats, voltorbs):
    check_balls_edges(ai_settings, balls, screen, stats, voltorbs)
    balls.update()
    if pygame.sprite.spritecollideany(hand, balls):
        stats.caught += 1
        print (str(stats.caught) + ' caught!')
        stats.vol_speed += .05
        balls.empty()
        create_ball(ai_settings, screen, balls)

def update_vol(ai_settings, screen, hand, voltorbs, balls, stats):
    check_vols_edges(ai_settings, voltorbs, screen, balls, stats)
    voltorbs.update()
    if pygame.sprite.spritecollideany(hand, voltorbs):
        print ('You got hit!' + '\n' + str(stats.hits_left) + ' hit(s) left!' )
        #decrement hits left by one
        stats.hits_left -= 1
        voltorbs.empty()
        create_vol(ai_settings, screen, voltorbs, stats)


def check_vols_edges(ai_settings, voltorbs, screen, balls, stats):
    #check if voltorb hit the bottom
    check_balls_edges(ai_settings, balls, screen, stats, voltorbs)
    for voltorb in voltorbs.sprites():
        if voltorb.rect.y >= 800 and stats.hits_left >= 0:
            voltorbs.empty()
            create_vol(ai_settings, screen, voltorbs, stats)
        elif stats.hits_left == -1:
            print('Game over!')
            print("You caught " + str(stats.caught) + ' pikas!')
            sys.exit()


def check_balls_edges(ai_settings, balls, screen, stats, voltorbs):
    #check if balls reached edge
    for ball in balls.sprites():
        if ball.check_edges():
            if stats.balls_left > 1:
                print(str(stats.balls_left) + ' misses left!')
            elif stats.balls_left == 1:
                print(str(stats.balls_left) + ' miss left!')
            else:
                print('Game over!')
                print("You caught " + str(stats.caught) + ' pikas!')
                sys.exit()

            ball_hit(ai_settings, stats, screen, balls, voltorbs)
            balls.empty()
            create_ball(ai_settings, screen, balls)
            create_vol(ai_settings, screen, voltorbs, stats)



def ball_hit(ai_settings, stats, screen, balls, voltorbs):
    #respond
    #decrement by one
    if stats.balls_left > 0:

        stats.balls_left -= 1

        create_ball(ai_settings, screen, balls)

        sleep(0.5)

        balls.empty()
        voltorbs.empty()
    else:
        stats.game_active = False


