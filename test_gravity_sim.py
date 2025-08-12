#
# Code ported from:
# https://gravitywars.meyerweb.com/js/gw.js
# 
# Which is itself adapted from Sohrab Ismail-Beigi
# http://pascal.sources.ru/games/gravwar2.htm
# http://appliedphysics.yale.edu/sohrab-ismail-beigi
import math
import matplotlib.pyplot as plt

#probably just some reminders
x_domain = (-500, 500)
y_domain = (-500, 500)

# we make some objects
planet1 = {'x': 100,
          'y': 400,
          'mass': 50}
planet2 = {'x': 400,
          'y': 100,
          'mass': 55}
planet3 = {'x': 150,
          'y': 400,
          'mass': 55}
planet4 = {'x': -150,
          'y': -400,
          'mass': 55}
planet5 = {'x': -30,
          'y': -250,
          'mass': 30}

planet_set = [planet1, planet2, planet3, planet4, planet5]

missile = {'x': 0,
           'y': 0,
           'mass': 1,
           'velocity_x': 0.005,
           'velocity_y': 0.005} 

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

# Here we simulate 1000 time steps
time = 1
for i in range(0, 4000):
    missile['x'] += missile['velocity_x'] * time
    missile['y'] += missile['velocity_y'] * time
    forces = calculateForces(missile, planet_set)
    missile['velocity_x'] += forces['x'] * time
    missile['velocity_y'] += forces['y'] * time
    missile['x'] += missile['velocity_x']
    missile['y'] += missile['velocity_y'] * time
    position_history['x'].append(missile['x'])
    position_history['y'].append(missile['y'])

# Truncate the trajectory history such that we just plot in 
# the domains
x_idx = findTruncateIdx(position_history['x'], x_domain)
y_idx = findTruncateIdx(position_history['y'], y_domain)

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
for planet in planet_set:
    ax.plot(planet['x'], planet['y'], 'o-', linewidth=2)

ax.plot(position_history['x'], position_history['y'], 'o-', linewidth=2)
plt.show()
