from settings import *
from random import choice, uniform

# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.surf = pygame.Surface((SIZE['paddle']), pygame.SRCALPHA)
        pygame.draw.rect(self.surf, COLORS['paddle'], pygame.FRect((0, 0), SIZE['paddle']), 0, 5)
        self.image = self.surf
        self.rect = self.image.get_frect(center = POS['player'])
        self.old_rect = self.rect.copy()
        
        self.direction = 0
        self.speed = SPEED['player']
    
    # User Input
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
    
    # Movement
    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top <= 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom >= WINDOW_HEIGHT else self.rect.bottom
    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.get_direction()
        self.move(dt)


# Ball Sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)
        self.surf = pygame.Surface((SIZE['ball']), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, COLORS['ball'], (SIZE['ball'][0] / 2, SIZE['ball'][1] / 2), SIZE['ball'][0] / 2)
        self.image = self.surf
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.old_rect = self.rect.copy()
        self.paddle_sprites = paddle_sprites
        
        self.direction = pygame.Vector2(choice((-1, 1)), uniform(0.7, 0.8) * choice((-1, 1)))
        self.speed = SPEED['ball']
    
    # Movement
    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
    
    # Paddle Collision
    def collision(self, direction):
        for sprite in self.paddle_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.direction.x *= -1
                    elif self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.direction.x *= -1
                else:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y *= -1
                    elif self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y *= -1
    
    # Wall Collision
    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1
        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1
    
    # Update
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.wall_collision()
    

