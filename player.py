import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initialize player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Add the player and asteroid field to the update group
    updatable.add(player, asteroid_field)

    # Game loop
    clock = pygame.time.Clock()
    dt = 0
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black color
        screen.fill("black")

        # Update game objects
        updatable.update(dt)

        # Collision detection between asteroids and bullets
        for asteroid in asteroids:
            for shot in shots:
                if pygame.sprite.collide_circle(asteroid, shot):
                    asteroid.kill()
                    shot.kill()

        # Draw game objects
        drawable.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and update delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
