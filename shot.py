from circleshape import *
from constants import *

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        pass

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        pass

    def update(self, dt):
        self.position += (self.velocity * dt)
        pass
     