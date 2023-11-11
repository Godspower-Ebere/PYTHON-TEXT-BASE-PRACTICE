import pygame
from pygame.locals import *
pygame.init()
background=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
size=width,height=100,200
screen=pygame.display.set_mode(size)
font=pygame.font.SysFont("tahoma",50)
style=font.render("q is pressed",1,red)
run=True
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_r:
				background=red
				
				
				
				
				
	screen.fill(background)
	pygame.display.update()
pygame.quit()