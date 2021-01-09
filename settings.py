import pygame
# Store all settings for Alien Invasion
class Settings:

    # Initialize game settings
    def __init__(self):

        # Screen #
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load("assets/background.jpg")

        # Ship Settings #
        self.ship_speed = 1.0
        self.ship_limit = 3


        # Bullet Settings # 
        self.bullet_speed = 1.0
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Alien Settings #
        self.alien_speed = 0.3
        self.fleet_drop_speed = 10
        # fleet direction (right)
        self.fleet_direction = 1