import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button

def create_text_area(screen, x, y, width, height, dialogue_text, colour, bordercolour):
    return Button(screen,  x, y, width, height, text=dialogue_text,
                radius=2, onClick=lambda: None, 
                borderThickness=2, textColour=(20, 20, 20),
                borderColour=bordercolour, inactiveColour=colour,
                hoverColour=colour, pressedColour=colour,
                textHAlign="left", textVAlign="top", hoverBorderColour=bordercolour,
                pressedBorderColour=bordercolour, margin=5,
                font=pygame.font.SysFont('bold', 16))

def create_text_input(screen, x, y, width, height, field_text, verify_angle, colour, bordercolour):
    field = TextBox(screen, x, y, width, height, fontSize=12,
                borderColour=bordercolour, textColour=(0, 0, 0),
                colour=colour, radius=2, borderThickness=2, onTextChanged=verify_angle,
                placeholderText=field_text)
    field.textOffsetTop = 12 // 3 + 2
    return(field)

def create_submit_button(screen, screenwidth, callback, player, states, text, colour, bordercolour): 
    return Button(screen, screenwidth-60-10, 10, 60, 20, text=text,
                fontSize=14, radius=2, onClick=callback, onClickParams=[player, states], 
                borderThickness=2,
                borderColour=bordercolour,
                inactiveColour=colour,
                hoverColour=colour,
                pressedColour=colour,
                hoverBorderColour=bordercolour,
                pressedBorderColour=bordercolour)
