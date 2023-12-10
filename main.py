# All code for Undead Uprising
# Lines 1 - 25 Basic Setup of Game Screen Settings (libraries, init, size)
# Lines 26 - 169 Character Classes (attributes, functions, etc.)
# Lines 170 - 211 Zombie Classes and Generating
# Lines 212 - 287 Start Menu
# Lines 288 - 383 Game Play Functions (movement detection, border, health bar, back button, etc.)
# Lines 384 - 388 Tutorial
# Lines 389 - 399 Game Settings (logo, title, character, state)
# Lines 400 - End Main Loop of Game (while loop, time, fps, etc.)

import pygame
from pygame.locals import *
import sys
import ctypes
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
time = 0

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
    orig_health = 100

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
        if Quinn.clicked:
            screen.blit(Quinn.h_quinn, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Quinn.char_img, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))

    def special():
        screen.blit(logo, (0, 0))

class Theresa():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_hospital.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/theresa.png')
    player_img = pygame.image.load('images/characters/player_theresa.png')
    h_theresa = pygame.image.load('images/characters/h_theresa.png')
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
        if Theresa.clicked:
            screen.blit(Theresa.h_theresa, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Theresa.char_img, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))

    def special():
        screen.blit(logo, (0, 0))

class Jekyll():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_snow_ice.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/jekyll.png')
    player_img = pygame.image.load('images/characters/player_jekyll.png')
    h_jekyll = pygame.image.load('images/characters/h_jekyll.png')
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
        if Jekyll.clicked:
            screen.blit(Jekyll.h_jekyll, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))
        else:
            screen.blit(Jekyll.char_img, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))

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
    
    def move(self, charX, charY, zombieX, zombieY):
        dx, dy = charX - zombieX, charY - zombieY
        stepx, stepy = dx / fps, dy / fps
        normalZombie.x -= stepx
        normalZombie.y -= stepy

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

