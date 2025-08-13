1. start and show menu
    select options
2. start game
    randomly select player locations
    randomly select and places planets/black holes as per options
        avoiding players
3. Players turns
    player 1 selects heading and velocity and presses fire
    player 2 selects heading and velocisty and presses fire
    calculate paths. if one hits declare winner or return to 3
4. If win show congrats and return to menu

## Menu details

About
- a little help text and some blurb about sending some cash
Help
- info about max velocity and the heading angle directions
Game Control
- random setup - draws a random screen
- play game - starts the game
- replay the map you just used (or start if you haven't yet)
- stop game
- quit
Options
- set max planets
- toggle removing the missle trails as they fire or not
- redraw screen - redraw the map removing the missile trails
- practice/compete - toggle single player mode (only one ship shoots, the player gets to choose which ship to be)
- toggle sound on or off
Modify Setup
- move ship
- move planet/blackhole
- make planet
- make blackhole
- delete planet/blackhole

## ADDITIONS:

1. Add toggle for naked blackholes or ones with event horizons
Ones with event horizons should add gravity based on the velocity of the missile that hits them
2. Turns or simultaneous fire 
3. net play?

## TODOS:

1. Refactor Player classes to inherit from master player class