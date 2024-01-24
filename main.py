# Undead Uprising
# Updated as of January 22, 2024
# Lines 15 - 27 Imports and Initialization
# Lines 28 - 80 Game Settings and Details
# Lines 81 - 86 Sprite Groups
# Lines 87 - 300 Character Classes
# Lines 301 - 371 Zombie Classes and Auto-generation
# Lines 372 - 400 Background Stories
# Lines 401 - 540 Start Menu
# Line 541 - 555 Tutorial
# Lines 556 - 660 Shop
# Lines 661 - 883 Game Play Functions (top menu bar, movement, reset character stats, game over, etc.)
# Lines 884 - 922 Bullet Shooting
# LInes 923 - 933 Reset Game After Round
# Lines 934 - ### Main Loop of Game

# ----------------------------------- Imports and Initialization -----------------------------------

import pygame
from pygame.locals import *
from pygame import mixer
import random, time, math, ctypes, sys
import pygame.gfxdraw

pygame.init()
mixer.init()

# ----------------------------------- Game Settings and Global Variables -----------------------------------

# Setting size of screen to full screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen_w, screen_h = 1280, 720
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)

# Setting the game name and logo
pygame.display.set_caption("Undead Uprising")
logo = pygame.image.load('images/test_char.png').convert_alpha()
pygame.display.set_icon(logo)

# Font, Time, and Control Variables
font = pygame.font.SysFont('consolas', 30) # sets the font family and font size
fps = 60
clock = pygame.time.Clock()
shop_display = False
zombies_allowed = True
paused = False
paused_screen = pygame.transform.scale(pygame.image.load("images/paused_screen.png").convert_alpha(), (screen_w, screen_h))
acc = 0
hovering_tutorial_b = False
hovering_start_b = False
hovering_quit_b = False

# Character speed variables
extraspeed = 0
extraspeed_duration = 300
extraspeed_timer = 0
charX_change = 0
charY_change = 0
speed = -5
diagspeed = -3.5

# Zombie generation time variables
last_zombie_time = time.time()
zombie_generation_rate = 0.25
player_health_decrease_timer = time.time()
in_well = -1
well_death = False

# Back button images
back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png").convert_alpha(), (130, 40))
high_back_button = pygame.transform.scale(pygame.image.load("images/highlighted_buttons/highlighted_BACK_button.png").convert_alpha(), (130, 40))

# Bullet variables
timetoshoot = 0
attackspeed = 50

# Jekyll's trail variables
trails = []
timetotrail = 0
trailspeed = 0

# ----------------------------------- Sprite Groups -----------------------------------

all_sprites = pygame.sprite.Group() 
zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# ----------------------------------- Character Classes -----------------------------------

