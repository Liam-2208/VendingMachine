import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Open World")

# Player properties
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 50
player_speed = 5

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
            player_pos[1] += player_speed

        # Drawing
        screen.fill(WHITE)
        
        # Draw the player
        pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
        
        # Draw some random trees (as green squares)
        for _ in range(5):
            tree_x = random.randint(0, WIDTH - 50)
            tree_y = random.randint(0, HEIGHT - 50)
            pygame.draw.rect(screen, GREEN, (tree_x, tree_y, 50, 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

game_loop()