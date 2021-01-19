
# Track game statistics
class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Track high score
        self.high_score = 0

        # Start game in inactive mode
        self.game_active = False
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
