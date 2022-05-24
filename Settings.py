class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self) :
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_speed = 0.8
        
        #setting bullets
        self.bullet_speed = 0.5
        self.bullet_width = 5
        self.bullet_height = 16
        self.bullet_color = (212,10,175)
        
