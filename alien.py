import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and rect attribute
        self.image = pygame.image.load('assets/enemy1.png')
        self.rect = self.image.get_rect()

        # Start each new enemy near top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Returns true if alien is at edge of screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    # Move alien to the right
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x