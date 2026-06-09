from settings import * 
from sprites import *
import json


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
        self.ball = Ball(self.all_sprites, self.paddle_sprites, self.update_score)
        self.opponent = Opponent((self.all_sprites, self.paddle_sprites), self.ball)
        
        # Score
        try:
            with open(join('data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {
                'player': 0,
                'opponent': 0
            }
        self.font = pygame.font.Font(None, 160)
    
    def display_score(self):
        # Player Score
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_surf, player_rect)
        
        # Opponent Score
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_surf, opponent_rect)
        
        # Line Separator
        pygame.draw.line(self.display_surface, COLORS['bg detail'], (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 5)
    
    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1
    
    def run(self):
        while self.running:
            self.game_events = pygame.event.get()
            dt = self.clock.tick() / 1000
            
            # Event Loop
            for event in self.game_events:
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)
            
            # Updates
            self.all_sprites.update(dt)
            
            # Draw Game
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()




if __name__ == '__main__':
    game = Game()
    game.run()

