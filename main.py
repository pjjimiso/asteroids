import pygame
import sys
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    inits = pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set groups as containers for the Player and Asteroids
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    # Create Player in the center of the window
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Create a field of randomly generated asteroids
    asteroidfield = AsteroidField()

    while True: 
        # Check if the user has closed the window and exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with black  
        pygame.Surface.fill(screen, (0,0,0))

        # Update everything in the updatable group
        updatable.update(dt)

        for asteroid in asteroids: 
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit(0)

        # Draw everything in the drawable group
        for entity in drawable: 
            entity.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Get milliseconds since last game update
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
