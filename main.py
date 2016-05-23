import pygame
from pygame.locals import *

#set the size of the window
w_size = 1000
h_size = 750

screen = pygame.display.set_mode((w_size, h_size), DOUBLEBUF)

sun = (255, 255, 0)
white_color = (255, 255, 255)
blue_color = (0, 120, 255)

#set initial position of the ball
p_x = 700
p_y = 300

#set the number of pixels in a step
step = 30;

#set the dimensions of the image
image_width = 88
image_height = 118

radius = 20

running = True
while running:
	for event in pygame.event.get():
		increment_right = False
		increment_left = False
		increment_up = False
		increment_down = False

		if event.type == pygame.QUIT:
			running = False
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				increment_right = True
			if event.key == K_LEFT:
				increment_left = True
			if event.key == K_UP:
				increment_up = True
			if event.key == K_DOWN:
				increment_down = True
		#apply the keys inserted but keep the ball into the screen
		if increment_right and p_x + step >= 0 and p_x + step <= w_size:
			p_x = p_x + step
		if increment_left and p_x - step >= 0 and p_x - step <= w_size:
			p_x = p_x - step
		if increment_up and p_y - step >= 0 and p_y - step <= h_size:
			p_y = p_y - step
		if increment_down and p_y + step >= 0 and p_y + step <= h_size:
			p_y = p_y + step

		position = [p_x, p_y]
		#import the image
 		image = pygame.image.load("Mihai.jpg")
 		#set the dimensions of the image
 		image = pygame.transform.scale(image,(image_width,image_height))

		screen.fill(blue_color)
		
		screen.blit(image,(w_size - image_width,(h_size - image_height)/7))

		pygame.draw.circle(screen, sun, (w_size-10, 10), 70)

		pygame.draw.circle(screen, white_color, position, radius)

		pygame.display.flip()

pygame.quit()
