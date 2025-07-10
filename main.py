import pygame 
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


    #Create Game Variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Groups
    updateable = pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    
    #Instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    done = False
    #Game Loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.CollisionCheck(player):
                print("Game Over!")
                done = True

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0
    pygame.quit()

if __name__ == "__main__":
    main()
