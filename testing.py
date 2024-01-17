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
        self.image = pygame.image.load("images/test_char.png").convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))

# Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.full_health_image = pygame.image.load("images/zombies/norm_zombie_full_health.png").convert_alpha()
        self.half_health_image = pygame.image.load("images/zombies/norm_zombie_half_health.png").convert_alpha()
        self.image = self.full_health_image
        self.rect = self.image.get_rect()
        self.target = target
        self.health = 2

    def update(self):
        # Calculate direction towards the player
        dx = self.target.rect.x - self.rect.x
        dy = self.target.rect.y - self.rect.y
        distance = math.sqrt(dx**2 + dy**2)

        # Move towards the player
        speed = 2
        if distance > 0:
            self.rect.x += (dx / distance) * speed
            self.rect.y += (dy / distance) * speed

        # Check for collisions with the player
        if pygame.sprite.collide_rect(self, self.target):
            self.health -= 1

            if self.health == 1:
                self.image = self.half_health_image
            elif self.health <= 0:
                self.kill()

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=start_pos)
        self.start_pos = start_pos
        self.target_pos = target_pos
        self.speed = 12

    def update(self):
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
                if zombie.health == 1:
                    zombie.image = zombie.half_health_image
                elif zombie.health <= 0:
                    zombie.kill()
                self.kill()

            # Check if the bullet is outside the screen boundaries
            if not pygame.Rect(0, 0, screen_width, screen_height).colliderect(self.rect):
                self.kill()

# Sprite groups
all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
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

        # Process spacebar event
        if game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Spacebar pressed, create a bullet
            start_pos = player.rect.center
            target_pos = pygame.mouse.get_pos()
            bullet = Bullet(start_pos, target_pos)
            bullets.add(bullet)
            all_sprites.add(bullet)

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

        # Check for collisions between bullets and zombies
        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet, zombies, False)
            for zombie in hits:
                zombie.health -= 1
                if zombie.health == 1:
                    zombie.image = zombie.half_health_image
                elif zombie.health <= 0:
                    zombie.kill()
                bullet.kill()

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
