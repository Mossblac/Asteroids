import pygame
from circleshape import *
from constants import *
from asteroid import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y,):
       super().__init__(x, y, PLAYER_RADIUS)
       self.rotation = 0
       self.timer = 0 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        triangle_points = self.triangle()
        pygame.draw.polygon(screen, (128,0,128), triangle_points, 0)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOT_COOLDOWN
        shoot = Shot(self.position.x, self.position.y)
        shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

        


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        
            

