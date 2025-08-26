import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): 
        pygame.draw.circle(
            screen, 
            (255,255,255), 
            self.position, 
            self.radius,
            2
        )

    def update(self, dt): 
        self.position += self.velocity * dt

    def split(self): 
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS: 
            return
        
        # Split into two smaller asteroids
        # Generate a random angle to be used for the new split asteroids
        random_angle = random.uniform(20,50)
        # The new asteroids will have a smaller radius than the parent asteroid
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Generate inverse velocities for the new asteroids
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = v1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = v2 * 1.2

