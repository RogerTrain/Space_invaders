import pygame
class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right:
            self.rect.x += 100
        if self.moving_left:
            self.rect.x -= 100
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('py_gamming/nave2.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)