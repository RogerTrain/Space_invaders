import sys
import pygame
from gaming_setting import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    def __init__(self):
        """ inatialize the game, and create game resources. """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    def run_game(self):
        """ Start of our main loop for the game"""
        while True:
            # Watch for keyboard and the mouse
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            # Redraw the screen during each pass through the loop.
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            # Make most recentlty drawn screen visible
        pygame.display.flip() 
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                    self.ship.moving_right = False
                # Move ship to the right 
                

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
    


              