# Gravity Wars Redux

This is a python remake of Ed Bartz's old Amiga PD game Gravity Wars. First released in September of 1987. This was the first Amiga game I ever played so it holds something a place in my heart.

This version includes a number of tweaks and additions largely to make it a little more interesting. But the game as a whole is much the same. One omission is the ability to build your own levels. It seldom results in play fields as interesting as the RNG gods grant us.

The goal of the game is to hit your opponent with you missiles, avoiding the planets and using their gravity to your advantage.

The mathematics that drive this version are derived largely from Grav War by Sohrab Ismail-Beigi (currently at Yale if you wish to look him up). You can find the sources for this at, http://pascal.sources.ru/games/gravwar2.htm. The code in Gravity Wars Redux is actually ported from Gravity Wars JS by Eric A Meyer, see: https://gravitywars.meyerweb.com/. This is largely because it was somewhat easier for me to port the Javascript code rather than the original pascal.

If you wish to play with the maths then check the included test_gravity_sim.py script. This will simulate multiple centres of gravity and one shot. Planetary volumes and. collision detection is omitted in this script, but you should get the idea.

## To play

Each player takes it in turn to select a missile firing angle and a velocity for their shot. The first player to strike the other wins. Your previous selected values are shown on subsequent shots, you only need to edit the values you want to change, the previously value will be used otherwise. Missiles will fly for 90 seconds until they run out of fuel.

In the settings menu you can control whether or not missile trails persist throughout the game or are erased after each round. Having the trails erased makes the game a little harder. You can also choose to toggle whether you take turns or fire simultaneously. When playing with simultaneously shots it is possible to draw. When you take turns player 1 has the advantage, this is the default as with the original Gravity Wars.

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

The game view always shows you all the planets in the solar system and the two players. The complete solar system area simulated is exactly 9 times the size of the game view. Any missile with sufficient velocity to leave the solar system is gone forever.

Planets are your primary obstacle. Each planet gets a random radius and density. The planet's mass, and in turn its gravity, is a function of its radius and density. Smaller, rocky planets are the most dense. Large gas giants are the least dense.

Ice giants make up quarter of the planets as do the gas giants. Most common of all are the planets with earth-like masses, making up just less than half the planets. Very small rocky planets are the least common of all.

In the settings menu you can choose the numbers of planets that are randomly generated.

Alongside planets you can use the settings menu to enable the existence of black holes. Black holes are the most dense objects of all and come in a variety of sizes. They are much rarer than the other planet types. When a black hole is present they are hard to make out but one clue is that they will block out the background stars. Black holes come in two varieties those with event horizons and naked singularities. Naked singularities are the rarest of all. When a missiles strikes an event horizon it will be absorbed by the black hole. Naked singularities, which do not have event horizons can not be hit but the exert powerful gravitational forces.

In the settings menu you can choose whether or not your solar systems can included Black Holes or Naked Singularities.

### Config

You can edit various settings in the config.ini file. Max Missile flight time, the gravitational constant and the total bounds of the solar system are probably the only ones worth looking at.

## TODO

1. Sound effects for the missiles, launching, traveling, striking planets, striking players and striking black holes
2. Package for OSX and win11
3. Nicer pixel art menus
4. Procedural generation of pixel art planet textures
5. net play
6. Music?
7. Save and input seeds
8. Refactor players classes to inherit from a parent player class