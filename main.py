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
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([
            self.screen_width,
            self.screen_height,
        ])
        
        self.player = Player(
            200, 200,
            CircleEntity(40, BLACK),
        )

        self.enemey = Enemey(
            400,400,
            SquareEntity(40,GREEN),
            self
            )
        
        self.entities = []
        self.entities.append(self.enemey)
            
    def setCaption(self,caption):
        pygame.display.set_caption(caption)

    def update_entities(self, dt, time):
        for e in self.entities:
            e.update(dt, time)

        self.player.update(dt, time)

    def draw_screen(self):
        self.screen.fill(WHITE)

        for e in self.entities:
            e.draw(self.screen)
        self.player.draw(self.screen)
        

        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get(): 
            # User did something
            if event.type == pygame.QUIT: 
                # If user clicked close
                # Flag that we are done so we exit this loop
                self.done=True 
            self.player.handle_event(event)

    def run(self):
        time = 0
        clock = pygame.time.Clock()
              
        self.done = False
        while not self.done:
            dt = clock.tick(10)
            time += dt

            self.handle_events()     
            self.update_entities(dt, time)
            self.draw_screen()
              
class BaseEntity(object):
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y      
        self.sprite = sprite

    def move_down(self, amount):
        self.y += amount

    def move_up(self, amount):
        self.y -= amount

    def move_right(self, amount):
        self.x += amount

    def move_left(self, amount): 
        self.x -= amount

    def update(self, dt, time): pass

    def draw(self,screen):
        self.sprite.draw(screen,self.x, self.y)

class Player(BaseEntity):
    def __init__(self,sprite,x,y):
        super(Player,self).__init__(sprite,x,y)
        
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

class Enemey(BaseEntity):
    def __init__(self,sprite,x,y,app):
        super(Enemey,self).__init__(sprite,x,y)
        self.app = app
        
    def update(self,dt,time):
        if self.x > self.app.player.x:
            self.move_left(10)
        else:
            self.move_right(10)
        if self.y > self.app.player.y:
            self.move_up(10)
        else:
            self.move_down(10)
        
class Sprite(object):
    def __init__(self, color):
        self.color = color

class CircleEntity(Sprite):
    def __init__(self, radius, color):
        super(CircleEntity, self).__init__(color)
        self.radius = radius
    def draw(self, screen, x, y):  
        pygame.draw.circle(
            screen, 
            self.color, 
            [x,y], 
            self.radius,
        )

class SquareEntity(Sprite):
    def __init__(self,side_length,color):
        super(SquareEntity,self).__init__(color)
        self.side_length = side_length
    def draw(self,screen,x,y):
        pygame.draw.rect(
            screen, 
            self.color, 
            [x, y, self.side_length, self.side_length], 
            2,
        )
    

app = Application(600,600)
app.setCaption("Example main.py")
app.run()