class John(pygame.sprite.Sprite):
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png').convert_alpha(), (screen_w, screen_h))
    h_john = pygame.image.load('images/characters/h_john.png').convert_alpha()
    char_img = pygame.image.load('images/characters/john.png').convert_alpha()
    clicked = False
    orig_health = 100

    def __init__(self):
        super().__init__()
        self.health = 100
        self.image = pygame.image.load('images/characters/player_john.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_w // 2, screen_h // 2))

    def show():
        if John.clicked:
            screen.blit(John.h_john, (screen_w * 0.28, screen_h / 2 + 20))
            John.music()
        else:
            screen.blit(John.char_img, (screen_w * 0.28, screen_h / 2 + 20))

    def music():
        mixer.music.load('background_music/earth.mp3')
        mixer.music.play(-1)

class Tony(pygame.sprite.Sprite):
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png').convert_alpha(), (screen_w, screen_h))
    h_tony = pygame.image.load('images/characters/h_tony.png').convert_alpha()
    char_img = pygame.image.load('images/characters/tony.png').convert_alpha()
    clicked = False
    orig_health = 200

    def __init__(self):
        super().__init__()
        self.health = 200
        self.image = pygame.image.load('images/characters/player_tony.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_w // 2, screen_h // 2))

    def show():
        if Tony.clicked:
            screen.blit(Tony.h_tony, (screen_w * (0.28 + 0.077), screen_h / 2 + 20))
            Tony.music()
        else:
            screen.blit(Tony.char_img, (screen_w * (0.28 + 0.077), screen_h / 2 + 20))
    
    def music():
        mixer.music.load('background_music/tony.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)

class Swift(pygame.sprite.Sprite):
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_track.png').convert_alpha(), (screen_w, screen_h))
    h_swift = pygame.image.load('images/characters/h_swift.png').convert_alpha()
    char_img = pygame.image.load('images/characters/swift.png').convert_alpha()
    clicked = False
    orig_health = 50

    def __init__(self):
        super().__init__()
        self.health = 50
        self.image = pygame.image.load('images/characters/player_swift.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_w // 2, screen_h // 2))

    def show():
        if Swift.clicked:
            screen.blit(Swift.h_swift, (screen_w * (0.28 + 2 * 0.077), screen_h / 2 + 20))
            Swift.music()
        else:
            screen.blit(Swift.char_img, (screen_w * (0.28 + 2 * 0.077), screen_h / 2 + 20))
    
    def music():
        mixer.music.load('background_music/rainbow.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)

class Quinn(pygame.sprite.Sprite):
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_magma.png').convert_alpha(), (screen_w, screen_h))
    h_quinn = pygame.image.load('images/characters/h_quinn.png').convert_alpha()
    char_img = pygame.image.load('images/characters/quinn.png').convert_alpha()
    grey_quinn = pygame.image.load('images/characters/grey_quinn.png')
    clicked = False
    orig_health = 135

    def __init__(self):
        super().__init__()
        self.health = 135
        self.image = pygame.image.load('images/characters/player_quinn.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_w//2, screen_h//2))

    def show():
        if Quinn.clicked and shop_items["quinn"] == True:
            screen.blit(Quinn.h_quinn, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))
            Quinn.music()
        else:
            screen.blit(Quinn.char_img, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))
        if shop_items["quinn"] == False:
            screen.blit(Quinn.grey_quinn, (screen_w * (0.28 + 3 * 0.077), screen_h / 2 + 20))

    def music():
        mixer.music.load('background_music/quinn.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)

class Theresa(pygame.sprite.Sprite):
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_hospital.png').convert_alpha(), (screen_w, screen_h))
    h_theresa = pygame.image.load('images/characters/h_theresa.png').convert_alpha()
    char_img = pygame.image.load('images/characters/theresa.png').convert_alpha()
    grey_theresa = pygame.image.load('images/characters/grey_theresa.png').convert_alpha()
    clicked = False
    orig_health = 120

    def __init__(self):
        super().__init__()
        self.health = 120
        self.image = pygame.image.load('images/characters/player_theresa.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_w//2, screen_h//2))

    def show():
        if Theresa.clicked and shop_items["theresa"] == True:
            screen.blit(Theresa.h_theresa, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))
            Theresa.music()
        else:
            screen.blit(Theresa.char_img, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))
        if shop_items["theresa"] == False:
            screen.blit(Theresa.grey_theresa, (screen_w * (0.28 + 4 * 0.077), screen_h / 2 + 20))

    def music():
        mixer.music.load('background_music/hospital.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)

    timetoregen = 180

    def special(self):
        Theresa.timetoregen -= 1
        if Theresa.timetoregen == 0:
            if player.health < 120:
                player.health += 1
            Theresa.timetoregen = 180

class Jekyll(pygame.sprite.Sprite):
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_lab.png').convert_alpha(), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/jekyll.png').convert_alpha()
    h_jekyll = pygame.image.load('images/characters/h_jekyll.png').convert_alpha()
    grey_jekyll = pygame.image.load('images/characters/grey_jekyll.png').convert_alpha()
    clicked = False
    orig_health = 100

    def __init__(self):
        super().__init__()
        self.health = 100
        self.image = pygame.image.load('images/characters/player_jekyll.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_w//2, screen_h//2))

    def show():
        if Jekyll.clicked and shop_items["jekyll"] == True:
            screen.blit(Jekyll.h_jekyll, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))
            Jekyll.music()
        else:
            screen.blit(Jekyll.char_img, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))
        if shop_items["jekyll"] == False:
            screen.blit(Jekyll.grey_jekyll, (screen_w * (0.28 + 5 * 0.077), screen_h / 2 + 20))

    def music():
        mixer.music.load('background_music/snow.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)

# Jekyll's special trail feature
class Trail:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.frame_count = 0  # Add a frame count variable
        self.max_frames = 50  # Set the maximum number of frames

        self.trail = pygame.Surface((70, 70), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(self.trail, 30, 30, 30, (50, 200, 50, 30))
        pygame.gfxdraw.filled_circle(self.trail, 30, 30, 30, (50, 200, 50, 30))
        self.speed = 0

    def update(self):  
        self.pos = (self.pos)
        self.frame_count += 1
        if self.frame_count >= self.max_frames:
            trails.remove(self)  # Remove the trail after max_frames frames

    def draw(self, surf):
        trail_rect = self.trail.get_rect(center=self.pos)
        surf.blit(self.trail, trail_rect) 

def trailfunction():
    global timetotrail
    global trailspeed
    pos = (player.rect.x+20+random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5]), player.rect.y+54+random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5]))
    if game_state == "game_play":
        if timetotrail <= 1:
            if picked_character == "Jekyll":
                trails.append(Trail(*pos))
                timetotrail = (trailspeed)

    for trail in trails:
        trail.update()  # Update the trail
        trail.draw(screen)

    timetotrail -= 1

def detect_collision(zombies, trails):
    for zombie in zombies:
        for trail in trails:
            if zombie.rect.colliderect(trail.trail.get_rect(center=trail.pos)):
                zombie.health -= 0.0005
                if zombie.health <= 1 and not zombie.health <= 0:
                    zombie.image = zombie.half_health_image
                elif zombie.health <= 0:
                    zombie.kill()

# ----------------------------------- Zombie Classes and Auto-generation -----------------------------------

class shieldZombie(pygame.sprite.Sprite):
    identity = "shield"

    def __init__(self, target):
        super().__init__()
        self.health = 3
        self.full_health_image = pygame.image.load("images/zombies/shield_zombie_full_health.png").convert_alpha()
        self.two_health_image = pygame.image.load("images/zombies/shield_zombie_two_health.png").convert_alpha()
        self.one_health_image = pygame.image.load("images/zombies/shield_zombie_one_health.png").convert_alpha()
        self.image = self.full_health_image
        self.rect = self.image.get_rect()
        self.target = target
        self.speed = random.uniform(2, 4) # Random speed between 1 and 3
    
    def update(self):
        # Calculate direction towards the player
        dx = self.target.rect.x - self.rect.x
        dy = self.target.rect.y - self.rect.y
        distance = math.sqrt(dx**2 + dy**2)

        # Move towards the player
        if distance > 0:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed

class Zombie(pygame.sprite.Sprite):
    identity = "normal"

    def __init__(self, target):
        super().__init__()
        self.health = 2
        self.full_health_image = pygame.image.load("images/zombies/norm_zombie_full_health.png").convert_alpha()
        self.half_health_image = pygame.image.load("images/zombies/norm_zombie_half_health.png").convert_alpha()
        self.image = self.full_health_image
        self.rect = self.image.get_rect()
        self.target = target
        self.speed = random.uniform(1, 3) # # Random speed between 1 and 3
    
    def update(self):
        # Calculate direction towards the player
        dx = self.target.rect.x - self.rect.x
        dy = self.target.rect.y - self.rect.y
        distance = math.sqrt(dx**2 + dy**2)

        # Move towards the player
        if distance > 0:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed

# Generates zombie randomly around the border of the screen
def generate_zombie(type):
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        if type == "shield":
            zombie = shieldZombie(player)
        else:
            zombie = Zombie(player)
        zombie.rect.x = random.randrange(screen_w - zombie.rect.width)
        zombie.rect.y = 85
    elif side == "bottom":
        if type == "shield":
            zombie = shieldZombie(player)
        else:
            zombie = Zombie(player)
        zombie.rect.x = random.randrange(screen_w - zombie.rect.width)
        zombie.rect.y = screen_h - zombie.rect.height
    elif side == "left":
        if type == "shield":
            zombie = shieldZombie(player)
        else:
            zombie = Zombie(player)
        zombie.rect.x = 0
        zombie.rect.y = random.randint(85, screen_h - zombie.rect.height)
    elif side == "right":
        if type == "shield":
            zombie = shieldZombie(player)
        else:
            zombie = Zombie(player)
        zombie.rect.x = screen_w - zombie.rect.width
        zombie.rect.y = random.randint(85, screen_h - zombie.rect.height)

    zombies.add(zombie)
    all_sprites.add(zombie)

# ----------------------------------- Background Stories -----------------------------------
            
def background_story():
    global picked_character
    john = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png").convert_alpha(), (screen_w, screen_h))
    tony = pygame.transform.scale(pygame.image.load("images/back_stories/Tony_backstory.png").convert_alpha(), (screen_w, screen_h))
    swift = pygame.transform.scale(pygame.image.load("images/back_stories/Swift_backstory.png").convert_alpha(), (screen_w, screen_h))
    quinn = pygame.transform.scale(pygame.image.load("images/back_stories/Quinn_backstory.png").convert_alpha(), (screen_w, screen_h))
    theresa = pygame.transform.scale(pygame.image.load("images/back_stories/Theresa_backstory.png").convert_alpha(), (screen_w, screen_h))
    jekyll = pygame.transform.scale(pygame.image.load("images/back_stories/John_backstory.png").convert_alpha(), (screen_w, screen_h))
    continue_button = pygame.transform.scale(pygame.image.load("images/CONTINUE_button.png").convert_alpha(), (275, 40))
    high_continue_button = pygame.transform.scale(pygame.image.load("images/highlighted_buttons/highlighted_CONTINUE_button.png").convert_alpha(), (275, 40))
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
    if screen_w - 350 <= mouse[0] <= screen_w - 75 and screen_h - 100 <= mouse[1] <= screen_h - 60:
        screen.blit(high_continue_button, (screen_w - 350, screen_h - 100))   
    else:
        screen.blit(continue_button, (screen_w - 350, screen_h - 100))

# ----------------------------------- Start Menu -----------------------------------

def menu_music():
    mixer.music.load('background_music/mainpage.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

menu_music()

def startMenu():
    global hovering_quit_b, hovering_start_b, hovering_tutorial_b
    # Images and Text
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png').convert_alpha(), (screen_w, screen_h))
    title_img = pygame.image.load('images/UNDEAD UPRISING.png').convert_alpha()
    text = font.render('Pick your character', True, (255, 255, 255))
    border = pygame.transform.scale(pygame.image.load('images/border.png').convert_alpha(), (700, 200))
    tutorial_b = pygame.transform.scale(pygame.image.load('images/TUTORIAL_button.png').convert_alpha(), (115, 115))
    start_b = pygame.transform.scale(pygame.image.load('images/START_button.png').convert_alpha(), (150, 60))
    quit_b = pygame.transform.scale(pygame.image.load('images/QUIT_button.png').convert_alpha(), (150, 60))
    high_tutorial_b = pygame.transform.scale(pygame.image.load('images/highlighted_buttons/highlighted_TUTORIAL_button.png').convert_alpha(), (115, 115))
    high_start_b = pygame.transform.scale(pygame.image.load('images/highlighted_buttons/highlighted_START_button.png').convert_alpha(), (150, 60))
    high_quit_b = pygame.transform.scale(pygame.image.load('images/highlighted_buttons/highlighted_QUIT_button.png').convert_alpha(), (150, 60))

    # Display images, text and buttons
    screen.blit(bg, (0, 0)) # background
    screen.blit(title_img, ((screen_w - 800) / 2, 125)) # title
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, 250)) # instruction
    screen.blit(border, (screen_w / 2 - 350, screen_h / 2 - 50)) # border
    if hovering_start_b:
        screen.blit(high_start_b, (screen_w / 2 - 200, screen_h - 140))
    else:
        screen.blit(start_b, (screen_w / 2 - 200, screen_h - 140))
    if hovering_quit_b:
        screen.blit(high_quit_b, (screen_w / 2 + 55, screen_h - 140))
    else:
        screen.blit(quit_b, (screen_w / 2 + 55, screen_h - 140))
    if hovering_tutorial_b:
        screen.blit(high_tutorial_b, (25, screen_h - 25 - 115))
    else:
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
    global game_state, player, picked_character, hovering_quit_b, hovering_start_b, hovering_tutorial_b

    if 30 <= mouse[0] <= 105 and screen_h - 105 <= mouse[1] <= screen_h - 30:
        hovering_tutorial_b = True
    else:
        hovering_tutorial_b = False
    
    if screen_w / 2 + 50 <= mouse[0] <= screen_w / 2  + 200 and screen_h - 140 <= mouse[1] < screen_h - 80:
        hovering_quit_b = True
    else:
        hovering_quit_b = False

    if screen_w / 2 - 200 <= mouse[0] <= screen_w / 2 - 50 and screen_h - 140 <= mouse[1] <= screen_h - 80:
        hovering_start_b = True
    else:
        hovering_start_b = False

    # Detects if a button was pressed
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Sets player to character clicked
        if screen_w * 0.28 <= mouse[0] <= screen_w * 0.28 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            all_sprites.remove(player)
            player = John()
            picked_character = "John"
            if John.clicked:
                John.clicked = not John.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = True, False, False, False, False, False
            print('John is picked')
        elif screen_w * (0.28 + 0.077) <= mouse[0] <= screen_w * (0.28 + 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            all_sprites.remove(player)
            player = Tony()
            picked_character =  "Tony"
            if Tony.clicked:
                Tony.clicked = not Tony.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, True, False, False, False, False
            print('Tony is picked')
        elif screen_w * (0.28 + 2 * 0.077) <= mouse[0] <= screen_w * (0.28 + 2 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            all_sprites.remove(player)
            player = Swift()
            picked_character = "Swift"
            if Swift.clicked:
                Swift.clicked = not Swift.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, True, False, False, False
            print('Swift is picked')
        elif shop_items["quinn"] == True and screen_w * (0.28 + 3 * 0.077) <= mouse[0] <= screen_w * (0.28 + 3 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            all_sprites.remove(player)
            player = Quinn()
            picked_character = "Quinn"
            if Quinn.clicked:
                Quinn.clicked = not Quinn.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, True, False, False
            print('Quinn is picked')
        # Special characters
        elif shop_items["theresa"] == True and screen_w * (0.28 + 4 * 0.077) <= mouse[0] <= screen_w * (0.28 + 4 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            all_sprites.remove(player)
            player = Theresa()
            picked_character = "Theresa"
            if Theresa.clicked:
                Theresa.clicked = not Theresa.clicked
            else:
                John.clicked, Tony.clicked, Swift.clicked, Quinn.clicked, Theresa.clicked, Jekyll.clicked = False, False, False, False, True, False
            print('Theresa is picked')
        elif shop_items["jekyll"] == True and screen_w * (0.28 + 5 * 0.077) <= mouse[0] <= screen_w * (0.28 + 5 * 0.077) + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            all_sprites.remove(player)
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

# ----------------------------------- Tutorial -----------------------------------

def tutorial(mouse):
    global game_state
    tut = pygame.transform.scale(pygame.image.load("images/backgrounds/Tutorial Screen.png").convert_alpha(), (screen_w, screen_h))
    back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png").convert_alpha(), (130, 40))
    high_back_button = pygame.transform.scale(pygame.image.load("images/highlighted_buttons/highlighted_BACK_button.png").convert_alpha(), (130, 40))
    screen.blit(tut, (0, 0))
    screen.blit(back_button, (screen_w - 250, screen_h - 100))
    if screen_w - 250 <= mouse[0] <= screen_w - 120 and screen_h - 100 <= mouse[1] <= screen_h - 60:
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_state = "start_menu"
        else:
            screen.blit(high_back_button, (screen_w - 250, screen_h - 100))

# ----------------------------------- Shop -----------------------------------

points = 16000

shop_items = {
    "quinn" : False,
    "theresa" : False, 
    "jekyll" : False,
    "med_kit" : False,
    "speed_potion" : False
}

costs = {
    "quinn" : 1000, 
    "theresa" : 1000,
    "jekyll" : 1000,
    "med_kit" : 200,
    "speed_potion" : 200
}

selected = ""

def shop(mouse):
    global selected, shop_display, points, zombies_allowed, font

    # Images, text, etc.
    text_font = pygame.font.SysFont('comic sans', 15, bold=True) # sets the font family and font size
    title1 = font.render('CHARACTERS', True, (0, 0, 0))
    title2 = font.render('POWER UPS', True, (0, 0, 0))
    darken = pygame.transform.scale(pygame.image.load("images/darken.png").convert_alpha(), (screen_w, screen_h))
    shop_title = pygame.transform.scale(pygame.image.load("images/SHOP_title.png").convert_alpha(), (685/3.5, 200/3.5))
    shop_bg = pygame.transform.scale(pygame.image.load("images/shop_bg.png").convert_alpha(), (screen_w * 0.8, screen_h * 0.7))
    back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png").convert_alpha(), (510/4.5, 155/4.5))
    buy_button = pygame.transform.scale(pygame.image.load("images/BUY_button.png").convert_alpha(), (818/8.7, 300/8.7))

    # Character images and definitions
    quinn = pygame.transform.scale(pygame.image.load("images/characters/circle_quinn.png"), (80, 80))
    normal_quinn = pygame.transform.scale(pygame.image.load("images/characters/normal_quinn.png"), (80, 80))
    quinn_title = text_font.render("QUINN", True, (0, 0, 0))
    quinn_cost = text_font.render("Cost: 1000 points", True, (0, 0, 0))
    quinn_feature = text_font.render("Feature: Higher initial health with no movement penalty", True, (0, 0, 0))
    theresa = pygame.transform.scale(pygame.image.load("images/characters/circle_theresa.png").convert_alpha(), (80, 80))
    normal_theresa = pygame.transform.scale(pygame.image.load("images/characters/normal_theresa.png").convert_alpha(), (80, 80))
    theresa_title = text_font.render("THERESA", True, (0, 0, 0))
    theresa_cost = text_font.render("Cost: 1000 points", True, (0, 0, 0))
    theresa_feature = text_font.render("Feature: Higher initial health with no movement penalty", True, (0, 0, 0))
    jekyll = pygame.transform.scale(pygame.image.load("images/characters/circle_jekyll.png").convert_alpha(), (80, 80))
    normal_jekyll = pygame.transform.scale(pygame.image.load("images/characters/normal_jekyll.png").convert_alpha(), (80, 80))
    jekyll_title = text_font.render("JEKYLL", True, (0, 0, 0))
    jekyll_cost = text_font.render("Cost: 1000 points", True, (0, 0, 0))
    jekyll_feature = text_font.render("Feature: Higher initial health with no movement penalty", True, (0, 0, 0))

    # Power-up images and definitions
    normal_med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/normal_med_kit.png").convert_alpha(), (80, 80))
    med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/circled_med_kit.png").convert_alpha(), (80, 80))
    med_kit_title = text_font.render("MEDICINE KIT", True, (0, 0, 0))
    med_kit_cost = text_font.render("Cost: 200 points", True, (0, 0, 0))
    med_kit_feature = text_font.render("Restores 25HP instantly when activated", True, (0, 0, 0))
    normal_speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/normal_speed_potion.png").convert_alpha(), (80, 80))
    speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/circled_speed_potion.png").convert_alpha(), (80, 80))
    speed_potion_title = text_font.render("SPEED POTION", True, (0, 0, 0))
    speed_potion_cost = text_font.render("Cost: 200 points", True, (0, 0, 0))
    speed_potion_feature = text_font.render("Boosts speed for 10 seconds when activated", True, (0, 0, 0))

    # Sign
    text = font.render("NOT ENOUGH POINTS", True, (0, 0, 0))

    # Display images and text
    screen.blit(darken, (0, 0))
    screen.blit(shop_title, ((screen_w - 685/3.5) / 2, 50))
    screen.blit(shop_bg, (screen_w * 0.1, 150))
    screen.blit(title1, (300, 185))
    screen.blit(title2, (800, 185))
    screen.blit(normal_quinn, (175, 250))
    screen.blit(normal_theresa, (175, 350))
    screen.blit(normal_jekyll, (175, 450))
    screen.blit(normal_med_kit, (screen_w / 2 + 50, 250))
    screen.blit(normal_speed_potion, (screen_w / 2 + 50, 350))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if shop_items["quinn"] == False and 175 <= mouse[0] <= 250 and 250 <= mouse[1] <= 325:
            screen.blit(quinn, (175, 250))
            selected = "quinn"
        if shop_items["theresa"] == False and 175 <= mouse[0] <= 250 and 350 <= mouse[1] <= 425:
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
        elif 500 <= mouse[0] <= 500 + 818/8.7 and screen_h - 150 <= mouse[1] <= screen_h - 150 + 300/8.7:
            if points >= costs[selected]:
                shop_items[selected] = not shop_items[selected]
                points -= costs[selected]
                selected = "buy"
                shop_display = not shop_display
                zombies_allowed = not zombies_allowed
            else:
                screen.blit(text, (screen_w / 2 - text.get_width() / 2, screen_h / 2))
        elif screen_w - 600 <= mouse[0] <= screen_w - 600 + 510/4.5 and screen_h - 150 <= mouse[1] <= screen_h - 150 + 155/4.5:
            shop_display = not shop_display
            zombies_allowed = not zombies_allowed

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

    screen.blit(quinn_title, (275, 265))
    screen.blit(quinn_cost, (275, 285))
    screen.blit(quinn_feature, (275, 305))
    screen.blit(theresa_title, (275, 365))
    screen.blit(theresa_cost, (275, 385))
    screen.blit(theresa_feature, (275, 405))
    screen.blit(jekyll_title, (275, 465))
    screen.blit(jekyll_cost, (275, 485))
    screen.blit(jekyll_feature, (275, 505))

    screen.blit(med_kit_title, (screen_w / 2 + 150, 265))
    screen.blit(med_kit_cost, (screen_w / 2 + 150, 285))
    screen.blit(med_kit_feature, (screen_w / 2 + 150, 305))

    # screen.blit(med_kit_def, (screen_w / 2 + 150, 255))

    screen.blit(speed_potion_title, (screen_w / 2 + 150, 365))
    screen.blit(speed_potion_cost, (screen_w / 2 + 150, 385))
    screen.blit(speed_potion_feature, (screen_w / 2 + 150, 405))
    screen.blit(buy_button, (500, screen_h - 150))
    screen.blit(back_button, (screen_w - 600, screen_h - 150))

# ----------------------------------- Game Play -----------------------------------

# Top menu bar (displays player health, points, and power-ups)
def bar(health, orig_health):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screen_w, 80))
    draw_health_bar(health, orig_health)
    power_ups()
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, 30))

