import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 30
ENEMY_WIDTH, ENEMY_HEIGHT = 40, 20
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        # Keep the player within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - PLAYER_WIDTH:
            self.rect.x = WIDTH - PLAYER_WIDTH

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)

    def update(self):
        self.rect.y -= 5  # Move the bullet up

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy(random.randint(0, WIDTH - ENEMY_WIDTH), random.randint(20, 100)) for _ in range(5)]
    bullets = []

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.rect.centerx, player.rect.top))

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5)
        if keys[pygame.K_RIGHT]:
            player.move(5)

        # Update and draw bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        # Check for bullet collisions with enemies
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    break

        # Draw everything
        player.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
