import pygame
import random


# Initialize Pygame
pygame.init()


# Set up screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Auto-generating Zombies")


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)


# Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, screen_width - 50), random.randint(50, screen_height - 50))
        self.speed = random.randint(1, 3)


    def update(self):
        # Move the zombie towards the player (for illustration purposes)
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed


# Create player sprite
player = Player()


# Create groups for sprites
all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
all_sprites.add(player)


# Timer event for generating zombies
ADDZOMBIE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDZOMBIE, 5000)  # Generates a new zombie every 5 seconds


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDZOMBIE:
            new_zombie = Zombie()
            zombies.add(new_zombie)
            all_sprites.add(new_zombie)


    # Update
    all_sprites.update()


    # Draw
    all_sprites.draw(screen)


    pygame.display.flip()


pygame.quit()


