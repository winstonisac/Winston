import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)   
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
        
    def draw(self, screen): 
        if self.index >= 10: 
            self.index = 0
        screen.blit(self.image[self.index>=6], self.rect) 
        self.index += 1

