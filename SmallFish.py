from Sprite import Sprite
import pygame
from random import randint

class SmallFish(Sprite):
    safe_x_one = 0
    safe_y_one = 60
    safe_x_two = 565
    safe_y_two = 405
    def __init__(self):
        self.image = pygame.image.load("assets/images/aero fish new.png")
        self.x = randint(SmallFish.safe_x_one,SmallFish.safe_x_two)
        self.y = randint(SmallFish.safe_y_one,SmallFish.safe_y_two)
        self.width = self.image.get_width()
        self.height = self.image.get_height()