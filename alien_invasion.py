import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

# Manage game assets and behavior
class AlienInvasion:


#############################################################################
# GAME RESOURCES #
#############################################################################

    # Initialize game, create resources
    def __init__(self):
        # Game init andd screen infomation
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance of game statistics and create scoreboard
        self.stats = GameStats(self)
        self.sb =Scoreboard(self)

        # Create ship, bullets, and aliens
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Play button
        self.play_button = Button(self, "Play")

    # Start main loop of game
    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

#############################################################################
# KEY EVENTS #
#############################################################################
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        # Right press
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Left press
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Up press
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        # Down press
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        # Spacebar press (shoot)
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # Q press (quit)
        elif event.key ==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # Right release
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # Left release
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # Up release
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        # Down release
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

#############################################################################
# BULLETS #
#############################################################################
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Update bullets position
    def _update_bullets(self):
        self.bullets.update()

        self._check_bullet_alien_collisions()

        # Remove bullets that are offscreen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    #check if bullet hit alien
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values(): 
                self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()


#############################################################################
# ALIENS #
#############################################################################
    # Create fleet of alien invaders
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens = space_x // (2 * alien_width)

        #determine number of rows
        ship_height = self.ship.rect.height
        space_y = (self.settings.screen_height - 
                    (3 * alien_height) - ship_height)
        number_of_rows = space_y // (2 * alien_height)

        # Create row of aliens
        for row_number in range(number_of_rows -1):
            for alien_number in range(number_of_aliens):
                self._create_alien(alien_number, row_number)

    # Create an alien and place in row
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # Respond if aliens have reached edge
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    # Drop fleet and change direction
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1

    # Check if aliens have reached the bottom
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    # Update positions of alien fleet
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # Alien, ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check for aliens hitting the bottom
        self._check_aliens_bottom()

#############################################################################
# Ship #
#############################################################################
    # Ship hit by alien
    def _ship_hit(self):

        if self.stats.ships_left > 0:
            # Decrement ship count
            self.stats.ships_left -= 1

            # Remove bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # Create new ship and center
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

#############################################################################
# Play button #
#############################################################################

    # Start game when player pushes start button
    def _check_play_button(self, mouse_pos):

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game settings
            self.settings.initialize_dynamic_settings()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

            # Reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()

            # Remove old aliens/bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

#############################################################################
# DRAW #
#############################################################################
    def _update_screen(self):
        # Redraw screen during each pass
        self.screen.blit(self.settings.bg, [0,0])
       
        # Redraw ship
        self.ship.blitme()
        
        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
       
        # Draw aliens
        self.aliens.draw(self.screen)

        # Draw score information
        self.sb.show_score()

        # Draw play button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

# Make game instance, run 
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
