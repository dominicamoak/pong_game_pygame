from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.surf = pygame.surface.Surface((SIZE['paddle']))
        self.color = COLORS['paddle']
        self.surf.fill(self.color)
        self.image = self.surf
        self.rect = self.image.get_frect(center = pos)
    
    def update(self):
        pass