# Displays health bar
def draw_health_bar(health, orig_health):
    border = pygame.transform.scale(pygame.image.load('images/bar_border.png').convert_alpha(), (300, 30))
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
    grey_med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/grey_med_kit.png").convert_alpha(), (50, 50))
    grey_speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/grey_speed_potion.png").convert_alpha(), (56 * (50/35), 35 * (50/35)))
    med_kit = pygame.transform.scale(pygame.image.load("images/power-ups/coloured_med_kit.png").convert_alpha(), (50, 50))
    speed_potion = pygame.transform.scale(pygame.image.load("images/power-ups/coloured_speed_potion.png").convert_alpha(), (56 * (50/35), 35 * (50/35)))
    
    items = font.render('Items', True, (255, 255, 255))
    screen.blit(items, (screen_w - 200 - items.get_width(), 30))

    if shop_items['med_kit'] == True:
        screen.blit(med_kit, (screen_w - 170, 15))
    else:
        screen.blit(grey_med_kit, (screen_w - 170, 15))
    
    if shop_items['speed_potion'] == True:
        screen.blit(speed_potion, (screen_w - 100, 15))
    else:
        screen.blit(grey_speed_potion, (screen_w - 100, 15))

# Sets character movement speed
def setspeed():
    global speed, diagspeed, extraspeed
    if picked_character == "John" or picked_character == "Quinn" or picked_character == "Theresa" or picked_character == "Jekyll":
        speed = -5
    if picked_character == "Tony":
        speed = -4
    if picked_character == "Swift":
        speed = -6
    if extraspeed == 1:
        speed -= 3
    
    diagspeed = -(math.sqrt((speed/2)**2 + (speed/2)**2))

