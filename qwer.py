import pygame
import random
import math

# Initialize Pygame
pygame.init()
player_image = pygame.image.load("../spaceship.png")
# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids")

# Set up the colors
WHITE = (255, 255, 255)

# Set up the player
player_image = pygame.image.load("spaceship.png")
player_rect = player_image.get_rect()
player_rect.center = (400, 300)
player_angle = 0

# Set up the bullets
bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect()
bullet_rect.center = (player_rect.centerx, player_rect.centery)
bullet_angle = player_angle
bullet_speed = 5
bullet_state = "ready"

# Set up the asteroids
asteroid_images = [pygame.image.load("asteroid1.png"), pygame.image.load("asteroid2.png"), pygame.image.load("asteroid3.png")]
asteroids = []
num_asteroids = 6

for i in range(num_asteroids):
    asteroid_rect = asteroid_images[random.randint(0, 2)].get_rect()
    asteroid_rect.x = random.randint(0, 800)
    asteroid_rect.y = random.randint(0, 600)
    asteroid_angle = random.randint(0, 360)
    asteroid_rotation = random.randint(-3, 3)
    asteroids.append((asteroid_rect, asteroid_angle, asteroid_rotation))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_angle += 5
            if event.key == pygame.K_RIGHT:
                player_angle -= 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_rect.center = (player_rect.centerx, player_rect.centery)
                bullet_angle = player_angle
                bullet_state = "fire"

    # Rotate the player
    player_rotated = pygame.transform.rotate(player_image, player_angle)
    player_rect_rotated = player_rotated.get_rect(center=player_rect.center)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx = math.cos(math.radians(player_angle)) * 5
        dy = math.sin(math.radians(player_angle)) * -5
        player_rect.move_ip(dx, dy)

    # Move the bullet
    if bullet_state == "fire":
        dx = math.cos(math.radians(bullet_angle)) * bullet_speed
        dy = math.sin(math.radians(bullet_angle)) * -bullet_speed
        bullet_rect.move_ip(dx, dy)

        if bullet_rect.left < 0 or bullet_rect.right > 800 or bullet_rect.top < 0 or bullet_rect.bottom > 600:
            bullet_state = "ready"

    # Draw on the screen
    screen.fill((0, 0, 0))
    screen.blit(player_rotated, player_rect_rotated)
    if bullet_state == "fire":
        screen.blit(bullet_image, bullet_rect)

    for asteroid in asteroids:
        asteroid_rect, asteroid_angle, asteroid_rotation = asteroid
        asteroid_rotated = pygame.transform.rotate(asteroid_images[random.randint(0, 2)], asteroid_angle)
        asteroid_rect_rotated = asteroid_rotated.get_rect(center=asteroid_rect.center)
        screen.blit(asteroid_rotated, asteroid_rect_rotated)

        asteroid_rect.move_ip(asteroid_rotation, 2)

        if asteroid_rect.left > 800:
            asteroid_rect.x = 0 - asteroid_rect.width
        if asteroid_rect.right < 0:
            asteroid_rect.x = 800
        if asteroid_rect.top > 600:
            asteroid_rect.y = 0 - asteroid_rect.height
        if asteroid_rect.bottom < 0:
            asteroid_rect.y = 600

        if bullet_rect.colliderect(asteroid_rect):
            asteroid_rect.x = random.randint(0, 800)
            asteroid_rect.y = random.randint(0, 600)
            bullet_state = "ready"

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids")

# Set up the colors
WHITE = (255, 255, 255)

# Set up the player
player_image = pygame.image.load("spaceship.png")
player_rect = player_image.get_rect()
player_rect.center = (400, 300)
player_angle = 0

# Set up the bullets
bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect()
bullet_rect.center = (player_rect.centerx, player_rect.centery)
bullet_angle = player_angle
bullet_speed = 5
bullet_state = "ready"

# Set up the asteroids
asteroid_images = [pygame.image.load("asteroid1.png"), pygame.image.load("asteroid2.png"), pygame.image.load("asteroid3.png")]
asteroids = []
num_asteroids = 6

for i in range(num_asteroids):
    asteroid_rect = asteroid_images[random.randint(0, 2)].get_rect()
    asteroid_rect.x = random.randint(0, 800)
    asteroid_rect.y = random.randint(0, 600)
    asteroid_angle = random.randint(0, 360)
    asteroid_rotation = random.randint(-3, 3)
    asteroids.append((asteroid_rect, asteroid_angle, asteroid_rotation))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_angle += 5
            if event.key == pygame.K_RIGHT:
                player_angle -= 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_rect.center = (player_rect.centerx, player_rect.centery)
                bullet_angle = player_angle
                bullet_state = "fire"

    # Rotate the player
    player_rotated = pygame.transform.rotate(player_image, player_angle)
    player_rect_rotated = player_rotated.get_rect(center=player_rect.center)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx = math.cos(math.radians(player_angle)) * 5
        dy = math.sin(math.radians(player_angle)) * -5
        player_rect.move_ip(dx, dy)

    # Move the bullet
    if bullet_state == "fire":
        dx = math.cos(math.radians(bullet_angle)) * bullet_speed
        dy = math.sin(math.radians(bullet_angle)) * -bullet_speed
        bullet_rect.move_ip(dx, dy)

        if bullet_rect.left < 0 or bullet_rect.right > 800 or bullet_rect.top < 0 or bullet_rect.bottom > 600:
            bullet_state = "ready"

    # Draw on the screen
    screen.fill((0, 0, 0))
    screen.blit(player_rotated, player_rect_rotated)
    if bullet_state == "fire":
        screen.blit(bullet_image, bullet_rect)

    for asteroid in asteroids:
        asteroid_rect, asteroid_angle, asteroid_rotation = asteroid
        asteroid_rotated = pygame.transform.rotate(asteroid_images[random.randint(0, 2)], asteroid_angle)
        asteroid_rect_rotated = asteroid_rotated.get_rect(center=asteroid_rect.center)
        screen.blit(asteroid_rotated, asteroid_rect_rotated)

        asteroid_rect.move_ip(asteroid_rotation, 2)

        if asteroid_rect.left > 800:
            asteroid_rect.x = 0 - asteroid_rect.width
        if asteroid_rect.right < 0:
            asteroid_rect.x = 800
        if asteroid_rect.top > 600:
            asteroid_rect.y = 0 - asteroid_rect.height
        if asteroid_rect.bottom < 0:
            asteroid_rect.y = 600

        if bullet_rect.colliderect(asteroid_rect):
            asteroid_rect.x = random.randint(0, 800)
            asteroid_rect.y = random.randint(0, 600)
            bullet_state = "ready"

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
