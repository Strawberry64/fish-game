from Sprite import Sprite
import pygame
from random import randint

"""
HOW TO CREATE NEW FISH!!!

Step 1: copy one of the following classes and rename it.
Step 2: replace the image that it will load. you should leave the assets/image./ part alone
Step 3: by default the fish will get a random location at creation. if you want to change its movement,
make a new function and when we are ready, we can call it to update the location. collision is designed to
be dynamic with the location.
"""

class BigFish(Sprite):
    classImage = pygame.image.load("assets/images/aero fish big.png")

    safe_x_one = 0 #leave alone
    safe_x_two = Sprite.safeAreaXCalc(classImage.get_width()) #will be calculated

    safe_y_one = 60 #leave along
    safe_y_two = Sprite.safeAreaYCalc(classImage.get_height()) #will be calculated

    
    def __init__(self):
        self.image = BigFish.classImage

        self.x = randint(BigFish.safe_x_one,BigFish.safe_x_two)
        self.y = randint(BigFish.safe_y_one,BigFish.safe_y_two)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

class SmallFish(Sprite):
    classImage = pygame.image.load("assets/images/aero fish new.png")

    safe_x_one = 0
    safe_x_two = Sprite.safeAreaXCalc(classImage.get_width())

    safe_y_one = 60
    safe_y_two = Sprite.safeAreaYCalc(classImage.get_height())
    def __init__(self):
        self.image = SmallFish.classImage
        self.x = randint(SmallFish.safe_x_one,SmallFish.safe_x_two)
        self.y = randint(SmallFish.safe_y_one,SmallFish.safe_y_two)
        self.width = self.image.get_width()
        self.height = self.image.get_height()