# Detects events during game play state
def detect_events():
    global charX, charY, charX_change, charY_change, mouse, game_state, player, speed, shop_display, shop_items, healthdiff, extraspeed, extraspeed_duration, extraspeed_timer
    
    # Detects key pressed
    pressed = pygame.key.get_pressed()

    # Medicine kit Power-up
    if pressed[pygame.K_q]:
        if shop_items['med_kit'] == True:
            healthdiff = player.orig_health - player.health
            if healthdiff >= 25:
                player.health += 25
            else:
                player.health += healthdiff
            
        shop_items['med_kit'] = False

    # Speed potion Power-up
    if pressed[pygame.K_e]:
        if shop_items['speed_potion']:
            extraspeed = 1
            extraspeed_timer = extraspeed_duration
            shop_items['speed_potion'] = False

    # Update extraspeed duration
    if extraspeed_timer > 0:
        extraspeed_timer -= 1
    else:
        extraspeed = 0

    # Character movement detection
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

    # Detects shop button clicked
    if pressed[pygame.K_b]:
            shop_display = not shop_display
    
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
    if player.rect.x <= 5:
        player.rect.x = 5
    if player.rect.x >= screen_w - 38:
        player.rect.x = screen_w - 38
    if player.rect.y <= 85:
        player.rect.y = 85
    if player.rect.y >= screen_h - 60:
        player.rect.y = screen_h - 60

