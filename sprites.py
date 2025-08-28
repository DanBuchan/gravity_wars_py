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
        self.rect = self.surf.get_rect()
        self.canon = pygame.Surface((5,5))
        self.canon.fill((255,64,64))
        self.x = random.randint(settings['XPlayDomain'][0],
                                int(settings['XPlayDomain'][1]/3)-self.sprite_dim_x)
        self.y = random.randint(settings['YPlayDomain'][0]+30,
                                settings['YPlayDomain'][1]-self.sprite_dim_y)
        #30 offset prevents player sprites overlapping with input UI
        self.canon_x = self.x+17
        self.canon_y = self.y+3
        self.angle_text = '000.0000'
        self.velocity_text = '1.0000'
        self.angle = 0.0
        self.velocity = 1.0
        
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
        self.y = random.randint(settings['YPlayDomain'][0]+30,
                                settings['YPlayDomain'][1]-self.sprite_dim_y)
        self.canon_x = self.x+3
        self.canon_y = self.y+3
        self.angle_text = '180.0000'
        self.velocity_text = '1.0000'
        self.angle = 180.0
        self.velocity = 1.0

# class for planets
class Planet(pygame.sprite.Sprite):
    def __init__(self, settings):
        super(Planet, self).__init__()
        self.density = math.floor((random.random() * 3) + 2) / 2
        # planet type
        # 1. Small rocky 1/8
        # 2. Rocky/earth-like 3/8
        # 3. Gas Giant 1/8
        # 4. Gas giant with ring 1/8
        # 5. Neptune like 1/8
        # 6. Neptune like with ring 1/8
        planet_types = (1, 2, 3, 4, 5, 6)
        self.planet_type = random.choices(planet_types,
                                          (1/8, 3/8, 1/8, 1/8,
                                           1/8, 1/8), k=1)[0]
        self.planet_colour = (200, 200, 200)
        # 15 to 85
        self.radius = random.randint(0, 5) + 20
        if self.planet_type == 2:
            self.planet_colour = random.choice(((225, 115, 60),(130, 225, 125),(125, 180, 220)))
            self.radius = random.randint(21, 45)
        if self.planet_type == 3:
            self.planet_colour = (225, 180, 70)
            self.radius = random.randint(61, 85)
        if self.planet_type == 4:
            self.planet_colour = (225, 180, 70)
            self.radius = random.randint(61, 85)
        if self.planet_type == 5:
            self.planet_colour = random.choice(((155, 190, 155),(155,155,190)))
            self.radius = random.randint(46, 60)
        if self.planet_type == 6:
            self.planet_colour = random.choice(((155, 190, 155),(155,155,190)))
            self.radius = random.randint(46, 60)
        self.mass = settings['G'] * 2 * math.pi * self.radius**2 * self.density
        self.x = random.randint(settings['XPlayDomain'][0]+self.radius,
                                settings['XPlayDomain'][1]-self.radius)
        self.y = random.randint(settings['YPlayDomain'][0]+self.radius,
                                settings['YPlayDomain'][1]-self.radius)
        self.image = pygame.Surface((self.radius*2+1, self.radius*2+1), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(self.image,
                                self.radius,
                                self.radius,
                                self.radius, self.planet_colour)
        pygame.gfxdraw.filled_circle(self.image,
                                     self.radius,
                                     self.radius,
                                     self.radius, self.planet_colour)
        self.rect = self.image.get_rect()

# class for Missiles
class Missile(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Missile, self).__init__() #
        # missile should start at the centre of the canon
        self.x = player.canon_x+2
        self.y = player.canon_y+1
        self.ar = math.pi * (90 - player.angle) / 180
        self.velocity_y = math.cos(self.ar) * -player.velocity /10
        self.velocity_x = math.sin(self.ar) * player.velocity /10
        self.surf = pygame.Surface((2, 2))
        self.surf.fill((230, 230, 230))
        self.rect = self.surf.get_rect()
        self.time_step = 2
    
    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)
    
    def __calculateForces(self, planets):
        forces = {'x': 0,
                  'y': 0,
                  'l': 0}
        for planet in planets:
            #first get the distance from my missile and this planet
            dx = self.x - planet.x-planet.radius
            dy = self.y - planet.y-planet.radius
            phys_dist = self.distance(dx,dy)
            k = 1/((phys_dist**2) * phys_dist)
            forces['x'] = forces['x'] - planet.mass * dx * k 
            forces['y'] = forces['y'] - planet.mass * dy * k
            forces['l'] = self.distance(forces['x'], forces['y'])  
        return forces

    def update_location(self, planets):
        self.x += self.velocity_x * self.time_step
        self.y += self.velocity_y * self.time_step
        forces = self.__calculateForces(planets)
        self.velocity_x += forces['x'] * self.time_step
        self.velocity_y += forces['y'] * self.time_step
        self.x += self.velocity_x
        self.y += self.velocity_y * self.time_step
        self.rect.x = self.x
        self.rect.y = self.y
        # position_history['x'].append(missile['x'])
        # position_history['y'].append(missile['y'])

# class for blackhole
class Blackhole(pygame.sprite.Sprite):
    pass
