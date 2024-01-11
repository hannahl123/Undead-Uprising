# All code for Undead Uprising
# Lines 1 - 30 Basic Setup of Game Screen Settings (libraries, init, size)
# Lines 31 - 187 Character Classes (attributes, functions, etc.)
# Lines 188 - 236 Zombie Classes and Generating
# Lines 237 - 338 Start Menu
# Lines 339 - 466 Shop
# Lines 467 - 686 Game Play Functions (game over, movement detection, top bar, border, health bar, back button, etc.)
# Lines 687 - 711 Background Stories
# Lines 712 - 719 Tutorial
# Lines 720 - 730 Game Details (logo, title, character, state)
# Lines 731 - 765 Main Loop of Game (while loop, time, fps, etc.)

import pygame
from pygame.locals import *
import sys
import ctypes
import math
import random

pygame.init()

# ---------------------------------------- Screen Settings ----------------------------------------

# Setting size of screen to full screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen_w, screen_h = true_res[0], true_res[1]
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
font = pygame.font.SysFont('consolas', 30) # sets the font family and font size
fps = 60
clock = pygame.time.Clock()

# ---------------------------------------- Characters ----------------------------------------
class John():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/john.png')
    player_img = pygame.image.load('images/characters/player_john.png')
    h_john = pygame.image.load('images/characters/h_john.png')
    clicked = False
    orig_health = 100

    def __init__(self):
        self.clicked = False
        self.img = John.char_img
        self.health = 100
        self.player_img = John.player_img
        self.area = pygame.Surface([35, 55])
        self.rect = self.area.get_rect()
        self.speed = 'normal'

    def show():
        if John.clicked:
            screen.blit(John.h_john, (screen_w * 0.28, screen_h / 2 + 20))
        else:
            screen.blit(John.char_img, (screen_w * 0.28, screen_h / 2 + 20))

class Tony():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/tony.png')
    player_img = pygame.image.load('images/characters/player_tony.png')
    h_tony = pygame.image.load('images/characters/h_tony.png')
    clicked = False
    orig_health = 100

    def __init__(self):
        self.clicked = False
        self.img = Tony.char_img
        self.health = 100
        self.player_img = Tony.player_img
        self.area = pygame.Surface([35, 55])
        self.rect = self.area.get_rect()
        self.speed = 'normal'

    def show():
        if Tony.clicked:
            screen.blit(Tony.h_tony, (screen_w * (0.28 + 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Tony.char_img, (screen_w * (0.28 + 0.077), screen_h / 2 + 20))

class Swift():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_track.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/swift.png')
    player_img = pygame.image.load('images/characters/player_swift.png')
    h_swift = pygame.image.load('images/characters/h_swift.png')
    clicked = False
    orig_health = 75

    def __init__(self):
        self.clicked = False
        self.img = Swift.char_img
        self.health = 75
        self.player_img = Swift.player_img
        self.area = pygame.Surface([35, 55])
        self.rect = self.area.get_rect()
        self.speed = 'fast'

    def show():
        if Swift.clicked:
            screen.blit(Swift.h_swift, (screen_w * (0.28 + 2 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Swift.char_img, (screen_w * (0.28 + 2 * 0.077), screen_h / 2 + 20))

class Quinn():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_magma.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/quinn.png')
    player_img = pygame.image.load('images/characters/player_quinn.png')
    h_quinn = pygame.image.load('images/characters/h_quinn.png')
    grey_quinn = pygame.image.load('images/characters/grey_quinn.png')
    clicked = False
    orig_health = 120

    def __init__(self):
        self.clicked = False
        self.img = Quinn.char_img
        self.health = 120
        self.player_img = Quinn.player_img
        self.area = pygame.Surface([35, 55])
        self.rect = self.area.get_rect()
        self.speed = 'normal'

    def show():
        if Quinn.clicked and shop_items["quinn"] == True:
            screen.blit(Quinn.h_quinn, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Quinn.char_img, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))
        if shop_items["quinn"] == False:
            screen.blit(Quinn.grey_quinn, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))

    def special():
        screen.blit(logo, (0, 0))

class Theresa():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_hospital.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/theresa.png')
    player_img = pygame.image.load('images/characters/player_theresa.png')
    h_theresa = pygame.image.load('images/characters/h_theresa.png')
    grey_theresa = pygame.image.load('images/characters/grey_theresa.png')
    clicked = False
    orig_health = 120

    def __init__(self):
        self.clicked = False
        self.img = Theresa.char_img
        self.health = 120
        self.player_img = Theresa.player_img
        self.area = pygame.Surface([37, 55])
        self.rect = self.area.get_rect()
        self.speed = 'normal'

    def show():
        if Theresa.clicked and shop_items["theresa"] == True:
            screen.blit(Theresa.h_theresa, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Theresa.char_img, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))
        if shop_items["theresa"] == False:
            screen.blit(Theresa.grey_theresa, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))

    def special():
        screen.blit(logo, (0, 0))

