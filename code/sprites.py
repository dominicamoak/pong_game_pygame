from settings import *
from random import choice, uniform

# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.surf = pygame.Surface((SIZE['paddle']))
        self.surf.fill(COLORS['paddle'])
        self.image = self.surf
        self.rect = self.image.get_frect(center = POS['player'])
        
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
        self.get_direction()
        self.move(dt)


# Ball Sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)
        self.surf = pygame.Surface((SIZE['ball']), pygame.SRCALPHA)
        
        # self.surf.fill(COLORS['ball'])
        self.image = self.surf
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
        self.direction = pygame.Vector2(choice((-1, 1)), uniform(0.7, 0.8) * choice((-1, 1)))
        self.speed = SPEED['ball']
    
    # Movement
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt
    
    # Collision
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
        self.move(dt)
        self.wall_collision()
    

