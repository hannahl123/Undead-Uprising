import pygame
import sys
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
            elif event.type == pygame.KEYDOWN:
                player_health -= damage_value
                if player_health <= 0:
                    sys.exit() #health becomes zero or lower, pygame ends the run

        screen.fill((255, 255, 255))
        draw_health_bar(player_health)

        health_text = font.render(f"Health: {player_health}", True, (0, 0, 0))
        screen.blit(health_text, (0, 0))

        pygame.display.flip()
        clock.tick(FPS) #screen stuff

if __name__ == "__main__":
    main()

