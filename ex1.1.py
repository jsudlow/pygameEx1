# Import a library of functions called 'pygame'
import pygame
from math import pi
from pygame.locals import *

pygame.init()

class Application:
	def __init__(self,sizeX,sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
	def init(self):
		self.screen = pygame.display.set_mode([self.sizeX,self.sizeY])
		
	def setCaption(self,caption):
		pygame.display.set_caption(caption)
	def run(self):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		BLUE =  (  0,   0, 255)
		GREEN = (  0, 255,   0)
		RED =   (255,   0,   0)
		done = False
		clock = pygame.time.Clock()
		circle_position = [60,250] 
		
		while not done:
			clock.tick(10)
 	       
			for event in pygame.event.get(): # User did something
				if event.type == KEYDOWN:
            		if event.key == K_DOWN:
                		circle_position[1] += 10
            		if event.key == K_UP:
                		circle_position[1] -= 10
            		if event.key == K_RIGHT:
                		circle_position[0] += 10
            		if event.key == K_LEFT:
                		circle_position[0] -= 10

			self.screen.fill(WHITE)
   			pygame.draw.circle(self.screen, BLACK, [circle_position[0],circle_position[1]], 40)
   		  	pygame.display.flip()

app = Application(600,600)
app.setCaption("Example py1.1")
app.init()
app.run()