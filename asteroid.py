import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, SPRITE_LINE_WIDTH) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        angle = random.uniform(20, 50)
        velo1 = self.velocity.rotate(angle)
        velo2 = self.velocity.rotate(-1 * angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS 
        asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
        asteroid2= Asteroid(self.position[0], self.position[1], new_rad)
        asteroid1.velocity = velo1 * 1.2
        asteroid2.velocity = velo2 * 1.2

