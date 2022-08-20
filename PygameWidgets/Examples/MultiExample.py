from PygameWidgets import Cursor,Btn,Clock,Colors
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500),pygame.RESIZABLE)
Button=Btn.Normal_Btn(screen,text='Click',xy=(200,200),size=50)
#ActiveBtn=Btn.Active_Btn(screen,text='Hello',Colors=((255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,255,255)),X=100,Y=100)
ActiveBtn=Btn.Active_Btn(screen,text='Hello',Colors=(Colors.Red,Colors.Green,Colors.Blue,Colors.Black,Colors.White),X=100,Y=100)
run=True
size=5
C=Cursor.Rect_Cursor(screen,Width=size,Height=size)
FPS=60
Clock=Clock.Clock(FPS)
Clock.Set_Up_Clock()
while run:
    Clock.Set_FPS()
    screen.fill((0,0,0))
    C.Draw()
    Button.Draw()
    ActiveBtn.Draw()
    mousepos=(C.x,C.y)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
        YN=Button.Detect(mousepos,e)
        YN1=ActiveBtn.Detect(mousepos,e)
        if YN:
            
            size+=5
            C=Cursor.Rect_Cursor(screen,Width=size,Height=size)
            
        if YN1:
            #print('Custom!')
            
            size+=10
            C=Cursor.Rect_Cursor(screen,Width=size,Height=size)
            
        
pygame.quit()
