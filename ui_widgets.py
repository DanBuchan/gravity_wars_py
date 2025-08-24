import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button

def create_text_area(screen, x, y, width, height, dialogue_text):
    return Button(screen,  x, y, width, height, text=dialogue_text,
                radius=2, onClick=lambda: None, 
                borderThickness=2, textColour=(20, 20, 20),
                borderColour=(200, 200,200), inactiveColour=(220,220,220),
                hoverColour=(220,220,220), pressedColour=(220, 220, 220),
                textHAlign="left", textVAlign="top", hoverBorderColour=(200,200,200),
                pressedBorderColour=(200,200,200), margin=5,
                font=pygame.font.SysFont('bold', 16))

def create_text_input(screen, x, y, width, height, field_text, verify_angle):
    field = TextBox(screen, x, y, width, height, fontSize=12,
                borderColour=(200, 200,200), textColour=(0, 0, 0),
                radius=2, borderThickness=2, onTextChanged=verify_angle,
                placeholderText=field_text)
    field.textOffsetTop = 12 // 3 + 2
    return(field)

def create_submit_button(screen, screenwidth, callback): 
    return Button(screen, screenwidth-60-10, 10, 60, 20, text='Submit',
                fontSize=14, radius=2, onClick=callback, 
                borderThickness=2)
