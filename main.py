import pygame
import sys
import ctypes

pygame.init()

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
screen_w, screen_h = true_res[0], true_res[1]

# Game Details - Loading and Setting the Name and Logos of the Game
pygame.display.set_caption("Undead Uprising")
logo = pygame.image.load('images/test_char.png')
pygame.display.set_icon(logo)
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')

# Keeping track of the state of the game - start_menu, game_play, or tutorial
game_state = "start_menu"
character = "John"  # default character

# Images, sounds, and other files needed
bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png'), (screen_w, screen_h))
back_button = pygame.transform.scale(pygame.image.load("images/BACK_button.png"), (510/4, 155/4))
h_back_button = pygame.transform.scale(pygame.image.load("images/h_BACK_button.png"), (510/4, 155/4))

# Characters

class John():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/john.png')
    h_john = pygame.image.load('images/characters/h_john.png')
    clicked = False
    health = 100
    def __init__(self, x = 500, y = 300):
        self.x = x
        self.y = y
        self.clicked = False
        self.rect = self.image.get_rect(center = (x, y))
        self.img = John.char_img
        self.health = John.health
        self.speed = 'normal'
    def show():
        if John.clicked:
            screen.blit(John.h_john, (screen_w * 2 / 7, screen_h / 2 + 20))
        else:
            screen.blit(John.char_img, (screen_w * 2 / 7, screen_h / 2 + 20))

