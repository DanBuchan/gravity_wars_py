import pygame
import pygame_menu
from pygame_menu import themes
import random
import time
import re

from config import settings, set_settings
from menu import *
from sprites import *
from ui_widgets import *
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
area_to_save = pygame.Rect(0, 0, settings['ScreenWidth'], settings['ScreenHeight'])
temp_screen = pygame.Surface(area_to_save.size)

# Game states
# 1: generating the sprites
# 2: generating the player 1 widgets
# 3: waiting/accepting player 1 input
# 4: generating the player 2 widgets
# 5: waiting/accepting player 2 input
# 6: animating missiles player 1
# 7: animating missiles player 2
# 8: animating both missiles
# 9: end of game state - win or draw    
player1_id = None
angle_dialogue = None
player1_angle_input = None
velocity_dialogue = None
player1_velocity_input = None
submit_button = None
player2_id = None
player2_angle_input = None
player2_velocity_input = None
running = True
frame_count = 0

def run_the_game(play1, play2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove, alternate):
    
    set_settings(play1, play2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove, alternate)
    print(settings)

    game_running = True
    player1 = None
    player2 = None
    planets = None
    missiles = None
    all_sprites = None
    states = {'sprite_gen': True,
              'p1_widget_gen': False,
              'p1_input': False,
              'p2_widget_gen': False,
              'p2_input': False,
              'clear_ui': False,
              'p1_missiles': False,
              'p2_missiles': False,
              'both_missiles': False,
              'end_game': False,
              }
    while game_running:
        random.seed(settings["Seed"])
        # random.seed(132988714769)
        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    game_running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                game_running = False
        # Using these ifs to handle game states. Not the best way apparently but it'll do
        if states['sprite_gen']:
            # Instantiate players.
            player1 = Player1(settings)
            player2 = Player2(settings)
            planets = pygame.sprite.Group()
            # missiles = pygame.sprite.Group()
            all_sprites = pygame.sprite.Group()
            all_sprites.add(player1)
            all_sprites.add(player2)
            screen.fill((0, 0, 0))
            # GENERATE STAR FIELD/BACKGROUND
            
            planet_count = random.randint(settings['MinPlanets'],
                                          settings['MaxPlanets'])
            accepted_count = 0
            while True:
                tmp_planet = Planet(settings)
                accept_planet = True
                for sprite in all_sprites:
                    dist = pygame.math.Vector2(tmp_planet.rect.center[0]+tmp_planet.x, tmp_planet.rect.center[1]+tmp_planet.y).distance_to((sprite.rect.center[0]+sprite.x, sprite.rect.center[1]+sprite.y))
                    spacing = player1.sprite_dim_x
                    if hasattr(sprite, 'radius'):
                        spacing = sprite.radius+5
                    if dist <= tmp_planet.radius+spacing:
                        accept_planet = False
                if accept_planet:
                    all_sprites.add(tmp_planet)
                    screen.blit(tmp_planet.image, (tmp_planet.x, tmp_planet.y))
                    accepted_count += 1    
                if accepted_count == planet_count:
                    break
            
            screen.blit(player1.surf, (player1.x, player1.y))
            screen.blit(player1.canon, (player1.canon_x, player1.canon_y))
            screen.blit(player2.surf, (player2.x, player2.y))
            screen.blit(player2.canon, (player2.canon_x, player2.canon_y))
            
            pygame.display.flip()
            temp_screen.blit(screen, (0, 0), area_to_save) 
            time.sleep(1)
            states['sprite_gen'] = False
            states['p1_widget_gen'] = True
            
        if states['p1_widget_gen']:            
            player1_id = create_text_area(screen, 10, 10, 65, 20, 'Player 1',(180, 180, 240), (160, 160, 220))
            angle_dialogue = create_text_area(screen, 80, 10, 85, 20, 'Angle (0-360)', (180, 180, 240), (160, 160, 220))
            player1_angle_input = create_text_input(screen, 165, 10, 65, 20, player1.angle_text, 0, 360, '000.0000', '359.9999', (180, 180, 240), (160, 160, 220))
            velocity_dialogue = create_text_area(screen, 235, 10, 90, 20, 'Velocity (0-10)', (180, 180, 240), (160, 160, 220))
            player1_velocity_input = create_text_input(screen, 325, 10, 60, 20, player1.velocity_text, 0, 10, '0.0000', '10.0000', (180, 180, 240), (160, 160, 220))
            submit_button = create_submit_button(screen, settings['ScreenWidth'], player1, states, player1_angle_input, player1_velocity_input, 'p1_input', 'p2_widget_gen', "Submit", (220, 220, 180), (220, 220, 160))
            # create the widgets afresh with the current value
            states['p1_widget_gen'] = False
            states['p1_input'] = True

        if states['p1_input']:
            pygame_widgets.update(events)
            pygame.display.update()

        if states['p2_widget_gen']:
            player1_id.hide()
            player1_angle_input.hide()
            player1_velocity_input.hide()
            submit_button.hide()
            player2_id = create_text_area(screen, 10, 10, 65, 20, 'Player 2', (240, 180, 180), (220, 160, 160))
            angle_dialogue = create_text_area(screen, 80, 10, 85, 20, 'Angle (0-360)', (240, 180, 180), (220, 160, 160))
            player2_angle_input = create_text_input(screen, 165, 10, 65, 20, player2.angle_text, 0, 360, '000.0000', '359.9999', (240, 180, 180), (220, 160, 160))
            velocity_dialogue = create_text_area(screen, 235, 10, 90, 20, 'Velocity (0-10)', (240, 180, 180), (220, 160, 160))
            player2_velocity_input = create_text_input(screen, 325, 10, 60, 20, player2.velocity_text, 0, 10, '0.0000', '10.0000', (240, 180, 180), (220, 160, 160))
            
            
            submit_2_button = create_submit_button(screen, settings['ScreenWidth'], player2, states, player2_angle_input, player2_velocity_input, 'p2_input', 'clear_ui', "Fire", (255, 120, 120), (200, 120, 120))
            # create the widgets afresh with the current value
            states['p2_widget_gen'] = False
            states['p2_input'] = True

        if states['p2_input']:
            pygame_widgets.update(events)
            pygame.display.update()
            # render p1 ui and await inputs
            # after inputs blit saved screen back to screen
            # if alternating animate p1 missiles
                #blit screen state to saved screen
                # render p2 ui and await inputs
                # after inputs blit saved screen back to screen
                # animate p2 missiles
            # else render p2 ui and await inputs
                # after inputs blit saved screen back to screen
                # animate p1 and p2 missiles
        
        if states['clear_ui']:
            screen.blit(temp_screen, (0, 0), area_to_save) 
            fire_state = "p1_missiles"
            if not settings['Alternate']:
                fire_state = 'both_missiles'
            states[fire_state] = True
            states['clear_ui'] = False

        if states['p1_missiles']:
            print(player1.angle, player1.velocity)

            pygame.display.update()
            #https://stackoverflow.com/questions/37976237/saving-modified-screens-in-python-pygame-for-later-use
            # https://pygamewidgets.readthedocs.io/en/latest/

        if states['p2_missiles']:
            print(player2.angle, player2.velocity)

            pygame.display.update()
            #https://stackoverflow.com/questions/37976237/saving-modified-screens-in-python-pygame-for-later-use
            # https://pygamewidgets.readthedocs.io/en/latest/
        if states['both_missiles']:
            print(player1.angle, player1.velocity)
            print(player2.angle, player2.velocity)
            pygame.display.update()
            #https://stackoverflow.com/questions/37976237/saving-modified-screens-in-python-pygame-for-later-use
            # https://pygamewidgets.readthedocs.io/en/latest/

        pygame.display.flip()
            # loop over planets and draw each one
            #start player 1 input loop    
        clock.tick(60)
        # print("game done")
        #game_running=False
    return()

mainmenu = pygame_menu.Menu('Welcome', 640, 512, 
                                     theme=themes.THEME_SOLARIZED)
    
settingmenu = pygame_menu.Menu('Settings', 640, 512, 
                               theme=themes.THEME_BLUE)
build_menu(mainmenu, settingmenu, settings, run_the_game)
while running:
    # Look at every event in the queue
    mainmenu.mainloop(screen)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()