# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_KINDS, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from player import Player
from shot import Shot

def main():
    pygame.init()
    frame_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    field = AsteroidField()
    # spawn player
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print(updatable)
    print(drawable)
    print(asteroids)
    print(shots)
    while pygame.get_init():
        for event in pygame.event.get():
            # make the window CLOSE button work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        # Setting FPS to 60
        dt = frame_clock.tick(60)/1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_collision(p1):
                print("Game over!")
                return
            for shot in shots:
                if shot.is_collision(asteroid) :
                    shot.kill()
                    asteroid.split()        
        pygame.display.flip()


# This line ensures the main() function is only called when this file is run directly
if __name__ == "__main__":
    main()