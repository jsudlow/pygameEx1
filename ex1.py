# Import a library of functions called 'pygame'
import pygame
from math import pi
from pygame.locals import *
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
circle_position = [60,250] 
pygame.key.set_repeat(100,10)
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                circle_position[1] += 10
            if event.key == K_UP:
                circle_position[1] -= 10
            if event.key == K_RIGHT:
                circle_position[0] += 10
            if event.key == K_LEFT:
                circle_position[0] -= 10
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # Draw a circle
    pygame.draw.circle(screen, BLACK, [circle_position[0],circle_position[1]], 40)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()