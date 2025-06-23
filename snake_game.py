import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake and Food settings
snake_block = 20
snake_speed = 10
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 25)

# Score display
def show_score(score):
    value = font.render(f"Score: {score}", True, BLACK)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake_list = []
    length = 1

    food_x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block
    food_y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block

    while not game_over:

        while game_close:
            screen.fill(WHITE)
            msg = font.render("Game Over! Press Q-Quit or R-Restart", True, RED)
            screen.blit(msg, [WIDTH // 6, HEIGHT // 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_block, snake_block])

        show_score(length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block
            food_y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block
            length += 1

        clock.tick(snake_speed)

    pygame.quit()

game_loop()