# Detects events during start menu state
def detect_start_menu():
    global game_state, character, player

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_z:
            shop()

    # Detects if a button was pressed
    if event.type == pygame.MOUSEBUTTONDOWN:

        # Sets player to character clicked
        if screen_w * 0.28 <= mouse[0] <= screen_w * 0.28 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = John()
            if John.clicked:
                John.clicked = not John.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = True, False, False, False, False, False
            print('John is picked')
        elif screen_w * (0.28 + 0.077) <= mouse[0] <= screen_w * (0.28 + 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Tony()
            if Tony.clicked:
                Tony.clicked = not Tony.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, True, False, False, False, False
            print('Tony is picked')
        elif screen_w * (0.28 + 2 * 0.077) <= mouse[0] <= screen_w * (0.28 + 2 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Swift()
            if Swift.clicked:
                Swift.clicked = not Swift.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, True, False, False, False
            print('Swift is picked')
        elif screen_w * (0.28 + 3 * 0.077) <= mouse[0] <= screen_w * (0.28 + 3 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Quinn()
            if Quinn.clicked:
                Quinn.clicked = not Quinn.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, True, False, False
            print('Quinn is picked')
        elif screen_w * (0.28 + 4 * 0.077) <= mouse[0] <= screen_w * (0.28 + 4 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Theresa()
            if Theresa.clicked:
                Theresa.clicked = not Theresa.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, False, True, False
            print('Theresa is picked')
        elif screen_w * (0.28 + 5 * 0.077) <= mouse[0] <= screen_w * (0.28 + 5 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            player = Jekyll()
            if Jekyll.clicked:
                Jekyll.clicked = not Jekyll.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, False, False, True
            print('Jekyll is picked')
        
        # Changes game state to game_play if start button is clicked
        elif screen_w / 2 - 200 <= mouse[0] <= screen_w / 2 - 50 and screen_h - 140 <= mouse[1] <= screen_h - 80:
            # if the start button was pressed, set the game state to game_play, which executes the next part of the game
            game_state = "game_play"
        
        # Changes game state to tutorial if  tutorial button is clicked
        elif 30 <= mouse[0] <= 105 and screen_h - 105 <= mouse[1] <= screen_h - 30:
            game_state = "tutorial"

        # Quits the game
        elif screen_w / 2 + 50 <= mouse[0] <= screen_w / 2  + 200 and screen_h - 140 <= mouse[1] < screen_h - 80:
            sys.exit()

# ----------------------------------- Shop -----------------------------------

points = 1500

shop_items = {
    "quinn" : False, 
    "theresa" : False, 
    "jekyll" : False,
    "heal" : 0,
    "shield" : 0,
    "dmg" : 0
}

def shop():
    # Images, text, etc.
    font = pygame.font.SysFont('consolas', 30) # sets the font family and font size
    title1 = font.render('CHARACTERS', True, (0, 0, 0))
    title2 = font.render('POWER UPS', True, (0, 0, 0))
    darken = pygame.transform.scale(pygame.image.load("images/darken.png"), (screen_w, screen_h))
    shop_title = pygame.transform.scale(pygame.image.load("images/SHOP_title.png"), (685/3.5, 200/3.5))
    shop_bg = pygame.transform.scale(pygame.image.load("images/shop_bg.png"), (screen_w * 0.8, screen_h * 0.7))
    quinn = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (75, 75))
    quinn_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    theresa = pygame.transform.scale(pygame.image.load("images/characters/circle_theresa.png"), (75, 75))
    theresa_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    jekyll = pygame.transform.scale(pygame.image.load("images/characters/circle_jekyll.png"), (75, 75))
    jekyll_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    heal = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (75, 75))
    heal_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    shield = pygame.transform.scale(pygame.image.load("images/characters/circle_theresa.png"), (75, 75))
    shield_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    damage = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (75, 75))
    dmg_def = pygame.transform.scale(pygame.image.load("images/characters/quinn_definition.png"), (365 / 3, 190 / 3))
    back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4.5, 155/4.5))
    buy_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4.5, 155/4.5))

    # Display images and text
    screen.blit(darken, (0, 0))
    screen.blit(shop_title, ((screen_w - 685/3.5) / 2, 50))
    screen.blit(shop_bg, (screen_w * 0.1, 150))
    screen.blit(title1, (300, 185))
    screen.blit(title2, (800, 185))
    screen.blit(quinn, (175, 250))
    screen.blit(quinn_def, (275, 255))
    screen.blit(theresa, (175, 350))
    screen.blit(theresa_def, (275, 355))
    screen.blit(jekyll, (175, 450))
    screen.blit(jekyll_def, (275, 455))
    screen.blit(heal, (screen_w / 2 + 50, 250))
    screen.blit(heal_def, (screen_w / 2 + 150, 255))
    screen.blit(shield, (screen_w / 2 + 50, 350))
    screen.blit(shield_def, (screen_w / 2 + 150, 355))
    screen.blit(damage, (screen_w / 2 + 50, 450))
    screen.blit(dmg_def, (screen_w / 2 + 150, 455))
    screen.blit(buy_button, (500, screen_h - 150))
    screen.blit(back_button, (screen_w - 600, screen_h - 150))
    

# ----------------------------------- Game Play -----------------------------------

# Top bar
def bar(health, orig_health):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screen_w, 80))
    draw_health_bar(health, orig_health)
    power_ups()

# Displays health bar
def draw_health_bar(health, orig_health):
    border = pygame.transform.scale(pygame.image.load('images/bar_border.png'), (400, 30))
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
    pygame.draw.rect(screen, color, (85, 25, (health / orig_health) * 400, 30))
    screen.blit(border, (85, 25))
    screen.blit(text, (25, 30))

