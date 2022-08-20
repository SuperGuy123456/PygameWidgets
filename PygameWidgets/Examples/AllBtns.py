from PygameWidgets import Btn
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
Button=Btn.Normal_Btn(screen,size=50,fgcolor=(0,255,0),xy=(0,0),Outline=(255,0,0))
run=True
while run:
    screen.fill((0,0,0))
    Button.Draw()
    pygame.display.update()
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        YN=Button.Detect(mousepos,event)
        if YN:
            print('clicked!')
pygame.quit()
