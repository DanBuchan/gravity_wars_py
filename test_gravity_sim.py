#
# Code ported from:
# https://gravitywars.meyerweb.com/js/gw.js
# 
# Which is itself adapted from Sohrab Ismail-Beigi
# http://pascal.sources.ru/games/gravwar2.htm
# http://appliedphysics.yale.edu/sohrab-ismail-beigi


# verse.G = 0.1
# density: floor((randon.random() * 3) + 2) / 2,
# radius: (Math.random() * 50) + 20,
# mass: 0,
# mass = verse.G * 2 * Math.PI * Math.pow(planets[i].radius,2) * planets[i].density;

import math
import matplotlib.pyplot as plt
import random

#probably just some reminders
x_play_domain = (-500, 500)
y_play_domain = (-500, 500)
x_system_domain = (-1000, 1000)
y_system_domain = (-1000, 1000)
g = 0.1
# random.seed(1234)
def generate_planet(x_bounds, y_bounds, g):
    planet = {'x': random.randint(x_bounds[0],x_bounds[1]),
              'y': random.randint(y_bounds[0],y_bounds[1]),
              'density': math.floor((random.random() * 3) + 2) / 2,
              'radius': (random.random() * 50) + 20,
              #'density': 0.75,
              'mass': None}
    planet['mass'] = g * 2 * math.pi * planet['radius']**2 * planet['density']
    return(planet)
planet_set = []
for i in range(1, 15):
    planet_set.append(generate_planet(x_play_domain,
                                      y_play_domain,
                                      g))

missile = {'x': 0,
           'y': 0,
           'velocity_x': random.random(),
           'velocity_y': random.random()} 

position_history = {'x': [],
                    'y': []}


def distance(x, y):
    return math.sqrt(x**2 + y**2)

def calculateForces(missile, planets):
    forces = {'x': 0,
              'y': 0,
              'l': 0}
    for planet in planets:
        #first get the distance from my missile and this planet
        dx = missile['x'] - planet['x']
        dy = missile['y'] - planet['y']
        phys_dist = distance(dx,dy)
        k = 1/((phys_dist**2) * phys_dist)
        forces['x'] = forces['x'] - planet['mass'] * dx * k 
        forces['y'] = forces['y'] - planet['mass'] * dy * k
        forces['l'] = distance(forces['x'], forces['y'])  
    return forces

def findTruncateIdx(positions, domain):
    idx = None
    for j, pos in enumerate(positions):
        if pos > domain[1]:
            idx = j
            break
        if pos < domain[0]:
            idx = j
            break          
    return(idx)

# Here we simulate 5mins of playtime at 60fps
# (5*60*60)
time = 1

for i in range(0, 18000):
    missile['x'] += missile['velocity_x'] * time
    missile['y'] += missile['velocity_y'] * time
    forces = calculateForces(missile, planet_set)
    missile['velocity_x'] += forces['x'] * time
    missile['velocity_y'] += forces['y'] * time
    missile['x'] += missile['velocity_x']
    missile['y'] += missile['velocity_y'] * time
    position_history['x'].append(missile['x'])
    position_history['y'].append(missile['y'])
    if missile['x'] < x_system_domain[0] or missile['x'] > x_system_domain[1]:
        break
    if missile['y'] < x_system_domain[0] or missile['y'] > x_system_domain[1]:
        break

# Truncate the trajectory history such that we just plot in 
# the domains
x_idx = findTruncateIdx(position_history['x'], x_play_domain)
y_idx = findTruncateIdx(position_history['y'], y_play_domain)

truncate_idx = None
if x_idx:
    truncate_idx = x_idx

if y_idx:
    if x_idx:
        if y_idx < truncate_idx:
            truncate_idx = y_idx
    else:
        truncate_idx = y_idx

if truncate_idx:
    position_history['x'] = position_history['x'][:truncate_idx]
    position_history['y'] = position_history['y'][:truncate_idx]

fig, ax = plt.subplots()
ax.set_xlim([-500, 500])
ax.set_ylim([-500, 500])
for i, planet in enumerate(planet_set):
    ax.plot(planet['x'], planet['y'], 'o-', linewidth=2)
    ax.text(planet['x'] + 7, planet['y'] + 7, i+1, fontsize=12)

ax.plot(position_history['x'], position_history['y'], linewidth=1)
plt.show()
