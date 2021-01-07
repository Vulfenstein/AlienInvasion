import pygame

class Ship:

    def __init__(self, ai_game):
        # Ships starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        
        # Draw at middle bottom 
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    # Update position based on flags
    def update(self):
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1

    # Draw ship at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)