# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_KINDS, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE
from player import Player

def main():
    pygame.init()
    frame_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # spawn player
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while pygame.get_init():
        for event in pygame.event.get():
            # make the window CLOSE button work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        p1.draw(screen)
        # Setting FPS to 60
        dt = frame_clock.tick(60)/1000
        pygame.display.flip()


# This line ensures the main() function is only called when this file is run directly
if __name__ == "__main__":
    main()