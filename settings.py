import pygame
# Store all settings for Alien Invasion
class Settings:

    # Initialize games static settings
    def __init__(self):

        # Screen #
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load("assets/background.jpg")
        self.bg_color = (0,0,0)

        # Ship Settings #
        self.ship_limit = 3

        # Bullet Settings # 
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Alien Settings #
        self.fleet_drop_speed = 10

        # Game speed up #
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    # Dynamic variables
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction (right)
        self.fleet_direction = 1

    # Speed settings
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
