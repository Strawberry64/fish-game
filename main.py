import pygame
import random

pygame.init()


flags =  [pygame.DOUBLEBUF | pygame.NOFRAME | pygame.SCALED]
screen = pygame.display.set_mode((640,480), flags[0])
pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))
clock = pygame.time.Clock()

print(flags)


safe_x_one = 0
safe_y_one = 60
safe_x_two = 590
safe_y_two = 430

def random_location(x1,y1,x2,y2):
    x = random.randint(x1,x2)
    y = random.randint(y1,y2)
    z = [x,y]
    return z

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

class Bubble(Sprite):
    def __init__(self,pos):
        self.image = pygame.image.load("assets/images/aero_fish.png")
        self.x = pos[0]
        self.y = pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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

def check_collision(mousePos,target):
    if mousePos[0] > target[0] and mousePos[0] < target[2]:
        if mousePos[1] > target[1] and mousePos[1] < target[3]:
            return True
    return False

def check_collision_click(mousePos,mouseClick,target):
    if mousePos[0] > target[0] and mousePos[0] < target[2]:
        if mousePos[1] > target[1] and mousePos[1] < target[3]:
            if mouseClick[0] == True:
                return True
    return False

background = pygame.image.load("assets/images/city.png")
start = Button([220,275],["assets/images/newstart.png","assets/images/newstarthover.png"])
back = Button([220,275],["assets/images/back.png","assets/images/backhover.png"])
quitButton = Button([220,375],["assets/images/quit.png","assets/images/quithover.png"])
fullscreenSprite = Button([555,15],["assets/images/fullscreen.png","assets/images/fullscreenhover.png"])


scoreImage = Sprite([20,20], "assets/images/score.png")

gameOverSprite = Sprite([195,60], "assets/images/gameOver.png")

fishes = []


#class Fish:

DEFAULT_TIME = 600
init_tick = 0
time = 600
score = 0
startGame = False
game = False
lastClick = False

score = 0
gameover = False
play = True
while play:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    tick = pygame.time.get_ticks()
    

    mouse = [pygame.mouse.get_pos(),pygame.mouse.get_pressed()]
    if(not(lastClick == True and mouse[1][0])):
        lastClick = False
        


    if(not(game) and (not(gameover)) and not(lastClick)):
        #start button
        if(check_collision(mouse[0],start.getFullPos())):
            start.setImage(1)
            if(check_collision_click(mouse[0],mouse[1],start.getFullPos())):
                startGame = True
        else:
            start.setImage(0)
        
        #quit button
        if(check_collision(mouse[0],quitButton.getFullPos())):
            quitButton.setImage(1)
            if(check_collision_click(mouse[0],mouse[1],quitButton.getFullPos())):
                play = False
        else:
            quitButton.setImage(0)

        if(check_collision(mouse[0],fullscreenSprite.getFullPos())):
            fullscreenSprite.setImage(1)
            if(check_collision_click(mouse[0],mouse[1],fullscreenSprite.getFullPos())):
                pygame.display.toggle_fullscreen()
        else:
            fullscreenSprite.setImage(0)


    # Do logical updates here.
    # ... 
    screen.blit(background,[0,0])
    if(game == True):
        if tick - init_tick > time:
            init_tick = tick
            fishes.append(Bubble(random_location(safe_x_one,safe_y_one,safe_x_two,safe_y_two)))
        if(len(fishes) < 11):
            if(lastClick == False):
                for i in range(len(fishes) - 1 , -1, -1):
                    if(check_collision_click(mouse[0],mouse[1],fishes[i].getFullPos())):
                        fishes.pop(i)
                        time -= 1
                        score += 1
                        i = -1
            for fish in fishes:
                screen.blit(fish.getImage(),fish.getPos())
            screen.blit(scoreImage.getImage(), scoreImage.getPos())
        else:
            game = False
            gameover = True

    if(gameover):
        screen.blit(gameOverSprite.getImage(), gameOverSprite.getPos())
        screen.blit(back.getImage(), back.getPos())
        if(check_collision(mouse[0],back.getFullPos())):
            back.setImage(1)
            if(check_collision_click(mouse[0],mouse[1],back.getFullPos())):
                gameover = False
        else:
            back.setImage(0)
    
    #screen.fill("grey")  # Fill the display with a solid color
    

    
    if(startGame):
        fishes = []
        time = DEFAULT_TIME

        game = True
        startGame = False
    
    if(not(game) and (not(gameover))):
        screen.blit(start.getImage(), start.getPos())
        screen.blit(quitButton.getImage(), quitButton.getPos())
        screen.blit(fullscreenSprite.getImage(), fullscreenSprite.getPos())
    
    if(mouse[1][0] == 1):
        lastClick = True
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)