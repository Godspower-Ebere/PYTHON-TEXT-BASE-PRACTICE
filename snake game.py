import pygame
pygame.init()
white=(255,255,255)
red=(255,0,0)
size=s_width,s_height=800,600
win=pygame.display.set_mode(size)
x=400
y=300
width=10
height=10
run=True
while run :
    win.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.type==pygame.K_LEFT:
                x-=10


    pygame.draw.rect(win,red,(x,y,width,height))
    pygame.display.update()
pygame.quit()
