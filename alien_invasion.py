import sys
import pygame

from Settings import Settings
from modules.ship import Ship
from modules.bullet import Bullet
from modules.alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game ressources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            size=(0, 0), flags=pygame.FULLSCREEN
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # Name of the window
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            # print(len(self.bullets))
            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disapppeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Check for any bullets that have hit aliens.
        # IF so, get rid of the bullet and the alien.

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collied.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)  # Les deux True value définissent si les sprites doivent etre détruit ou non
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.settings.alien_speed += 0.2
            self._create_fleet()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_alien(self, alien_number, row):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_heigth = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_heigth + 2 * alien.rect.height * row
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_heigth -
                             (alien_height * 3) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create the fill fleet of aliens.
        for row in range(number_rows):
            for alien_number in range(number_alien_x):
                # Create an alien and place it in the row.
                self._create_alien(alien_number, row)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # MAke a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
