import pygame_menu
from pygame_menu import themes

def settings_menu(mainmenu, settingmenu):
    mainmenu._open(settingmenu)
def about_menu(mainmenu, about):
    mainmenu._open(about)

def build_menu(mainmenu, settingmenu, settings, run_the_game):
    player1name = settingmenu.add.text_input('Player 1 Name: ', default=settings['Player1Name'], maxchar=20)
    player2name = settingmenu.add.text_input('Player 2 Name: ', default=settings['Player2Name'], maxchar=20)
    planetNumber = settingmenu.add.range_slider('Pick Number of Planets',
                          (settings['MinPlanets'],
                           settings['MaxPlanets']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1)
    allowBlackholes = settingmenu.add.toggle_switch('Allow Blackholes', settings['Blackholes'], toggleswitch_id='blackholes')
    allowNakedBlackholes = settingmenu.add.toggle_switch('Allow Naked Blackholes', settings['NakedBlackholes'], toggleswitch_id='nakedblackholes')
    removeTrails = settingmenu.add.toggle_switch('Erase Missile Trails', settings['RemoveTrails'], toggleswitch_id='removetrails')
    alternateTurns = settingmenu.add.toggle_switch('Aternate Turns', settings['Alternate'], toggleswitch_id='alternateturns')
    
    about = pygame_menu.Menu('About', 640, 512, 
                                     theme=themes.THEME_BLUE)
    ABOUT = "This is a remake of Ed Bartz Gravity Wars 2"
    about.add.label(ABOUT, max_char=-1, font_size=20)
    
    mainmenu.add.button('Start', run_the_game, player1name, 
                        player2name, planetNumber, 
                        allowBlackholes, 
                        allowNakedBlackholes,
                        removeTrails, alternateTurns)
    mainmenu.add.button('Settings', settings_menu, mainmenu, settingmenu)
    mainmenu.add.button('About', about_menu, mainmenu, about)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)
