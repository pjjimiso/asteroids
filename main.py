import pygame
from constants import *
from player import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    inits = pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    # Create Player in the center of the window
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True: 
        # Check if the user has closed the window and exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black  
        pygame.Surface.fill(screen, (0,0,0))
        
        # Draw the player
        player.draw(screen)
        
        # Refresh the screen
        pygame.display.flip()

        # Get milliseconds since last game update
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
