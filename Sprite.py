import pygame

class Sprite:
    def __init__(self, pos, image):
        self.image = pygame.image.load(image)
        self.x = pos[0]
        self.y = pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = pygame.image.load(image)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getEndX(self):
        return self.x + self.width        
    def getEndY(self):
        return self.y + self.height
    def getWidth(self):
        return self.width        
    def getHeight(self):
        return self.height
    def getPos(self):
        return [self.x,self.y]    
    def getFullPos(self):
        return [self.x,self.y,self.x + self.width,self.y + self.height]
    def getEndPos(self):
        return [self.x + self.width, self.y + self.height]
    
    def checkHover(self,mousePos):
        if mousePos[0] > self.getX() and mousePos[0] < self.getEndX():
            if mousePos[1] > self.getY() and mousePos[1] < self.getEndY():
                return True
        return False

    def checkHoverClick(self,mousePos,mouseClick):
        if(self.checkHover(mousePos)):
            if mouseClick[0] == True:
                return True
        return False