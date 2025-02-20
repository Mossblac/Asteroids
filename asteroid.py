import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
    
        


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_b = self.velocity.rotate(random_angle)
        vector_c = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = 1.2 * vector_b
        asteroid_c = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_c.velocity = 1.2 * vector_c