normalCount = 0

# Game Play Function
def play():
    global player, charX, charY, charX_change, charY_change, game_state, clock, points, last_zombie_time, screen, zombie_generation_rate, player_health_decrease_timer, zombies_allowed, acc, in_well, well_death, normalCount
    border()

    if picked_character == "John" or picked_character == "Tony":
        if 0.8 * screen_w <= player.rect.x <= 0.9 * screen_w and 0.1 * screen_h + 83 <= player.rect.y <= 0.16 * screen_h + 83:
            if in_well < 0:
                in_well = time.time()
            if time.time() - in_well >= 1:
                well_death = True
                player.health = 0
                in_well = -1
        else:
            in_well = -1

    # Character movement changes
    player.rect.x += charX_change
    player.rect.y += charY_change

    if zombies_allowed:
        # Generate zombies every 5 seconds
        current_time = time.time()
        time_elapsed = current_time - last_zombie_time
        if time_elapsed >= 1 / zombie_generation_rate:
            # Generate a zombie
            if normalCount == 8:
                generate_zombie("shield")
                normalCount = 0
            else:
                generate_zombie("normal")
            normalCount += 1

            # Update last zombie generation time
            last_zombie_time = current_time

            # Increase zombie generation rate over time
            if zombie_generation_rate < 0.5:
                zombie_generation_rate += 0.05
            elif zombie_generation_rate < 1:
                zombie_generation_rate += 0.03
            else:
                zombie_generation_rate += 0.015
            acc += 0.0001

        hits = pygame.sprite.spritecollide(player, zombies, False)
        for zombie in hits:
            current_time = time.time()
            if current_time - player_health_decrease_timer >= 0.33333333:
                player.health -= 1
                player_health_decrease_timer = current_time

        all_sprites.update()
    all_sprites.draw(screen)

    if picked_character == "Theresa":
        player.special()

    # Game end
    if player.health == 0:
        game_state = 'game_over'

