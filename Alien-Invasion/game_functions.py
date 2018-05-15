import sys 
from time import sleep 

import pygame
from bullet import Bullet
from alien import Alien 


# start a new game, if the player clicks Play button
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse,y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

# React to Key and Mouse events 
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship):
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = Rpygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

#React to Key event
def check_keydown_event(event, ai_settings, screen, stats, sb, ship, aliens, bullets):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEET:
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

# create bullet
def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False 
    elif event.key == pygame.KLEET:
        ship.moving_left = False 

# update images on the screen and flip new screen 
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):

    scren.fill(ai_settings.bg_color)

    #Redraw all bullets 
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #update bullets positions 
    bullets.update()

    #Get rid of bullests 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullets)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


#Respond to bulletss-alien collisions 
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

        check_high_score(stats, sb)

        if len(aliens) == 0:
            start_new_level(ai_settings, aliens, bullets, sb, screen, ship, stats)


#if entire fleet is destroyed, start a new level.
def start_new_level(ai_settings, aliens, bullets, sb, screen, ship, stats):
    bullets.empty()
    ai_settings.increase_speed()
    stats.level += 1 
    sb.prep_level()
    create_fleet(ai_settings, screen, ship, aliens)

#create aliens, and find the number of aliens in a row:
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

#create an alien and place it in the row 
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

#Determine num of  aliens that fit on screen 
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

#Determine num of rows of aliens that fit on screen 
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets) 
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break 

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    
    # Decrement ships_left
    stats.ships_left -= 1
    
    if stats.ships_left > 0:

        #update Scoreboards
        sb.prep_ships()

        # Empty the list of aliens and bullets 
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship 
        create_fleet(ai_settings, screen, ship, aliens)
        ship.cetner_ship()

        #pause 
        sleep(0.5)
    
    else:
        stats.game_active = False 
        pygame.mouse.set_visible(True)

def start_game(ai_settings, screen, stats, aliens, bullets):

    pygame.mouse.set_visible(False)

    stats.reset_stats()
    stats.game_active = True 

    sb.prep_images()

    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score 
        sb.prep_high_score()
        