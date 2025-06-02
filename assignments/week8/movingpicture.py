import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Image Objects")

# Load and scale image (adjust the path if needed)
image = pygame.image.load("ea85a121-e08d-4736-b142-d0ac451b9eeb.png")
image = pygame.transform.scale(image, (80, 80))

# ImageObject class
class ImageObject:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 80)
        self.y = random.randint(0, HEIGHT - 80)
        self.speed_x = random.choice([-1, 1]) * random.randint(1, 3)
        self.speed_y = random.choice([-1, 1]) * random.randint(1, 3)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x <= 0 or self.x >= WIDTH - 80:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= HEIGHT - 80:
            self.speed_y *= -1

    def draw(self, surface):
        surface.blit(image, (self.x, self.y))

# Create multiple animated images
objects = [ImageObject() for _ in range(5)]

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obj in objects:
        obj.move()
        obj.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
