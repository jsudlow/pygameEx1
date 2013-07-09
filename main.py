# Import a library of functions called 'pygame'
import pygame
from math import pi
from pygame.locals import *

pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Application:
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([self.screen_width,self.screen_height])
        self.player = Player(400,400,40,BLACK)
            
    def setCaption(self,caption):
        pygame.display.set_caption(caption)

    def draw_screen(self):
        self.screen.fill(WHITE)
        self.player.draw(self.screen)
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                self.done=True # Flag that we are done so we exit this loop
            self.player.handle_event(event)

    def run(self):
        self.done = False
        clock = pygame.time.Clock()
              
        while not self.done:
            clock.tick(10)
            self.handle_events()     
            self.draw_screen()
              

class BaseEntity(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        
    def move_down(self,ammount):
        self.y += ammount

    def move_up(self,ammount):
        self.y -= ammount

    def move_right(self,ammount):
        self.x += ammount

    def move_left(self,ammount): 
        self.x -= ammount
    def draw(self): raise NotImplementedError()


class CircleEntity(BaseEntity):
    def __init__(self,x,y,radius,color):
        super(CircleEntity,self).__init__(x,y,color)
        self.radius = radius
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, [self.x,self.y], self.radius)

class SquareEntity(BaseEntity):
    def __init__(self,x,y,side_length,color):
        super(SquareEntity,self).__init__(x,y,color)
        self.side_length = side_length
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, [75, 10, 50, 20], 2)

class Player(CircleEntity):
    def __init__(self,x,y,radius,color):
        super(Player,self).__init__(x,y,radius,color)
        
    def handle_event(self,event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.move_down(10)
            if event.key == K_UP:
                self.move_up(10)
            if event.key == K_RIGHT:
                self.move_right(10)
            if event.key == K_LEFT:
                self.move_left(10)

    

app = Application(600,600)
app.setCaption("Example main.py")
app.run()

