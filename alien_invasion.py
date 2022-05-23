import sys
import pygame

from Settings import Settings
from modules.ship import Ship 

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game, and create game ressources"""
        pygame.init()
        self.settings = Settings()
        
        
        self.screen = pygame.display.set_mode(
            size=(self.settings.screen_width, self.settings.screen_heigth)
            )
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            self._check_events()
            #Redraw the screen during each pass through the loop.
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()

        
if __name__ == "__main__":
    #MAke a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()