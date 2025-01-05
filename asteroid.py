from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        pass

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        pass

    def update(self, dt):
        self.position += (self.velocity * dt)
        pass

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            splitAngle = random.uniform(20,50)
            asteroid1Vector = self.velocity.rotate(splitAngle)
            asteroid2Vector = self.velocity.rotate(-splitAngle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid1.velocity = asteroid1Vector * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid2.velocity = asteroid2Vector * 1.2
        pass

