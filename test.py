import pygame
import pygame_gui
import random
import time
import math

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zombie Game")

# Colors
white = (255, 255, 255)

# Create a UI manager
manager = pygame_gui.UIManager((screen_width, screen_height))

# Create a start menu button
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((screen_width / 2 - 100, screen_height / 2 - 25), (200, 50)),
    text='Start Game',
    manager=manager
)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/characters/player_john.png").convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))

# Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.image = pygame.image.load("images/zombies/norm_zombie_full_health.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.target = target
        self.speed = random.uniform(1, 5)  # Random speed between 1 and 3

    def update(self):
        # Calculate direction towards the player
        dx = self.target.rect.x - self.rect.x
        dy = self.target.rect.y - self.rect.y
        distance = math.sqrt(dx**2 + dy**2)

        # Move towards the player with randomized speed
        if distance > 0:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed

# Sprite groups
all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Generate zombies at random locations around the border
def generate_zombie():
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        zombie = Zombie(player)
        zombie.rect.x = random.randrange(screen_width - zombie.rect.width)
        zombie.rect.y = 0
    elif side == "bottom":
        zombie = Zombie(player)
        zombie.rect.x = random.randrange(screen_width - zombie.rect.width)
        zombie.rect.y = screen_height - zombie.rect.height
    elif side == "left":
        zombie = Zombie(player)
        zombie.rect.x = 0
        zombie.rect.y = random.randrange(screen_height - zombie.rect.height)
    elif side == "right":
        zombie = Zombie(player)
        zombie.rect.x = screen_width - zombie.rect.width
        zombie.rect.y = random.randrange(screen_height - zombie.rect.height)

    zombies.add(zombie)
    all_sprites.add(zombie)

# Game loop
running = True
clock = pygame.time.Clock()
last_zombie_time = time.time()
game_active = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Process UI events
        manager.process_events(event)

        # Process button click event
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                game_active = True

    # Process other events if the game is active
    if game_active:
        # Player movement
        keys = pygame.key.get_pressed()
        speed = 5  # Adjust the speed as needed

        # Calculate the movement vector
        movement = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            movement.y -= 1
        if keys[pygame.K_s]:
            movement.y += 1
        if keys[pygame.K_a]:
            movement.x -= 1
        if keys[pygame.K_d]:
            movement.x += 1

        # Normalize the movement vector if it's not (0, 0)
        if movement.length() > 0:
            movement.normalize_ip()

        # Update player position
        player.rect.x += movement.x * speed
        player.rect.y += movement.y * speed


        # Generate zombies every 5 seconds
        current_time = time.time()
        if current_time - last_zombie_time >= 5:
            generate_zombie()
            last_zombie_time = current_time

        # Update sprites
        all_sprites.update()

        # Check for collisions between player and zombies
        if pygame.sprite.spritecollide(player, zombies, dokill=True):
            print("Game Over!")

    # Draw background
    screen.fill(white)

    # Draw UI
    if not game_active:
        manager.update(1 / 30)
        manager.draw_ui(screen)

    # Draw sprites if the game is active
    if game_active:
        all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
