from settings import *

class Sprite(pygame.sprite.Sprite): #spirte class
    def __init__(self, pos, surf, groups):
        super().__init__(groups) 
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
