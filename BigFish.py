from Sprite import Sprite
import pygame
from random import randint

class BigFish(Sprite):
    safe_x_one = 0
    safe_y_one = 60
    safe_x_two = 540
    safe_y_two = 380
    def __init__(self):
        self.image = pygame.image.load("assets/images/aero fish big.png")
        self.x = randint(BigFish.safe_x_one,BigFish.safe_x_two)
        self.y = randint(BigFish.safe_y_one,BigFish.safe_y_two)
        self.width = self.image.get_width()
        self.height = self.image.get_height()