class Jekyll():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_snow_ice.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/jekyll.png')
    player_img = pygame.image.load('images/characters/player_jekyll.png')
    h_jekyll = pygame.image.load('images/characters/h_jekyll.png')
    grey_jekyll = pygame.image.load('images/characters/grey_jekyll.png')
    clicked = False
    orig_health = 120

    def __init__(self):
        self.clicked = False
        self.img = Jekyll.char_img
        self.health = 120
        self.player_img = Jekyll.player_img
        self.area = pygame.Surface([39, 59])
        self.rect = self.area.get_rect()
        self.speed = 'fast'

    def show():
        if Jekyll.clicked and shop_items["jekyll"] == True:
            screen.blit(Jekyll.h_jekyll, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Jekyll.char_img, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))
        if shop_items["jekyll"] == False:
            screen.blit(Jekyll.grey_jekyll, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))

    def special():
        screen.blit(logo, (0, 0))

# ---------------------------------------- Zombies ----------------------------------------

all_sprites = pygame.sprite.Group() 

class normalZombie:
    zombie_full_health = pygame.image.load('images/zombies/norm_zombie_full_health.png')
    zombie_half_health = pygame.image.load('images/zombies/norm_zombie_half_health.png')
    health = 2
    x = 100
    y = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = normalZombie.health
        self.full_health = normalZombie.zombie_full_health
        self.half_health = normalZombie.zombie_half_health
        self.area = pygame.Surface([35, 55])
        self.rect = self.area.get_rect()
    
    def show():
        if normalZombie.health == 2:
            screen.blit(normalZombie.zombie_full_health, (normalZombie.x, normalZombie.y))
        elif normalZombie.health == 1:
            screen.blit(normalZombie.zombie_half_health, (normalZombie.x, normalZombie.y))
        else:
            screen.blit(logo, (normalZombie.x, normalZombie.y))

def generate():
    randNum = random.randint(0, 3)
    if randNum == 0: # appear from top border
        randX, randY = random.randint(0, screen_w - 35), 100
    elif randNum == 1: # appear from right border
        randX, randY = screen_w - 35, random.randint(100, screen_h - 60)
    elif randNum == 2: # appear from bottom border
        randX, randY = random.randint(0, screen_w - 35), screen_h - 60
    else: # appear from left border
        randX, randY = screen_w - 35, random.randint(100, screen_h - 60)
    zombie = normalZombie(randX, randY)
    zombie.rect.x = zombie.x
    zombie.rect.y = zombie.y
    return zombie

test = generate()

# ----------------------------------- Start Menu -----------------------------------

def startMenu():
    # Images and Text
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png'), (screen_w, screen_h))
    title_img = pygame.image.load('images/UNDEAD UPRISING.png')
    text = font.render('Pick your character', True, (255, 255, 255))
    border = pygame.transform.scale(pygame.image.load('images/border.png'), (700, 200))
    tutorial_b = pygame.transform.scale(pygame.image.load('images/TUTORIAL_button.png'), (115, 115))
    start_b = pygame.transform.scale(pygame.image.load('images/START_button.png'), (150, 60))
    quit_b = pygame.transform.scale(pygame.image.load('images/QUIT_button.png'), (150, 60))

    # Display images, text and buttons
    screen.blit(bg, (0, 0)) # background
    screen.blit(title_img, ((screen_w - 800) / 2, 125)) # title
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, 250)) # instruction
    screen.blit(border, (screen_w / 2 - 350, screen_h / 2 - 50)) # border
    screen.blit(start_b, (screen_w / 2 - 200, screen_h - 140))
    screen.blit(quit_b, (screen_w / 2 + 55, screen_h - 140))
    screen.blit(tutorial_b, (25, screen_h - 25 - 115))

    # Display all character images
    John.show()
    Tony.show()
    Swift.show()
    Quinn.show()
    Theresa.show()
    Jekyll.show()

