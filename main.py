import pygame
import pygame_menu
from pygame_menu import themes
import random
import time
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import re

from config import settings, set_settings
from menu import *
from sprites import *
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

def output():
    # Get text in the textbox
    print(player1_angle_input.getText())
    print(player1_velocity_input.getText())

number_pattern = re.compile('^[1234567890]*\.*[1234567890]*$')

def verify_angle():
    text = player1_angle_input.getText()
    if len(text) == 0:
        return
    if re.search(number_pattern, text):
        value = float(text)
        if value < 0:
            player1_angle_input.setText('000.0000')
        if value >= 360:
            player1_angle_input.setText('359.9999')
    else:
        player1_angle_input.setText('')
    return None
    
def verify_velocity():
    text = player1_velocity_input.getText()
    if len(text) == 0:
        return
    if re.search(number_pattern, text):
        value = float(text)
        if value < 0:
            player1_velocity_input.setText('0.0000')
        if value > 10:
            player1_velocity_input.setText('10.0000')
    else:
        player1_velocity_input.setText('')
    return None
    
player1_id = Button(screen, 10, 10, 65, 20, text='Player 1',
                radius=2, onClick=lambda: None, 
                borderThickness=2, textColour=(20, 20, 20),
                borderColour=(200, 200,200), inactiveColour=(220,220,220),
                hoverColour=(220,220,220), pressedColour=(220, 220, 220),
                textHAlign="left", hoverBorderColour=(200,200,200),
                pressedBorderColour=(200,200,200), margin=6,
                font=pygame.font.SysFont('bold', 16))
angle_dialogue = Button(screen, 80, 10, 85, 20, text='Angle (0-360)',
                radius=2, onClick=lambda: None,
                borderThickness=2, textColour=(20, 20, 20),
                borderColour=(200, 200,200), inactiveColour=(220,220,220),
                hoverColour=(220,220,220), pressedColour=(220, 220, 220),
                textHAlign="left", textVAlign="top", hoverBorderColour=(200,200,200),
                pressedBorderColour=(200,200,200), margin=5,
                font=pygame.font.SysFont('bold', 16))
player1_angle_input = TextBox(screen, 165, 10, 65, 20, fontSize=12,
                  borderColour=(200, 200,200), textColour=(0, 0, 0),
                  radius=2, borderThickness=2, onTextChanged=verify_angle,
                  placeholderText="000.0000")
player1_angle_input.textOffsetTop = 12 // 3 + 2
velocity_dialogue = Button(screen, 235, 10, 90, 20, text='Velocity (0-10)',
                radius=2, onClick=lambda: None,
                borderThickness=2, textColour=(20, 20, 20),
                borderColour=(200, 200,200), inactiveColour=(220,220,220),
                hoverColour=(220,220,220), pressedColour=(220, 220, 220),
                textHAlign="left", hoverBorderColour=(200,200,200),
                pressedBorderColour=(200,200,200), margin=5,
                font=pygame.font.SysFont('bold', 16))
player1_velocity_input = TextBox(screen, 325, 10, 60, 20, fontSize=12,
                  borderColour=(200, 200,200), textColour=(20, 20, 20),
                  radius=2, borderThickness=2,
                  placeholderText="1.0000", onTextChanged=verify_velocity, )  
player1_velocity_input.textOffsetTop = 12 // 3 + 2 
submit_button = Button(screen, settings['ScreenWidth']-60-10, 10, 60, 20, text='Submit',
                fontSize=14, radius=2, onClick=output, 
                borderThickness=2)


running = True
frame_count = 0
# Build menu
def run_the_game(play1, play2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove, alternate):
    
    set_settings(play1, play2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove, alternate)
    print(settings)

    game_running = True
    generate_sprites = True
    input_player_1 = False
    player1 = None
    player2 = None
    planets = None
    missiles = None
    all_sprites = None
    while game_running:
        random.seed(settings["Seed"])
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
        if generate_sprites:
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
            time.sleep(1)
            generate_sprites = False
            input_player_1 = True
            
        if input_player_1:
            # create the widgets afresh with the current value
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