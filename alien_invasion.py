import sys
import pygame

from settings import Settings
from ship import Ship

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

    # Start main loop of game
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    #look for keyboard events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Move ship right
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        # Redraw screen during each pass
        self.screen.blit(self.settings.bg, [0,0])
        # Redraw ship
        
        self.ship.blitme()

        pygame.display.flip()

# Make game instance, run 
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
