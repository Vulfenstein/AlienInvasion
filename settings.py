import pygame
# Store all settings for Alien Invasion
class Settings:

    # Initialize game settings
    def __init__(self):
        # Screen #
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load("assets/background.jpg")
       # self.bg_color = (230, 230, 230)

        # Ship Settings #
        self.ship_speed = 1.0