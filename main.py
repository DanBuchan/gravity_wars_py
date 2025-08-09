import pygame
import pygame_menu
from pygame_menu import themes
 
import random
from config import settings, set_settings
from sprites import Player1, Player2, Planet, Blackhole, Missile
# from menu import mainmenu
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()

# maybe we'll load some background music...
# pygame.mixer.music.load("sounds/Apoxode_-_Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)

# explosion = pygame.mixer.Sound("")
# hit_rocky_planet = pygame.mixer.Sound("")
# hit_gas_giant = pygame.mixer.Sound("")
# hit_event_horizon = pygame.mixer.Sound("")
screen = pygame.display.set_mode([settings['ScreenWidth'],
                                  settings['ScreenHeight']])

# Instantiate players.
player1 = Player1()
player2 = Player2()

planets = pygame.sprite.Group()
missiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

running = True
frame_count = 0

# Create settings class
# Build menu

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def run_the_game(play1, play2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove):
    
    set_settings(play1, play2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove)
    game_running = True
    while game_running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    game_running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                game_running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # draw player 1
        # draw player 2
        # loop over planets and draw each one

        #start player 1 input loop

        clock.tick(60)
        print("game done")
        return()
 
def settings_menu():
    mainmenu._open(settingmenu)
def about_menu():
    mainmenu._open(about)

settingmenu = pygame_menu.Menu('Settings', 640, 512, 
                                 theme=themes.THEME_BLUE)
player1name = settingmenu.add.text_input('Player 1 Name: ', default=settings['Player1Name'], maxchar=20)
player2name = settingmenu.add.text_input('Player 2 Name: ', default=settings['Player2Name'], maxchar=20)
planetNumber = settingmenu.add.range_slider('Pick Number of Planets',
                      (settings['MinPlanets'],
                       settings['MaxPlanets']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1)
allowBlackholes = settingmenu.add.toggle_switch('Allow Blackholes', settings['Blackholes'], toggleswitch_id='blackholes')
allowNakedBlackholes = settingmenu.add.toggle_switch('Allow Naked Blackholes', settings['NakedBlackholes'], toggleswitch_id='nakedblackholes')
removeTrails = settingmenu.add.toggle_switch('Erase Missile Trails', settings['RemoveTrails'], toggleswitch_id='removetrails')

about = pygame_menu.Menu('About', 640, 512, 
                                 theme=themes.THEME_BLUE)
ABOUT = "This is a remake of Ed Bartz Gravity Wars 2"
about.add.label(ABOUT, max_char=-1, font_size=20)

mainmenu = pygame_menu.Menu('Welcome', 640, 512, 
                                 theme=themes.THEME_SOLARIZED)
mainmenu.add.button('Start', run_the_game, player1name, 
                    player2name, planetNumber, 
                    allowBlackholes, 
                    allowNakedBlackholes,
                    removeTrails)
mainmenu.add.button('Settings', settings_menu)
mainmenu.add.button('About', about_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

while running:
    # Look at every event in the queue
    mainmenu.mainloop(screen)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()