# Testing health bar and sprites

import pygame
import random
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

GREEN = (0, 255, 0)
YELLOW_GREEN = (173, 255, 47)
YELLOW_RED = (255, 150, 50)
RED = (255, 0, 0)

player_health = 100
damage_value = 10 #for the space bar test, can change this to any sort of damage thing

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Health Bar Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500

class Char(pygame.sprite.Sprite):
    char_img = pygame.image.load('images/characters/john.png')
    def __init__(self, color, height, width): 
        super().__init__() 
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height)) 
        self.rect = self.image.get_rect()
    
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed / 10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed / 10

all_sprites_list = pygame.sprite.Group() 
gravity = 4

object_ = Char(RED, 30, 30)
object_.rect.x = 200
object_.rect.y = 300

all_sprites_list.add(object_) 

zombie_img = pygame.image.load('images/test_char.png')
zomb = Rect(200, 50, 50, 50)

def draw_health_bar(health):
    if health > 70:
        color = GREEN
    elif health > 50:
        color = YELLOW_GREEN
    elif health > 20:
        color = YELLOW_RED
    else:
        color = RED
    pygame.draw.rect(screen, color, (0, 0, health * 1.5, 20))

def main():
    global player_health

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player_health -= damage_value
            #    if player_health <= 0:
            #        sys.exit() #health becomes zero or lower, pygame ends the run
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            object_.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            object_.moveRight(5)
        if keys[pygame.K_DOWN]:
            object_.moveForward(5)
        if keys[pygame.K_UP]:
            object_.moveBack(5)
        screen.fill((255, 255, 255))
        draw_health_bar(player_health)
        health_text = font.render(f"Health: {player_health}", True, (0, 0, 0))
        screen.blit(health_text, (0, 0))
        all_sprites_list.update() 
        all_sprites_list.draw(screen)
        collide = pygame.Rect.colliderect(object_.rect, zomb)
        if collide:
            print('collided')
        pygame.draw.rect(screen, (0, 0, 255), zomb)
        pygame.display.flip()
        clock.tick(FPS) #screen stuff

if __name__ == "__main__":
    main()