picked_character = ""

# Detects events during start menu state
def detect_start_menu():
    global game_state, character, player, picked_character

    # Detects if a button was pressed
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Sets player to character clicked
        if screen_w * 0.28 <= mouse[0] <= screen_w * 0.28 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = John()
            picked_character = "John"
            if John.clicked:
                John.clicked = not John.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = True, False, False, False, False, False
            print('John is picked')
        elif screen_w * (0.28 + 0.077) <= mouse[0] <= screen_w * (0.28 + 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Tony()
            picked_character =  "Tony"
            if Tony.clicked:
                Tony.clicked = not Tony.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, True, False, False, False, False
            print('Tony is picked')
        elif screen_w * (0.28 + 2 * 0.077) <= mouse[0] <= screen_w * (0.28 + 2 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Swift()
            picked_character = "Swift"
            if Swift.clicked:
                Swift.clicked = not Swift.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, True, False, False, False
            print('Swift is picked')
        # Special characters
        elif shop_items["quinn"] == True and screen_w * (0.28 + 3 * 0.077) <= mouse[0] <= screen_w * (0.28 + 3 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Quinn()
            picked_character = "Quinn"
            if Quinn.clicked:
                Quinn.clicked = not Quinn.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, True, False, False
            print('Quinn is picked')
        elif shop_items["theresa"] == True and screen_w * (0.28 + 4 * 0.077) <= mouse[0] <= screen_w * (0.28 + 4 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Theresa()
            picked_character = "Theresa"
            if Theresa.clicked:
                Theresa.clicked = not Theresa.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, False, True, False
            print('Theresa is picked')
        elif shop_items["jekyll"] == True and screen_w * (0.28 + 5 * 0.077) <= mouse[0] <= screen_w * (0.28 + 5 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Jekyll()
            picked_character = "Jekyll"
            if Jekyll.clicked:
                Jekyll.clicked = not Jekyll.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, False, False, True
            print('Jekyll is picked')

        # If start button clicked, load background story
        elif screen_w / 2 - 200 <= mouse[0] <= screen_w / 2 - 50 and screen_h - 140 <= mouse[1] <= screen_h - 80:
            # if the start button was pressed, set the game state to game_play, which executes the next part of the game
            game_state = "bg_story"
        
        # Changes game state to tutorial if  tutorial button is clicked
        elif 30 <= mouse[0] <= 105 and screen_h - 105 <= mouse[1] <= screen_h - 30:
            game_state = "tutorial"

        # Quits the game
        elif screen_w / 2 + 50 <= mouse[0] <= screen_w / 2  + 200 and screen_h - 140 <= mouse[1] < screen_h - 80:
            sys.exit()

# ----------------------------------- Shop -----------------------------------

points = 1600

shop_items = {
    "quinn" : False, 
    "theresa" : False, 
    "jekyll" : False,
    "med_kit" : False,
    "speed_potion" : False,
    "bomb" : False
}

costs = {
    "quinn" : 1500,
    "theresa" : 1500,
    "jekyll" : 1500,
    "med_kit" : 100,
    "speed_potion" : 100,
    "bomb" : 100
}

selected = ""

def shop(mouse):
    global selected, shop_display, points

    # Images, text, etc.
    font = pygame.font.SysFont('consolas', 30) # sets the font family and font size
    title1 = font.render('CHARACTERS', True, (0, 0, 0))
    title2 = font.render('POWER UPS', True, (0, 0, 0))
    darken = pygame.transform.scale(pygame.image.load("images/darken.png"), (screen_w, screen_h))
    shop_title = pygame.transform.scale(pygame.image.load("images/SHOP_title.png"), (685/3.5, 200/3.5))
    shop_bg = pygame.transform.scale(pygame.image.load("images/shop_bg.png"), (screen_w * 0.8, screen_h * 0.7))
    back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4.5, 155/4.5))
    buy_button = pygame.transform.scale(pygame.image.load("images/BUY_button.png"), (818/8.7, 300/8.7))

    # Character images and definitions
    quinn = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (80, 80))
    normal_quinn = pygame.transform.scale(pygame.image.load("images/characters/normal_quinn.png"), (80, 80))
    quinn_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    theresa = pygame.transform.scale(pygame.image.load("images/characters/circle_theresa.png"), (80, 80))
    normal_theresa = pygame.transform.scale(pygame.image.load("images/characters/normal_theresa.png"), (80, 80))
    theresa_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    jekyll = pygame.transform.scale(pygame.image.load("images/characters/circle_jekyll.png"), (80, 80))
    normal_jekyll = pygame.transform.scale(pygame.image.load("images/characters/normal_jekyll.png"), (80, 80))
    jekyll_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    
    # Power-up images and definitions
    normal_med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/normal_med_kit.png"), (80, 80))
    med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/circled_med_kit.png"), (80, 80))
    med_kit_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    normal_speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/normal_speed_potion.png"), (80, 80))
    speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/circled_speed_potion.png"), (80, 80))
    speed_potion_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    normal_bomb = pygame.transform.scale(pygame.image.load("images/power-ups/normal_bomb.png"), (80, 80))
    bomb = pygame.transform.scale(pygame.image.load("images/power-ups/circled_bomb.png"), (80, 80))
    bomb_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))

    # Sign
    sign = pygame.image.load("images/test_char.png")
    text = font.render("NOT ENOUGH POINTS", True, (0, 0, 0))

    # Display images and text
    screen.blit(darken, (0, 0))
    screen.blit(shop_title, ((screen_w - 685/3.5) / 2, 50))
    screen.blit(shop_bg, (screen_w * 0.1, 150))
    screen.blit(title1, (300, 185))
    screen.blit(title2, (800, 185))
    screen.blit(normal_theresa, (175, 350))
    screen.blit(normal_quinn, (175, 250))
    screen.blit(normal_jekyll, (175, 450))
    screen.blit(normal_med_kit, (screen_w / 2 + 50, 250))
    screen.blit(normal_speed_potion, (screen_w / 2 + 50, 350))
    screen.blit(normal_bomb, (screen_w / 2 + 50, 450))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if shop_items["quinn"] == False and 175 <= mouse[0] <= 250 and 250 <= mouse[1] <= 325:
            screen.blit(quinn, (175, 250))
            selected = "quinn"
        elif shop_items["theresa"] == False and 175 <= mouse[0] <= 250 and 350 <= mouse[1] <= 425:
            screen.blit(theresa, (175, 350))
            selected = "theresa"
        elif shop_items["jekyll"] == False and 175 <= mouse[0] <= 250 and 450 <= mouse[1] <= 525:
            screen.blit(jekyll, (175, 450))
            selected = "jekyll"
        elif shop_items["med_kit"] == False and screen_w / 2 + 50 <= mouse[0] <= screen_w / 2 + 100 and 250 <= mouse[1] <= 300:
            screen.blit(med_kit, (screen_w / 2 + 50, 250))
            selected = "med_kit"
        elif shop_items["speed_potion"] == False and screen_w / 2 + 50 <= mouse[0] <= screen_w / 2 + 100 and 350 <= mouse[1] <= 400:
            screen.blit(speed_potion, (screen_w / 2 + 50, 350))
            selected = "speed_potion"
        elif shop_items["bomb"] == False and screen_w / 2 + 50 <= mouse[0] <= screen_w / 2 + 100 and 450 <= mouse[1] <= 500:
            screen.blit(bomb, (screen_w / 2 + 50, 450))
            selected = "bomb"
        elif 500 <= mouse[0] <= 500 + 818/8.7 and screen_h - 150 <= mouse[1] <= screen_h - 150 + 300/8.7:
            if points >= costs[selected]:
                shop_items[selected] = not shop_items[selected]
                points -= costs[selected]
                selected = "buy"
                shop_display = not shop_display
            else:
                screen.blit(text, (screen_w / 2 - text.get_width() / 2, screen_h / 2))
        elif screen_w - 600 <= mouse[0] <= screen_w - 600 + 510/4.5 and screen_h - 150 <= mouse[1] <= screen_h - 150 + 155/4.5:
            shop_display = not shop_display

    if selected == "quinn":
        screen.blit(quinn, (175, 250))
    elif selected == "theresa":
        screen.blit(theresa, (175, 350))
    elif selected == "jekyll":
        screen.blit(jekyll, (175, 450))
    elif selected == "med_kit":
        screen.blit(med_kit, (screen_w / 2 + 50, 250))
    elif selected == "speed_potion":
        screen.blit(speed_potion, (screen_w / 2 + 50, 350))
    elif selected == "bomb":
        screen.blit(bomb, (screen_w / 2 + 50, 450))

    screen.blit(quinn_def, (275, 255))
    screen.blit(theresa_def, (275, 355))
    screen.blit(jekyll_def, (275, 455))
    screen.blit(med_kit_def, (screen_w / 2 + 150, 255))
    screen.blit(speed_potion_def, (screen_w / 2 + 150, 355))
    screen.blit(bomb_def, (screen_w / 2 + 150, 455))
    screen.blit(buy_button, (500, screen_h - 150))
    screen.blit(back_button, (screen_w - 600, screen_h - 150))

