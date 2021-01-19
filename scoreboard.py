import pygame.font

class Scoreboard:

    def __init__(self, ai_game):
        # Score keeping attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Final score image
        self.prep_score()

    def prep_score(self):
        # Turn score into rendered image
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)

        # Display score in top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        # Draw score to screen
        self.screen.blit(self.score_image, self.score_rect)