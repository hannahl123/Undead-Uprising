import pygame
import sys
import random

#INTI
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PARTICLE = (255, 51, 51) #COLOR OF PARTICLERS AND ALSO PLAYER TEST MODEL
RED = (255, 51, 51) # COLOR OF ENEMY TESTS

# Player class
class Player(pygame.sprite.Sprite): #random game I pulled, code necessary will be noted
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(PARTICLE) 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2) #size of it

        self.speed = 1 #speed of test player

    def update(self): #move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

#ENEMY EXISTER
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(0, WIDTH)

#HERE

#THIS IS THE PARTICLES
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 5))
        self.image.fill(PARTICLE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx = random.uniform(-2, 1)
        self.vy = random.uniform(-1, 2)
        self.duration = FPS // 3 #FPS

    def update(self):
        self.rect.x += self.vx * 2
        self.rect.y += self.vy * 2
        self.duration -= 1
        if self.duration <= 0:
            self.kill()

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Effect Example")
clock = pygame.time.Clock()

#grouping stuf, only thing relevant to the particles is the thing called particles and all_sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
particles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0

#gameshot
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #THIS IS THE PART OF THE CODE THAT MAKES IT SO WHEN THE SQUARE 
    all_sprites.update()

    #PLAYER COLLIDE TO ENEMIES, PARTICLES MADE
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        for _ in range(20):  # Create 20 particles for each enemy hit
            particle = Particle(hit.rect.centerx, hit.rect.centery)
            all_sprites.add(particle)
            particles.add(particle)
#SCREEN
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    #SCORE
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, PARTICLE)
    screen.blit(score_text, (10, 10))

    #display
    pygame.display.flip()

    #FPS
    clock.tick(FPS)
    FPS = (60)

#the end:(
pygame.quit()
sys.exit()