# ----------------------------------- Game Play -----------------------------------

# Top bar
def bar(health, orig_health):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screen_w, 80))
    draw_health_bar(health, orig_health)
    power_ups()
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, 30))

# Displays health bar
def draw_health_bar(health, orig_health):
    border = pygame.transform.scale(pygame.image.load('images/bar_border.png'), (300, 30))
    font = pygame.font.SysFont('consolas', 30) # sets the font family and font size
    text = font.render(str(int(health)), True, (255, 255, 255))
    if health > 70:
        color = (0, 255, 0)
    elif health > 50:
        color = (173, 255, 47)
    elif health > 20:
        color = (255, 150, 50)
    else:
        color = (255, 0, 0)
    pygame.draw.rect(screen, color, (85, 25, (health / orig_health) * 300, 30))
    screen.blit(border, (85, 25))
    screen.blit(text, (25, 30))

# Displays power-ups
def power_ups():
    grey_med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/grey_med_kit.png"), (50, 50))
    grey_speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/grey_speed_potion.png"), (56 * (50/35), 35 * (50/35)))
    grey_bomb = pygame.transform.scale(pygame.image.load("images/power-ups/grey_bomb.png"), (27 * (50/32), 32 * (50/32)))
    
    med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/coloured_med_kit.png"), (50, 50))
    speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/coloured_speed_potion.png"), (56 * (50/35), 35 * (50/35)))
    bomb = pygame.transform.scale(pygame.image.load("images/power-ups/coloured_bomb.png"), (27 * (50/32), 32 * (50/32)))
    
    items = font.render('Items', True, (255, 255, 255))
    screen.blit(items, (screen_w - 300 - items.get_width(), 30))

    if shop_items['med_kit'] == True:
        screen.blit(med_kit, (screen_w - 240, 15))
    else:
        screen.blit(grey_med_kit, (screen_w - 240, 15))
    
    if shop_items['speed_potion'] == True:
        screen.blit(speed_potion, (screen_w - 175, 15))
    else:
        screen.blit(grey_speed_potion, (screen_w - 175, 15))
    
    if shop_items['bomb'] == True:
        screen.blit(bomb, (screen_w - 85, 15))
    else:
        screen.blit(grey_bomb, (screen_w - 85, 15))

