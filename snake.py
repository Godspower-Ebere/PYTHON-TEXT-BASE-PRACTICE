import pygame
pygame.init()
color=(255,192,192)
snake=(50,28,59)
size=w,h=500,500
win=pygame.display.set_mode(size)
x,y,width,height,vel=400,400,30,30,5
running=True
def drawing():
    win.fill(color)
    pygame.draw.rect(win,snake,[x,y,width,height])
    pygame.display.update()
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x-=vel
    if key[pygame.K_RIGHT]:
        x+=vel
    if key[pygame.K_UP]:
        y-=vel
    if key[pygame.K_DOWN]:
        y+=vel
        if event.type==pygame.KEYUP:
            if event.type==pygame.K_LEFT:
                x-=vel
    drawing()
    
pygame.quit()
