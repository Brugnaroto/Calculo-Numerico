import pygame
from pygame.locals import *

def car_position(x,y,carImg):
    screen.blit(carImg, (x,y))
    
def car_size(x,y,carImg):
    car = pygame.transform.scale(carImg, (x,y))
    return car

def car_delete(x,y,t,n):
    pygame.draw.rect(screen, white, (x, y+15, 100, n),t)
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fluxo de carros')
car1Img = pygame.image.load('./img/car1.png')
car2Img = pygame.image.load('./img/car2.png')
car3Img = pygame.image.load('./img/car3.png')
car4Img = pygame.image.load('./img/car4.png')
car5Img = pygame.image.load('./img/car5.png')
car6Img = pygame.image.load('./img/car6.png')
car7Img = pygame.image.load('./img/car7.png')
car8Img = pygame.image.load('./img/car8.png')
asfaltoImg = pygame.image.load('./img/asfalto.png')

screen.fill(white)
x = (display_width*0.0001)
y = (display_height*0.001)
asfalto = car_size(1000,600,asfaltoImg)

x1 = (display_width*0.01)
y1 = (display_height*0.26)
car1 = car_size(50,70,car1Img)
car1 = pygame.transform.rotate(car1,270)

x2 = (display_width*0.01)
y2 = (display_height*0.64)
car2 = car_size(60,80,car2Img)
car2 = pygame.transform.rotate(car2,270)

x3 = (display_width*0.9)
y3 = (display_height*0.16)
car3 = car_size(50,70,car3Img)
car3 = pygame.transform.rotate(car3,90)

x4 = (display_width*0.89)
y4 = (display_height*0.55)
car4 = car_size(60,80,car4Img)
car4 = pygame.transform.rotate(car4,90)

x5 = (display_width*0.315)
y5 = (display_height*0.85)
car5 = car_size(60,80,car5Img)

x6 = (display_width*0.690)
y6 = (display_height*0.85)
car6 = car_size(60,80,car6Img)

x7 = (display_width*0.245)
y7 = (display_height*0.01)
car7 = car_size(50,80,car7Img)
car7 = pygame.transform.rotate(car7,180)

x8 = (display_width*0.625)
y8 = (display_height*0.01)
car8 = car_size(50,80,car8Img)
car8 = pygame.transform.rotate(car8,180)

R = 0
S = 0
T = 0
U = 0
V = 0
X = 0
W = 0
Z = 0
troca = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("R: %.0f"%R)
            print("S: %.0f"%S)
            print("T: %.0f"%T)
            print("U: %.0f"%U)
            print("V: %.0f"%V)
            print("W: %.0f"%W)
            print("X: %.0f"%X)
            print("Z: %.0f"%Z)
            pygame.quit()
    
    car_position(x,y, asfalto)

    if x1+79 == x7 or x3-61 == x6:
        R+=1   
    if y7+79 == y3 or y6-61 == y1:
        S+=1

    if y8+79 == y3 or y5-61 == y1:
        T+=1
    if x1+81 == x8 or x3-59 == x6:
        U+=1

    #Erro em V e W
    #print(x2, x8)
    if x2+30 == x7 or x4-61 == x6:
        V+=1
    if y7+70 == y3 or y6-70 == y1:
        X+=1

    if x2+70 == x8 or x4-361 == x5:
        Z+=1
    if y8+81 == y4 or y5-30 == y2:
        W+=1
        
    if x1+80 == x7:
        x1 = x1
        if (y7 > 0 and y7 < 200) or y7 > 550:
            x1 = x1
        elif (y5 > 200 and y5 < 300) or (y5 > 100 and y5 < 450):
            x1 = x1
        else:
            x1+=1
            
    elif x1+80 == x8:
        x1 = x1

        if (y8 > 0 and y8 < 200) or y8 > 550:
            x1 = x1
        elif (y6 > 200 and y6 < 300) or (y6 > 100 and y6 < 450):
            x1 = x1
        else:
            x1+=1

    else:
        x1+=1
        
    if x2+80 == x7:
        x2 = x2
        
        if y7 < 450 and y7 > 200:
            x2 = x2
        elif y5 > 300 and y5 > 200:
            x2 = x2
        else:
            x2+=2
            
    elif x2+80 == x8:
        x2 = x2

        if y8 < 450 and y8 > 200:
            x2 = x2
        elif y6 > 300 and y6 > 200:
            x2 = x2
        else:
            x2+=2

    else:
        x2+=2
    
    if x3-60 == x6:
        x3 = x3
        
        if y6 < 300 and y6 > 50:
            x3 = x3
        elif y8 < 100 or y8 > 450:
            x3 = x3
        else:
            x3-=1
            
    elif x3-60 == x5:
        x3 = x3

        if y5 < 300 and y5 > 50:
            x3 = x3
        elif y7 < 100 or y7 > 450:
            x3 = x3
        else:
            x3-=1

    else:
        x3-=1      
        
    if x4-60 == x6:
        x4 = x4
        
        if y6 < 600 and y6 > 250:
            x4 = x4
        elif y8 < 400 and y8 > 150:
            x4 = x4
        else:
            x4-=1
            
    elif x4-60 == x5:
        x4 = x4

        if y5 < 600 and y5 > 250:
            x4 = x4
        elif y7 < 400 and y7 > 150:
            x4 = x4
        else:
            x4-=1

    else:
        x4-=1

    y5-=1
    y6-=1
    y7+=1
    y8+=1

    if x1 == display_width:
        x1 = -60
    if x2 == display_width:
        x2 = -60
    if x3 == -60:
        x3 = 860
    if x4 == -60:
        x4 = 860
    if y5 == -60:
        y5 = 650
    if y6 == -60:
        y6 = 650
    if y7 == display_height:
        y7 = -50
    if y8 == display_height:
        y8 = -50
    
    car_position(x1, y1, car1)
    car_position(x2, y2, car2)
    car_position(x3, y3, car3)
    car_position(x4, y4, car4)
    car_position(x5, y5, car5)
    car_position(x6, y6, car6)
    car_position(x7, y7, car7)
    car_position(x8, y8, car8)
    
    #pygame.display.flip()       
    pygame.display.update()
    