class Tony():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_earth.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/tony.png')
    h_tony = pygame.image.load('images/characters/h_tony.png')
    clicked = False
    def __init__(self, x = 500, y = 300):
        self.x = x
        self.y = y
        self.clicked = False
        self.img = Tony.char_img
        self.health = 100
        self.speed = 'normal'

    def show():
        if Tony.clicked:
            screen.blit(Tony.h_tony, (screen_w * 2.5 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Tony.char_img, (screen_w * 2.5 / 7, screen_h / 2 + 20))

class Swift():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_track.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/swift.png')
    h_swift = pygame.image.load('images/characters/h_swift.png')
    clicked = False

    def __init__(self, x = 500, y = 300):
        self.x = x
        self.y = y
        self.clicked = False
        self.img = Swift.char_img
        self.health = 100
        self.speed = 'normal'

    def show():
        if Swift.clicked:
            screen.blit(Swift.h_swift, (screen_w * 3 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Swift.char_img, (screen_w * 3 / 7, screen_h / 2 + 20))

class Quinn():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_magma.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/quinn.png')
    h_quinn = pygame.image.load('images/characters/h_quinn.png')
    clicked = False

    def __init__(self, x = 500, y = 300):
        self.x = x
        self.y = y
        self.clicked = False
        self.img = Quinn.char_img
        self.health = 100
        self.speed = 'normal'

    def show():
        if Quinn.clicked:
            screen.blit(Quinn.h_quinn, (screen_w * 3.5 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Quinn.char_img, (screen_w * 3.5 / 7, screen_h / 2 + 20))

class Theresa():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_hospital.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/theresa.png')
    h_theresa = pygame.image.load('images/characters/h_theresa.png')
    clicked = False

    def __init__(self, x = 500, y = 300):
        self.x = x
        self.y = y
        self.clicked = False
        self.img = Theresa.char_img
        self.health = 100
        self.speed = 'normal'

    def show():
        if Theresa.clicked:
            screen.blit(Theresa.h_theresa, (screen_w * 4 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Theresa.char_img, (screen_w * 4 / 7, screen_h / 2 + 20))

class Jekyll():
    bg = pygame.transform.scale(pygame.image.load('images/backgrounds/bg_hospital.png'), (screen_w, screen_h))
    char_img = pygame.image.load('images/characters/jekyll.png')
    h_jekyll = pygame.image.load('images/characters/h_jekyll.png')
    clicked = False

    def __init__(self, x = 500, y = 300):
        self.x = x
        self.y = y
        self.clicked = False
        self.img = Jekyll.char_img
        self.health = 100
        self.speed = 'normal'

    def show():
        if Jekyll.clicked:
            screen.blit(Jekyll.h_jekyll, (screen_w * 4.5 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Jekyll.char_img, (screen_w * 4.5 / 7, screen_h / 2 + 20))


def display_start():
    screen.blit(bg, (0, 0)) # displays the background
    font = pygame.font.SysFont('consolas', 25) # sets the font family and font size
    screen.blit(big_logo, ((screen_w - 800) / 2, 125)) # displays the big title
    text = font.render('Pick your character', True, (255, 255, 255)) # sets the instructions text
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, 250)) # displays the instructions text
    border_image = pygame.image.load('images/border.png')
    screen.blit(border_image, (screen_w / 2 - 350, screen_h / 2 - 50))
    show_all_char() # displays all 6 characters
    buttons() # displays the start button
    pygame.display.update() # updates the screen

# Displays the start button
def buttons():
    # tutorial_b = pygame.image.load('images/Tutorial_button.png')
    # tutorial_b = pygame.transform.scale(tutorial_b, (75, 75))
    start_b = pygame.image.load('images/START_button.png')
    start_b = pygame.transform.scale(start_b, (150, 60))
    quit_b = pygame.image.load('images/QUIT_button.png')
    quit_b = pygame.transform.scale(quit_b, (150, 60))
    screen.blit(start_b, (screen_w / 2 - 200, screen_h - 140))
    screen.blit(quit_b, (screen_w / 2 + 50, screen_h - 140))
    # screen.blit(tutorial_b, (30, screen_h - 105))

# Displays all characters on the start menu
def show_all_char():
    John.show()
    Tony.show()
    Swift.show()
    Quinn.show()
    Theresa.show()
    Jekyll.show()

def back(hover):
    if hover:
        screen.blit(h_back_button, (screen_w - 200, screen_h - 100))
    else:
        screen.blit(back_button, (screen_w - 200, screen_h - 100))

# Default character position - center of screen
charX = screen_w / 2 - 30
charY = screen_h / 2 - 30
charX_change = 0
charY_change = 0

def movement(event):
    global charX, charY, charX_change, charY_change, mouse
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
        # sets the variable to False, which breaks the while loop
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            charX_change = -3
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            charX_change = 3
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            charY_change = -3
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            charY_change = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            charX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
            charY_change = 0

# Function to play the game
def play(char):
    global charX, charY, charX_change, charY_change
    # border code
    if charX <= 0:
        charX = 0
    if charX >= screen_w - 50:
        charX = screen_w - 50
    if charY <= 0:
        charY = 0
    if charY >= screen_h - 60:
        charY = screen_h - 60
    if char == 'John':
        screen.blit(John.bg, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            movement(event)
        charX += charX_change
        charY += charY_change
        screen.blit(John.char_img, (charX, charY))
        draw_health_bar(John.health)
    elif char == 'Tony':
        screen.blit(Tony.bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            movement(event)
        charX += charX_change
        charY += charY_change
        screen.blit(Tony.char_img, (charX, charY))
    elif char == 'Swift':
        screen.blit(Swift.bg, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            movement(event)
        charX += charX_change
        charY += charY_change
        screen.blit(Swift.char_img, (charX, charY))
    elif char == 'Quinn':
        screen.blit(Quinn.bg, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            movement(event)
        charX += charX_change
        charY += charY_change
        screen.blit(Quinn.char_img, (charX, charY))
    elif char == 'Theresa':
        screen.blit(Theresa.bg, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            movement(event)
        charX += charX_change
        charY += charY_change
        screen.blit(Theresa.char_img, (charX, charY))
    elif char == 'Jekyll':
        screen.blit(Jekyll.bg, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            movement(event)
        charX += charX_change
        charY += charY_change
        screen.blit(Jekyll.char_img, (charX, charY))
    pygame.display.update()


def draw_health_bar(health):
    if health > 70:
        color = (0, 255, 0)
    elif health > 50:
        color = (173, 255, 47)
    elif health > 20:
        color = (255, 150, 50)
    else:
        color = (255, 0, 0)
    pygame.draw.rect(screen, color, (30, 30, health * 4, 30))

def intro():
    screen.blit(bg, (0, 0))

def detect_start_menu():
    global game_state, character
    # if the mouse is clicked in the start menu, check where the cursor is
    if game_state == 'start_menu' and event.type == pygame.MOUSEBUTTONDOWN:
        # checks which character the mouse cursor is on
        if screen_w * 2 / 7 <= mouse[0] <= screen_w * 2 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            # if John is clicked, state in the console and set the character to John
            character = "John"
            John.clicked = True
            Tony.clicked = False
            Quinn.clicked = False
            Swift.clicked = False
            Jekyll.clicked = False
            Theresa.clicked = False
            print('John is picked')
        elif screen_w * 2.5 / 7 <= mouse[0] <= screen_w * 2.5 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            # if Tony is clicked, state in the console and set the character to Tony
            character = "Tony"
            John.clicked = False
            Tony.clicked = True
            Quinn.clicked = False
            Swift.clicked = False
            Jekyll.clicked = False
            Theresa.clicked = False
            print('Tony is picked')
        elif screen_w * 3 / 7 <= mouse[0] <= screen_w * 3 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            # if Swift is clicked, state in the console and set the character to Swift
            character = "Swift"
            John.clicked = False
            Tony.clicked = False
            Quinn.clicked = False
            Swift.clicked = True
            Jekyll.clicked = False
            Theresa.clicked = False
            print('Swift is picked')
        elif screen_w * 3.5 / 7 <= mouse[0] <= screen_w * 3.5 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            # if Quinn is clicked, state in the console and set the character to Quinn
            character = "Quinn"
            John.clicked = False
            Tony.clicked = False
            Quinn.clicked = True
            Swift.clicked = False
            Jekyll.clicked = False
            Theresa.clicked = False
            print('Quinn is picked')
        elif screen_w * 4 / 7 <= mouse[0] <= screen_w * 4 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            # if Theresa is clicked, state in the console and set the character to Theresa
            character = "Theresa"
            John.clicked = False
            Tony.clicked = False
            Quinn.clicked = False
            Swift.clicked = False
            Jekyll.clicked = False
            Theresa.clicked = True
            print('Theresa is picked')
        elif screen_w * 4.5 / 7 <= mouse[0] <= screen_w * 4.5 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
            # if Jekyll is clicked, state in the console and set the character to Jekyll
            character = "Jekyll"
            John.clicked = False
            Tony.clicked = False
            Quinn.clicked = False
            Swift.clicked = False
            Jekyll.clicked = True
            Theresa.clicked = False
            print('Jekyll is picked')
        # checks if the start button is clicked
        elif screen_w / 2 - 200 <= mouse[0] <= screen_w / 2 - 50 and screen_h - 140 <= mouse[1] <= screen_h - 80:
            # if the start button was pressed, set the game state to game_play, which executes the next part of the game
            game_state = "game_play"
        # checks if the tutorial button is clicked
        if 30 <= mouse[0] <= 105 and screen_h - 105 <= mouse[1] <= screen_h - 30:
            game_state = "tutorial"

# Variable to keep the game on, when changed to False then exit
running = True

# Main Loop of Game
while running:
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        if game_state == 'start_menu':
            detect_start_menu()
    if game_state == 'start_menu':
        display_start()
    elif game_state == 'game_play':
        play(character)
    elif game_state == 'tutorial':
        intro()