def game_over():
    global well_death

    # Images
    game_over_screen = pygame.transform.scale(pygame.image.load("images/game_over_screen.png").convert_alpha(), (screen_w, screen_h))
    well_game_over_screen = pygame.transform.scale(pygame.image.load("images/well_game_over_screen.png").convert_alpha(), (screen_w, screen_h))    
    try_again = pygame.transform.scale(pygame.image.load("images/TRY_AGAIN_button.png").convert_alpha(), (325, 50))
    quit = pygame.transform.scale(pygame.image.load("images/QUIT_button.png").convert_alpha(), (225, 90))

    # Display images
    if well_death:
        screen.blit(well_game_over_screen, (0, 0))
    else:
        screen.blit(game_over_screen, (0, 0))
    
    screen.blit(try_again, (200, screen_h - 150))
    screen.blit(quit, (screen_w - 500, screen_h - 175))

# ----------------------------------- Bullet Shooting -----------------------------------

# Bullet object class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((7, 7))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=start_pos)
        self.start_pos = start_pos
        self.target_pos = target_pos
        self.speed = 10
    
    def update(self):
        global points
        
        # Move towards the target
        direction = pygame.math.Vector2(self.target_pos) - pygame.math.Vector2(self.start_pos)
        distance = direction.length()
        if distance > 0:
            direction.normalize_ip()
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

            # Check for collisions with zombies
            hits = pygame.sprite.spritecollide(self, zombies, False)
            for zombie in hits:
                zombie.health -= 1
                if zombie.identity == "normal":
                    if zombie.health == 1:
                        zombie.image = zombie.half_health_image
                    elif zombie.health <= 0:
                        zombie.kill()
                        points += random.randint(5, 8)
                else:
                    if zombie.health == 2 and not zombie.health <= 1:
                        zombie.image = zombie.two_health_image
                    elif zombie.health <= 1 and not zombie.health <= 0:
                        zombies.image = zombie.one_health_image
                    elif zombie.health <= 0:
                        zombie.kill()
                        points += random.randint(9, 12)
                self.kill()

            # Check if the bullet is outside the screen boundaries
            if not pygame.Rect(0, 0, screen_w, screen_h).colliderect(self.rect):
                self.kill()

