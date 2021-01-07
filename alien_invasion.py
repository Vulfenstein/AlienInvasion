import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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

    # Start main loop of game
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    #look for keyboard events
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

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # Redraw screen during each pass
        self.screen.blit(self.settings.bg, [0,0])
        # Redraw ship
        self.ship.blitme()
        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

# Make game instance, run 
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