# Bullets
class Bullet:
    bullet_img = pygame.image.load('images/test_char.png')
    def __init__(self, x, y, mouse): # pass in current character position
        self.x = x
        self.y = y
        self.x2 = mouse[0]
        self.y2 = mouse[1]
        self.img = Bullet.bullet_img
        self.area = pygame.Surface([10, 10])
        self.rect = self.area.get_rect()
        self.speed = 2
        self.vdist = mouse[1] - y
        self.hdist = mouse[0] - x
    
    def update_pos(self, x, y, vx, vy):
        Bullet.x += 2

# Default character settings - player, position, speed
player = John()
charX = screen_w / 2 - 18
charY = screen_h / 2 - 28
charX_change = 0
charY_change = 0
speed = -6
diagspeed = -4

# Detects events during game play state
def movement():
    global charX, charY, charX_change, charY_change, mouse, game_state, player, speed, shop_display
    pressed = pygame.key.get_pressed()
    # Detects key pressed
    if pressed[pygame.K_b]:
            shop_display = not shop_display

    if pressed[pygame.K_w] and not pressed[pygame.K_s] and not pressed[pygame.K_a] and not pressed[pygame.K_d]:
       charX_change = 0
       charY_change = speed
    if pressed[pygame.K_s] and not pressed[pygame.K_w] and not pressed[pygame.K_a] and not pressed[pygame.K_d]:
       charX_change = 0
       charY_change = -speed
    if pressed[pygame.K_a] and not pressed[pygame.K_w] and not pressed[pygame.K_s] and not pressed[pygame.K_d]:
       charX_change = speed
       charY_change = 0
    if pressed[pygame.K_d] and not pressed[pygame.K_w] and not pressed[pygame.K_s] and not pressed[pygame.K_a]:
       charX_change = -speed
       charY_change = 0
    
    if pressed[pygame.K_w] and pressed[pygame.K_a] and not pressed[pygame.K_s] and not pressed[pygame.K_d]:
       charX_change = diagspeed
       charY_change = diagspeed
    if pressed[pygame.K_w] and pressed[pygame.K_s] and not pressed[pygame.K_a] and not pressed[pygame.K_wd]:
        charX_change = 0
        charY_change = 0
    if pressed[pygame.K_w] and pressed[pygame.K_d] and not pressed[pygame.K_a] and not pressed[pygame.K_s]:
        charX_change = -diagspeed
        charY_change = diagspeed
    if pressed[pygame.K_a] and pressed[pygame.K_s] and not pressed[pygame.K_w] and not pressed[pygame.K_d]:
        charX_change = diagspeed
        charY_change = -diagspeed
    if pressed[pygame.K_a] and pressed[pygame.K_d] and not pressed[pygame.K_s] and not pressed[pygame.K_w]:
        charX_change = 0
        charY_change = 0
    if pressed[pygame.K_s] and pressed[pygame.K_d] and not pressed[pygame.K_w] and not pressed[pygame.K_a]:
        charX_change = -diagspeed
        charY_change = -diagspeed
    
    if pressed[pygame.K_w] and pressed[pygame.K_a] and pressed[pygame.K_s] and not pressed[pygame.K_d]:
        charX_change = speed
        charY_change = 0
    if pressed[pygame.K_w] and pressed[pygame.K_a] and pressed[pygame.K_d] and not pressed[pygame.K_s]:
        charX_change = 0
        charY_change = speed
    if pressed[pygame.K_w] and pressed[pygame.K_s] and pressed[pygame.K_d] and not pressed[pygame.K_a]:
        charX_change = -speed
        charY_change = 0
    if pressed[pygame.K_a] and pressed[pygame.K_s] and pressed[pygame.K_d] and not pressed[pygame.K_w]:
        charX_change = 0
        charY_change = -speed
    
    if pressed[pygame.K_w] and pressed[pygame.K_a] and pressed[pygame.K_s] and pressed[pygame.K_d]:
        charX_change = 0
        charY_change = 0

    if not pressed[pygame.K_s] and not pressed[pygame.K_w] and not pressed[pygame.K_a] and not pressed[pygame.K_d]:
       charX_change = 0
       charY_change = 0
    
    # Detects back button clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if screen_w - 510/4 - 30 <= mouse[0] <= screen_w - 30 and screen_h - 155/4 - 30 <= mouse[1] <= screen_h - 30:
            detect_start_menu()
            charX = screen_w / 2 - 18
            charY = screen_h / 2 - 28
            charX_change = 0
            charY_change = 0
            game_state = 'start_menu'

