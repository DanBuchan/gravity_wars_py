import pygame
import pygame_menu
from pygame_menu import themes
 
import random
import configparser
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

config = configparser.ConfigParser()
config.read('config.ini')
settings = {
    'ScreenWidth': int(config['DEFAULT']['ScreenWidth']),
    'ScreenHeight': int(config['DEFAULT']['ScreenHeight']),
    'MinPlanets': int(config['DEFAULT']['MinPlanets']),
    'MaxPlanets': int(config['DEFAULT']['MaxPlanets']),
    'Player1Name': config['DEFAULT']['Player1Name'],
    'Player2Name': config['DEFAULT']['Player2Name'],
    'Blackholes': eval(config['DEFAULT']['Blackholes']),
    'NakedBlackholes': eval(config['DEFAULT']['NakedBlackholes']),
    'RemoveTrails': eval(config['DEFAULT']['RemoveTrails']),
    'MusicVolume': int(config['DEFAULT']['MusicVolume']),
    'SFXVolume': int(config['DEFAULT']['SFXVolume']),
}

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
 
def start_the_game():
    pass
 
def settings_menu():
    mainmenu._open(setting)
def about_menu():
    mainmenu._open(about)

mainmenu = pygame_menu.Menu('Welcome', 640, 512, 
                                 theme=themes.THEME_SOLARIZED)
mainmenu.add.button('Start', start_the_game)
mainmenu.add.button('Settings', settings_menu)
mainmenu.add.button('About', about_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
setting = pygame_menu.Menu('Settings', 640, 512, 
                                 theme=themes.THEME_BLUE)
setting.add.text_input('Player 1 Name: ', default=settings['Player1Name'], maxchar=20)
setting.add.text_input('Player 2 Name: ', default=settings['Player2Name'], maxchar=20)
setting.add.range_slider('Pick a discrete range',
                      (settings['MinPlanets'],
                       settings['MaxPlanets']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1)
setting.add.toggle_switch('Allow Blackholes', settings['Blackholes'], toggleswitch_id='blackholes')
setting.add.toggle_switch('Allow Naked Blackholes', settings['NakedBlackholes'], toggleswitch_id='nakedblackholes')
setting.add.toggle_switch('Erase Missle Trails', settings['RemoveTrails'], toggleswitch_id='trails')

about = pygame_menu.Menu('About', 640, 512, 
                                 theme=themes.THEME_BLUE)
ABOUT = "This is a remake of Ed Bartz Gravity Wars 2"
about.add.label(ABOUT, max_char=-1, font_size=20)

mainmenu.mainloop(screen)

while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()