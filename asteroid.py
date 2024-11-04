import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(random.uniform(-100, 100), random.uniform(-100, 100))

    def update(self, dt):
        # Move asteroid by its velocity scaled by dt
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def split(self):
        # Remove the asteroid from the game
        self.kill()

        # If the asteroid is too small to split, don't create new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new asteroids with the new radius and adjusted velocities
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2