# ----------------------------------- Reset Game After Round -----------------------------------

def resetGame():
    global all_sprites, zombies, trails, bullets, player, zombie_generation_rate, acc, points
    player.__init__()
    all_sprites = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    zombie_generation_rate = 0.45
    acc = 0
    points = 0

# ----------------------------------- Main Loop of Game -----------------------------------

# Setting the game state and default character choice
game_state = "start_menu" # start_menu, bg_story, game_play, or tutorial
picked_character = "John" # Chosen character - defaulted John
player = John() # Default character

running = True

while running:
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            shop_display = not shop_display
            zombies_allowed = not zombies_allowed
        if game_state == "start_menu":
            detect_start_menu()
        elif game_state == "bg_story":
            if event.type == pygame.MOUSEBUTTONDOWN and screen_w - 350 <= mouse[0] <= screen_w - 75 and screen_h - 100 <= mouse[1] <= screen_h - 60:
                game_state = "game_play"
                all_sprites.add(player)
        elif game_state == "game_play":
            setspeed()
            detect_events()
        elif game_state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= mouse[0] <= 525 and screen_h - 150 <= mouse[1] <= screen_h - 100:
                    game_state = "start_menu"
                    resetGame()
                if screen_w - 500 <= mouse[0] <= screen_w - 500 + 225 and screen_h - 175 <= mouse[1] <= screen_h - 85:
                    running = False
    if game_state == "start_menu":
        startMenu()
    elif game_state == "bg_story":
        background_story()
    elif game_state == "game_play":
        # Basic screen set-up
        screen.blit(player.bg, (0, 80))
        bar(player.health, player.orig_health)
        
        if zombies_allowed:
            play()

            # Bullet Detection
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                if timetoshoot <= abs(2.5 - acc):
                    start_pos = player.rect.center
                    target_pos = pygame.mouse.get_pos()
                    bullet = Bullet(start_pos, target_pos)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
                    timetoshoot = attackspeed
            timetoshoot -= 1.5
            trailfunction()
            detect_collision(zombies, trails)
        
        # Display shop screen
        if shop_display:
            shop(mouse)

        # Back Button
        if screen_w - 160 <= mouse[0] <= screen_w - 30 and screen_h - 70 <= mouse[1] <= screen_h - 30:
            screen.blit(high_back_button, (screen_w - 160, screen_h - 70))
        else:
            screen.blit(back_button, (screen_w - 160, screen_h - 70))
    elif game_state == "game_over":
        game_over()
    elif game_state == "tutorial":
        tutorial(mouse)
    pygame.display.update()
    clock.tick(fps)
