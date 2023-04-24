class Settings:
    """A class to store all settings for Alien Invasion """
    def __init__(self):
        # screen settigs.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (222, 232, 255)
        # ship settings
        self.ship_speed = 2.5
        # bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)