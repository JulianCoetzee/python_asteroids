import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity*dt)
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:   
            split_angle = random.uniform(20, 50)
            s1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            s2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            s1.velocity = self.velocity.rotate(split_angle) * 1.2
            s2.velocity = self.velocity.rotate(-1*split_angle) * 1.2
        self.kill()
