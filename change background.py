import pygame
import math
pygame.init()

size=width,height=(600,300)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("white color".upper())

#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
cyan=(0,255,255)
background=(255,255,255)
black=(0,0,0)
#font
fsize=math.sqrt(height)
myfont=pygame.font.SysFont("tahoma",int(fsize))
font=myfont.render("PRESS SOME ALPHABET TO CHANGE THE BG-COLOR",10,black)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                background=red
                pygame.display.set_caption("RED color".upper())
            if event.key==pygame.K_g:
                background=green
                pygame.display.set_caption("green color".upper())
            if event.key==pygame.K_b:
                background=blue
                pygame.display.set_caption("blue color".upper())
            if event.key==pygame.K_y:
                background=yellow
                pygame.display.set_caption("yellow color".upper())
            if event.key==pygame.K_c:
                background=cyan
                pygame.display.set_caption("cyan color".upper())
            if event.key==pygame.K_w:
                background=(255,255,255)
                pygame.display.set_caption("white color".upper( ))



        screen.fill(background)
        screen.blit(font,(width/5.5,height/2))
        pygame.display.update()
pygame.quit()
