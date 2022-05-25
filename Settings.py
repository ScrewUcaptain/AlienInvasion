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
