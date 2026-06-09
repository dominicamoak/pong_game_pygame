from settings import * 
from sprites import *


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
        self.paddle_sprites = pygame.sprite.Group()
        
        # Sprites
        self.player = Player((self.all_sprites, self.paddle_sprites))
        self.ball = Ball(self.all_sprites, self.paddle_sprites)
    
    def update(self):
        pass
    
    def run(self):
        while self.running:
            self.game_events = pygame.event.get()
            dt = self.clock.tick() / 1000
            
            # Event Loop
            for event in self.game_events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Updates
            self.all_sprites.update(dt)
            
            # Draw Game
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()




if __name__ == '__main__':
    game = Game()
    game.run()

