from settings import * 
from player import *


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('PONG')
        
        # General Setup
        self.running = True
        self.clock = pygame.time.Clock()
        
        # Surfaces
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Groups
        self.all_sprites = pygame.sprite.Group()
        
        # Sprites
        self.player = Player(self.all_sprites, (POS['player'][0], POS['player'][1]))
    
    def update(self):
        pass
    
    def run(self):
        self.game_events = pygame.event.get()
        
        while self.running:
            dt = self.clock.tick() / 1000
            
            # Event Loop
            for event in self.game_events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Draw Game
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()




if __name__ == '__main__':
    game = Game()
    game.run()