# Creates a border around the screen that stops the character from moving out of screen
def border():
    global charX, charY, charX_change, charY_change
    if charX <= 5:
        charX = 5
    if charX >= screen_w - 38:
        charX = screen_w - 38
    if charY <= 85:
        charY = 85
    if charY >= screen_h - 60:
        charY = screen_h - 60

# Back button images
back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4, 155/4))
h_back_button = pygame.transform.scale(pygame.image.load("images/h_BACK_button.png"), (510/4, 155/4))

# Game Play Function
def play(shop_display, mouse):
    global player, charX, charY, charX_change, charY_change, game_state, clock, points
    border()
    # Basic screen set-up
    screen.blit(player.bg, (0, 80))
    screen.blit(test.zombie_full_health, (test.x, test.y))
    screen.blit(player.player_img, (charX, charY))
    bar(player.health, player.orig_health)
    screen.blit(back_button, (screen_w - 510/4 - 30, screen_h - 155/4 - 30))

    # Character movement changes
    charX += charX_change
    charY += charY_change
    player.rect.x = charX
    player.rect.y = charY

    all_sprites.update() 
    all_sprites.draw(screen)
    
    # Detect collision between character and zombie
    collide = pygame.Rect.colliderect(player.rect, test.rect)
    
    if collide:
        points += 1
        player.health -= 1
        print('collided')

    # Game end
    if player.health == 0:
        game_state = 'game_over'
    
    # Display shop screen
    if shop_display:
        shop(mouse)

