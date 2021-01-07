import pygame

class Ship:

    def __init__(self, ai_game):
        # Ships starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        
        # Draw at middle bottom 
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value of ships horizontal/vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # Update position based on flags
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    # Draw ship at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)