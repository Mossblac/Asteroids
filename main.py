import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.016
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load("asteroidBG.jpg")
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(bg_image, (0, 0))
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisions(asteroid):
                    asteroid.split()

        pygame.display.flip()
        clock.tick(60)
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
if __name__== "__main__":
    main()


