# Displays power-ups
def power_ups():
    grey_heal = pygame.transform.scale(pygame.image.load("images/test_char.png"), (50, 50))
    grey_shield = pygame.transform.scale(pygame.image.load("images/test_char.png"), (50, 50))
    grey_damage = pygame.transform.scale(pygame.image.load("images/test_char.png"), (50, 50))
    heal = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (50, 50))
    shield = pygame.transform.scale(pygame.image.load("images/characters/circle_theresa.png"), (50, 50))
    damage = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (50, 50))
    items = font.render('Items', True, (255, 255, 255))
    screen.blit(items, (screen_w - 300 - items.get_width(), 30))

    if shop_items['heal'] == 1:
        screen.blit(heal, (screen_w - 250, 15))
    else:
        screen.blit(grey_heal, (screen_w - 250, 15))
    
    if shop_items['shield'] == 1:
        screen.blit(shield, (screen_w - 175, 15))
    else:
        screen.blit(grey_shield, (screen_w - 175, 15))
    
    if shop_items['dmg'] == 1:
        screen.blit(damage, (screen_w - 100, 15))
    else:
        screen.blit(grey_damage, (screen_w - 100, 15))

# Default character settings - player, position, speed
player = John()
charX = screen_w / 2 - 18
charY = screen_h / 2 - 28
charX_change = 0
charY_change = 0
speed = 5

# Detects events during game play state
def movement():
    global charX, charY, charX_change, charY_change, mouse, game_state, player, speed, shop_display

    # Detects key pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            charX_change = -speed
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            charX_change = speed
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            charY_change = -speed
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            charY_change = speed
        if event.key == pygame.K_b:
            shop_display = not shop_display

    # Detects key released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            charX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
            charY_change = 0
    
    # Detects back button clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if screen_w - 510/4 - 30 <= mouse[0] <= screen_w - 30 and screen_h - 155/4 - 30 <= mouse[1] <= screen_h - 30:
            detect_start_menu()
            charX = screen_w / 2 - 18
            charY = screen_h / 2 - 28
            charX_change = 0
            charY_change = 0
            speed = 4
            game_state = 'start_menu'

# Creates a border around the screen that stops the character from moving out of screen
def border():
    global charX, charY, charX_change, charY_change
    if charX <= 5:
        charX = 5
    if charX >= screen_w - 38:
        charX = screen_w - 38
    if charY <= 5:
        charY = 5
    if charY >= screen_h - 60:
        charY = screen_h - 60

# Back button images
back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4, 155/4))
h_back_button = pygame.transform.scale(pygame.image.load("images/h_BACK_button.png"), (510/4, 155/4))

# Game Play Function
def play(collides, shop_display):
    global player, charX, charY, charX_change, charY_change, game_state, clock    
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
        collides += 1
        if collides > 60:
            collide = False
        else:
            player.health -= 1
        print('collided')
    
    # Game end
    if player.health == 0:
        game_state = 'game_over'
    
    # Display shop screen
    if shop_display:
        shop()
    test.move(charX, charY, test.x, test.y)

def game_over():
    # Images
    game_over_screen = pygame.transform.scale(pygame.image.load("images/game_over_screen.png"), (screen_w, screen_h))
    try_again = pygame.transform.scale(pygame.image.load("images/TRY_AGAIN_button.png"), (1000/3, 150/3))
    quit = pygame.transform.scale(pygame.image.load("images/QUIT_button.png"), (250*0.9, 100*0.9))

    # Display images
    screen.blit(game_over_screen, (0, 0))
    screen.blit(try_again, (200, screen_h - 150))
    screen.blit(quit, (screen_w - 500, screen_h - 175))

# ----------------------------------- Tutorial -----------------------------------

def tutorial():
    screen.blit(logo, (0, 0))

# ----------------------------------- Game Details -----------------------------------

# Setting the game name and logo
pygame.display.set_caption("Undead Uprising")
logo = pygame.image.load('images/test_char.png')
pygame.display.set_icon(logo)

# State of game and character choice
game_state = "start_menu" # start_menu, game_play, or tutorial
character = "John" # default character

# ----------------------------------- Main Loop of Game -----------------------------------

# Keeps track of game time
running = True
collides = 0
shop_display = False

while running:
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        if game_state == 'start_menu':
            detect_start_menu()
        elif game_state == 'game_play':
            movement()
    if game_state == 'start_menu':
        startMenu()
    elif game_state == 'game_play':
        collides = 0
        play(collides, shop_display)
    elif game_state == 'game_over':
        game_over()
    elif game_state == 'tutorial':
        tutorial()
    pygame.display.update()
    clock.tick(fps)

print(time)
