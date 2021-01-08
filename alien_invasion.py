import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

# Manage game assets and behavior
class AlienInvasion:

    # Initialize game, create resources
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    # Start main loop of game
    def run_game(self):
        while True:
            self._check_events()
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

        # Remove bullets that are offscreen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

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

    # Update positions of alien fleet
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

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

        pygame.display.flip()

# Make game instance, run 
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
