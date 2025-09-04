# Gravity Wars Redux

This is a python remake of Ed Bartz's old Amiga PD game Gravity Wars v2.0. First released in September of 1987. This was the first Amiga game I ever played so it holds a real place in my heart. You can get it from Aminet at https://aminet.net/package/game/2play/GravityWars

This version includes a number of tweaks and additions largely to make it a little more interesting. But the game as a whole is much the same. One omission is the ability to build your own levels. It seldom results in play fields as interesting as the RNG gods grant us.

The goal of the game is to hit your opponent with your missile, avoiding the planets and using their gravity to your advantage.

The mathematics that drive this version are derived largely from Grav War by Sohrab Ismail-Beigi (he's currently at Yale if you wish to look him up). You can find the Pascal sources for his version at, http://pascal.sources.ru/games/gravwar2.htm. The code in Gravity Wars Redux is actually ported from Gravity Wars JS by Eric A Meyer, see: https://gravitywars.meyerweb.com/. This is largely because it was somewhat easier for me to port from Javascript code rather than pascal (didn't fancy learning Pascal just to do this tbh). One big change relative to Gravity Wars is that we recalculate the missile trajectories at every frame rather than at specific time point.

If you wish to play around with the maths implementation then check the included test_gravity_sim.py script. This will simulate multiple centres of gravity and a single missile. Planetary volumes and collision detection are omitted in this script, but you should get the idea of how the gravitation works and which constants/variables you can tweak to get differing behaviours.

## To play

Each player takes it in turn to select a missile firing angle and a velocity for their shot. The first player to strike the other wins. Any angle from 0 to 359.99999 is allowed. Any speed from 0.00001 to a max of 10 is valid. Your previous chosen values are displayed for subsequent shots, you only need to edit the values you wish to change, the previously value will be used if you leave it. Missiles fly for 90 seconds until they run out of fuel.

In the settings menu you can control whether or not missile trails persist throughout the game or are erased after each round. Having the trails erased makes the game a little harder. You can also choose to toggle whether you take turns to shoot or fire simultaneously. When playing with simultaneous shots it is possible for the game to end in a draw. When you taking turns Player 1 has a strong first player advantage, this has been left as the default way to play, as with the original Gravity Wars.

While in game you can quit and return to the main menu using the Escape key at anytime. This is useful for quickly generating new solar systems if you don't like what was generated.

### Shot angles

Angles use the following layout for both players.

```
        90
         |
         |
180 -----+----- 0
         |
         |
        270 
```

### The solar system

The game view always shows you all the planets in the solar system and the two players. The complete solar system area simulated is exactly 9 times the size of the game view. Any missile with sufficient velocity to leave the solar system is gone forever, you'll need to take another shot.

Planets are your primary obstacle. Each planet is created with a random radius and density. The planet's mass, and in turn its gravity, is a function of its radius and density. Smaller, rocky planets are the most dense. Large gas giants are the least dense. Ice giants make up quarter of the planets as do the gas giants. Most common of all are the planets with earth-like masses, making up just less than half the planets. Very small rocky planets are the least common of all.

In the settings menu you can choose the numbers of planets that are randomly generated for each solar system.

Alongside planets you can use the settings menu to enable the existence of black holes. Black holes are the most dense objects of all and come in a variety of sizes. They are much rarer than the other planet types. When a black hole is present they are hard to make out but one clue is that they block out the background stars behind them. Black holes come in two varieties those with event horizons and naked singularities. Naked singularities are the rarest of all. When a missile strikes an event horizon it will be absorbed by the black hole. Naked singularities, which do not have event horizons, can not be hit but they exert powerful gravitational forces over anything that passes too near.

In the settings menu you can choose whether or not your solar systems can included Black Holes or Naked Singularities.

### Config

You can edit various settings in the config.ini file. Max Missile flight time, the gravitational constant and the total bounds of the solar system are probably the only ones worth looking at. Though you could choose to play on giant playfields if you desire.

## Installation

Fully portable installation should work with:

```
git clone https://github.com/DanBuchan/gravity_wars_redux.git
cd gravity_wars_redux
pip install -r requirements.txt
python main.py
```

Executable packages coming soon.

## TODO

1. Sound effects for the missiles, launching, traveling, striking planets, striking players and striking black holes
2. Package for OSX and win11
3. Nicer pixel art menus
4. Procedural generation of pixel art planet textures
5. net play
6. Music?
7. Refactor players classes to inherit from a parent player class
8. Amiga AGA port
9. Spectrum Next port