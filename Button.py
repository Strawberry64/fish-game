from Sprite import Sprite
import pygame


class Button(Sprite):
    def __init__(self,pos, images):
        self.images = []
        for item in images:
            self.images.append(pygame.image.load(item))
        self.image = self.images[0]
        self.x = pos[0]
        self.y = pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def setImage(self,index):
        self.image = self.images[index]