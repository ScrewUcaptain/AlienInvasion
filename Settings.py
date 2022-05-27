class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # setting bullets
        self.bullet_speed = 1.8
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (212, 10, 175)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 0.80
        self.fleet_drop_speed = 10

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1  # don't change this

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change through the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.8

        # Scoring
        self.alien_points = 10

        # fleet_direction of 1 represents right to left and -1 represent left to right.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
