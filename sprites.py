import pygame
import random
import math
# Player 1 and 2 classes should probably just subclass a main
# player class

# class for player 1
class Player1(pygame.sprite.Sprite):
    def __init__(self, settings):
        super(Player1, self).__init__()
        self.sprite_dim_x = 25
        self.sprite_dim_y = 11
        self.surf = pygame.Surface((self.sprite_dim_x,
                                    self.sprite_dim_y))
        self.surf.fill((200, 200, 200))
        self.canon = pygame.Surface((5,5))
        self.canon.fill((255,64,64))
        self.rect = self.surf.get_rect()
        self.x = random.randint(settings['XPlayDomain'][0],
                                int(settings['XPlayDomain'][1]/3)-self.sprite_dim_x)
        self.y = random.randint(settings['YPlayDomain'][0]+self.sprite_dim_y,
                                settings['YPlayDomain'][1])
        self.canon_x = self.x+17
        self.canon_y = self.y+3
        
# class for player 2
class Player2(pygame.sprite.Sprite):
    def __init__(self, settings):
        super(Player2, self).__init__()
        self.sprite_dim_x = 25
        self.sprite_dim_y = 11
        self.surf = pygame.Surface((self.sprite_dim_x,
                                    self.sprite_dim_y))
        self.surf.fill((200, 200, 200))
        self.canon = pygame.Surface((5,5))
        self.canon.fill((255,64,64))
        self.rect = self.surf.get_rect()
        self.x = random.randint(int((settings['XPlayDomain'][1]/3)*2),
                                settings['XPlayDomain'][1]-self.sprite_dim_x)
        self.y = random.randint(settings['YPlayDomain'][0]+self.sprite_dim_y,
                                settings['YPlayDomain'][1])
        self.canon_x = self.x+3
        self.canon_y = self.y+3

# class for planets
class Planet(pygame.sprite.Sprite):
    def __init__(self, settings):
        super(Planet, self).__init__()
        self.density = math.floor((random.random() * 3) + 2) / 2
        self.radius = int((random.random() * 50) + 20)
        self.mass = settings['G'] * 2 * math.pi * self.radius**2 * self.density
        self.x = random.randint(settings['XPlayDomain'][0]+self.radius,
                                settings['XPlayDomain'][1]-self.radius)
        self.y = random.randint(settings['YPlayDomain'][0]+self.radius,
                                settings['YPlayDomain'][1]-self.radius)
        self.circle = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(self.circle, 15, 15, 14, (0, 255, 0))
        pygame.gfxdraw.filled_circle(self.circle, 15, 15, 14, (0, 255, 0))
        self.image = self.circle
        self.rect = self.image.get_rect(center=(self.x, self.y))

# class for blackholes
class Blackhole(pygame.sprite.Sprite):
    pass
# class for Missiles
class Missile(pygame.sprite.Sprite):
    pass