def game_over():
    # Images
    game_over_screen = pygame.transform.scale(pygame.image.load("images/game_over_screen.png"), (screen_w, screen_h))
    try_again = pygame.transform.scale(pygame.image.load("images/TRY_AGAIN_button.png"), (325, 50))
    quit = pygame.transform.scale(pygame.image.load("images/QUIT_button.png"), (225, 90))

    # Display images
    screen.blit(game_over_screen, (0, 0))
    screen.blit(try_again, (200, screen_h - 150))
    screen.blit(quit, (screen_w - 500, screen_h - 175))

# ----------------------------------- Background Stories -----------------------------------
            
def background_story():
    global picked_character, game_state
    john = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png"), (screen_w, screen_h))
    tony = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png"), (screen_w, screen_h))
    swift = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png"), (screen_w, screen_h))
    quinn = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png"), (screen_w, screen_h))
    theresa = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png"), (screen_w, screen_h))
    jekyll = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png"), (screen_w, screen_h))
    continue_button = pygame.transform.scale(pygame.image.load("images/CONTINUE_button.png"), (275, 40))
    if picked_character == "John":
        screen.blit(john, (0, 0))
    elif picked_character == "Tony":
        screen.blit(tony, (0, 0))
    elif picked_character == "Swift":
        screen.blit(swift, (0, 0))
    elif picked_character == "Quinn":
        screen.blit(quinn, (0, 0))
    elif picked_character == "Theresa":
        screen.blit(theresa, (0, 0))
    elif picked_character == "Jekyll":
        screen.blit(jekyll, (0, 0))
    screen.blit(continue_button, (screen_w - 350, screen_h - 100))   

# ----------------------------------- Tutorial -----------------------------------

def tutorial():
    tut = pygame.transform.scale(pygame.image.load("images/backgrounds/Tutorial.png"), (screen_w, screen_h))
    back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4, 155/4))
    screen.blit(tut, (0, 0))
    screen.blit(back_button, (screen_w - 200, screen_h - 100))

# ----------------------------------- Game Details -----------------------------------

# Setting the game name and logo
pygame.display.set_caption("Undead Uprising")
logo = pygame.image.load('images/test_char.png')
pygame.display.set_icon(logo)

# State of game and character choice
game_state = "start_menu" # start_menu, bg_story, game_play, or tutorial
character = "John" # default character

# ----------------------------------- Main Loop of Game -----------------------------------

running = True
shop_display = False

while running:
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            shop_display = not shop_display
        if game_state == "start_menu":
            detect_start_menu()
        elif game_state == "bg_story":
            if event.type == pygame.MOUSEBUTTONDOWN and screen_w - 350 <= mouse[0] <= screen_w - 75 and screen_h - 100 <= mouse[1] <= screen_h - 60:
                game_state = "game_play"
        elif game_state == "game_play":
            movement()
        elif game_state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= mouse[0] <= 525 and screen_h - 150 <= mouse[1] <= screen_h - 100:
                    game_state = "start_menu"
    if game_state == "start_menu":
        startMenu()
    elif game_state == "bg_story":
        background_story()
    elif game_state == "game_play":
        play(shop_display, mouse)
    elif game_state == "game_over":
        game_over()
    elif game_state == "tutorial":
        tutorial()
    pygame.display.update()
    clock.tick(fps)
