import pygame
import random

pygame.init()


flags =  [pygame.DOUBLEBUF | pygame.NOFRAME | pygame.SCALED]
screen = pygame.display.set_mode((640,480), flags[0])
pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font("assets/fonts/segoeuigis.ttf", 36)

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
        if(check_hover(mousePos)):
            if mouseClick[0] == True:
                return True
        return False

class SmallFish(Sprite):
    safe_x_one = 0
    safe_y_one = 60
    safe_x_two = 565
    safe_y_two = 405
    def __init__(self):
        self.image = pygame.image.load("assets/images/aero fish new.png")
        self.x = random.randint(SmallFish.safe_x_one,SmallFish.safe_x_two)
        self.y = random.randint(SmallFish.safe_y_one,SmallFish.safe_y_two)
        self.width = self.image.get_width()
        self.height = self.image.get_height()


class BigFish(Sprite):
    safe_x_one = 0
    safe_y_one = 60
    safe_x_two = 540
    safe_y_two = 380
    def __init__(self):
        self.image = pygame.image.load("assets/images/aero fish big.png")
        self.x = random.randint(BigFish.safe_x_one,BigFish.safe_x_two)
        self.y = random.randint(BigFish.safe_y_one,BigFish.safe_y_two)
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

background = pygame.image.load("assets/images/city.png")
start = Button([220,275],["assets/images/newstart.png","assets/images/newstarthover.png"])
back = Button([220,275],["assets/images/back.png","assets/images/backhover.png"])
quitButton = Button([220,375],["assets/images/quit.png","assets/images/quithover.png"])
fullscreenSprite = Button([555,15],["assets/images/fullscreen.png","assets/images/fullscreenhover.png"])
competitiveSprite = Button([555,105],["assets/images/compOff.png","assets/images/compOn.png"])

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
comp = False
compTimeStart = 0
compTimeEnd = 0
lastClick = False

randomFishNumber = 0


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
        if(start.checkHover(mousePos)):
            start.setImage(1)
            if(start.checkHoverClick(mousePos,mouseClick)):
                startGame = True
        else:
            start.setImage(0)
        
        #quit button
        if(quitButton.checkHover(mousePos)):
            quitButton.setImage(1)
            if(quitButton.checkHoverClick(mousePos)):
                play = False
        else:
            quitButton.setImage(0)

        if(fullscreenSprite.check_hover(mousePos)):
            fullscreenSprite.setImage(1)
            if(fullscreenSprite.checkHoverClick(mousePos,mouseClick)):
                pygame.display.toggle_fullscreen()
        else:
            fullscreenSprite.setImage(0)
        #competitive mode button
        if(competitiveSprite.checkHoverClick):
            if(comp == False):
                competitiveSprite.setImage(1)
                comp = True
            else:
                competitiveSprite.setImage(0)
                comp = False

    # Do logical updates here.
    # ... 
    screen.blit(background,[0,0])
    if(game == True and comp == False):
        if tick - init_tick > time:
            randomFishNumber = random.randint(0,100)
            init_tick = tick
            fishes.append(SmallFish())
        if(len(fishes) < 11):
            if(lastClick == False):
                for i in range(len(fishes) - 1 , -1, -1):
                    if(check_collision_click(mouse[0],mouse[1],fishes[i].getFullPos())):
                        fishes.pop(i)
                        time -= 1
                        score += 1
                        break
            for fish in fishes:
                screen.blit(fish.getImage(),fish.getPos())
            screen.blit(scoreImage.getImage(), scoreImage.getPos())
            screen.blit(font.render(str(score),False, (0,43,162)), [240,18])
        else:
            game = False
            gameover = True
    if(game == True and comp == True):
        screen.blit(fishes[0].getImage(),fishes[0].getPos())
        if(check_collision_click(mouse[0],mouse[1],fishes[0].getFullPos())):
            fishes.pop(0)
        screen.blit(scoreImage.getImage(), scoreImage.getPos())
        screen.blit(font.render(str((tick - compTimeStart)/1000),False, (174,0,0)), [240,18])
        if(len(fishes) == 0):
            compTimeEnd = tick
            print("Final Time in ms: " + str((compTimeEnd - compTimeStart)))
            game = False
            gameover = True

    if(gameover):
        screen.blit(gameOverSprite.getImage(), gameOverSprite.getPos())
        screen.blit(back.getImage(), back.getPos())
        if(comp == False):
            screen.blit(font.render(("Score: " + str(score)),False, (0,43,162)), [20,18])
        else:
            screen.blit(font.render(("Time in Seconds: " + str((compTimeEnd - compTimeStart)/1000)),False, (174,0,0)), [20,18])
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
        if(comp):
            for i in range(50):
                fishes.append(SmallFish())
            compTimeStart = tick
    
    if(not(game) and (not(gameover))):
        screen.blit(start.getImage(), start.getPos())
        screen.blit(quitButton.getImage(), quitButton.getPos())
        screen.blit(fullscreenSprite.getImage(), fullscreenSprite.getPos())
        screen.blit(competitiveSprite.getImage(), competitiveSprite.getPos())
    
    if(mouse[1][0] == 1):
        lastClick = True
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(360)         # wait until next frame (at 60 FPS)