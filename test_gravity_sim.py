#
# Code ported from:
# https://gravitywars.meyerweb.com/js/gw.js
# 
# Which is itself adapted from Sohrab Ismail-Beigi
# http://pascal.sources.ru/games/gravwar2.htm
# http://appliedphysics.yale.edu/sohrab-ismail-beigi


# verse.G = 0.1
# density: Math.floor((Math.random() * 3) + 2) / 2,
# radius: (Math.random() * 50) + 20,
# mass: 0,
# mass = verse.G * 2 * Math.PI * Math.pow(planets[i].radius,2) * planets[i].density;

import math
import matplotlib.pyplot as plt

#probably just some reminders
x_play_domain = (-500, 500)
y_play_domain = (-500, 500)
x_system_domain = (-1000, 1000)
y_system_domain = (-1000, 1000)

# we make some objects
planet1 = {'x': 100,
          'y': 400,
          'mass': 25}
planet2 = {'x': 400,
          'y': 100,
          'mass': 25}
planet3 = {'x': 150,
          'y': 200,
          'mass': 25}
planet4 = {'x': -150,
          'y': -400,
          'mass': 30}
planet5 = {'x': -30,
          'y': -250,
          'mass': 30}
planet6 = {'x': -400,
          'y': 300,
          'mass': 25}

planet_set = [planet1, planet2, planet3, planet4, planet5, planet6]

missile = {'x': 0,
           'y': 0,
           'velocity_x': -0.001,
           'velocity_y': 0.001} 

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
