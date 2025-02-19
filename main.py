import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.016
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)  
        pygame.display.flip()
        clock.tick(60)
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
if __name__== "__main__":
    main()


























