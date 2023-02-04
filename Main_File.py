import pygame
from pygame.locals import * #Enhances QUIT function 
pygame.init() #Initializes functions of pygame module
screen = pygame.display.set_mode((600,600)) #Tuple = Length and Width of window
pygame.display.set_caption("trialname")
red = (200,0,0)
def show_text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("freesans",size, bold=True, italic=True)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
dict1 = {1: "",
         2: "",
         3: "",
         4: "",
         5: "",
         6: "",
         7: "",
         8: "",
         9: ""}
x = 0
y = 0
c = 1
while True:
    if dict1[1] == "X" and dict1[2] == "X" and dict1[3] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[1] == "O" and dict1[2] == "O" and dict1[3] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[1] == "X" and dict1[5] == "X" and dict1[9] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[1] == "O" and dict1[5] == "O" and dict1[9] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[4] == "X" and dict1[5] == "X" and dict1[6] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[4] == "O" and dict1[5] == "O" and dict1[6] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[7] == "X" and dict1[8] == "X" and dict1[9] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[7] == "O" and dict1[8] == "O" and dict1[9] == "O":
        print("O is the Winner!")
        break
    if dict1[3] == "X" and dict1[5] == "X" and dict1[7] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[3] == "O" and dict1[5] == "O" and dict1[7] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[1] == "X" and dict1[4] == "X" and dict1[7] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[1] == "O" and dict1[4] == "O" and dict1[7] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[2] == "X" and dict1[5] == "X" and dict1[8] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[2] == "O" and dict1[5] == "O" and dict1[8] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[3] == "X" and dict1[6] == "X" and dict1[9] == "X":
        screen.fill((0,0,0))
        show_text("X is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    if dict1[3] == "O" and dict1[6] == "O" and dict1[9] == "O":
        screen.fill((0,0,0))
        show_text("O is the Winner!",150,300,red,50)
        pygame.display.update()
        break
    pygame.draw.line(screen,red,(0,200),(600,200),20)
    pygame.draw.line(screen,red,(0,400),(600,400),20)
    pygame.draw.line(screen,red,(200,0),(200,600),20)
    pygame.draw.line(screen,red,(400,0),(400,600),20)
    if c % 2 == 0:
        if 0 < x < 200 and 0 < y < 200:
            if dict1[1] == "":
                pygame.draw.circle(screen,red,(100,100),50,10)
                c = c + 1
                dict1[1] = "O"
        if 200 < x < 400 and 0 < y < 200:
            if dict1[2] == "":
                pygame.draw.circle(screen,red,(300,100),50,10)
                c = c + 1
                dict1[2] = "O"
        if 400 < x < 600 and 0 < y < 200:
            if dict1[3] == "":
                pygame.draw.circle(screen,red,(500,100),50,10)
                c = c + 1
                dict1[3] = "O"
        if 0 < x < 200 and 200 < y < 400:
            if dict1[4] == "":
                pygame.draw.circle(screen,red,(100,300),50,10)
                c = c + 1
                dict1[4] = "O"
        if 200 < x < 400 and 200 < y < 400:
            if dict1[5] == "":
                pygame.draw.circle(screen,red,(300,300),50,10)
                c = c + 1
                dict1[5] = "O"
        if 400 < x < 600 and 200 < y < 400:
            if dict1[6] == "":
                pygame.draw.circle(screen,red,(500,300),50,10)
                c = c + 1
                dict1[6] = "O"
        if 0 < x < 200 and 400 < y < 600:
            if dict1[7] == "":
                pygame.draw.circle(screen,red,(100,500),50,10)
                c = c + 1
                dict1[7] = "O"
        if 200 < x < 400 and 400 < y < 600:
            if dict1[8] == "":
                pygame.draw.circle(screen,red,(300,500),50,10)
                c = c + 1
                dict1[8] = "O"
        if 400 < x < 600 and 400 < y < 600:
            if dict1[9] == "":
                pygame.draw.circle(screen,red,(500,500),50,10)
                c = c + 1
                dict1[9] = "O"
    if c % 2 != 0:
        if 0 < x < 200 and 0 < y < 200:
            if dict1[1] == "":
                pygame.draw.line(screen,red,(0,0),(200,200),10)
                pygame.draw.line(screen,red,(0,200),(200,0),10)
                c = c + 1
                dict1[1] = "X"
        if 200 < x < 400 and 0 < y < 200:
            if dict1[2] == "":
                pygame.draw.line(screen,red,(200,0),(400,200),10)
                pygame.draw.line(screen,red,(400,0),(200,200),10)
                c = c + 1
                dict1[2] = "X"
        if 400 < x < 600 and 0 < y < 200:
            if dict1[3] == "":
                pygame.draw.line(screen,red,(400,0),(600,200),10)
                pygame.draw.line(screen,red,(400,200),(600,0),10)
                c = c + 1
                dict1[3] = "X"
        if 0 < x < 200 and 200 < y < 400:
            if dict1[4] == "":
                pygame.draw.line(screen,red,(0,200),(200,400),10)
                pygame.draw.line(screen,red,(200,200),(0,400),10)
                c = c + 1
                dict1[4] = "X"
        if 200 < x < 400 and 200 < y < 400:
            if dict1[5] == "":
                pygame.draw.line(screen,red,(200,200),(400,400),10)
                pygame.draw.line(screen,red,(400,200),(200,400),10)
                c = c + 1
                dict1[5] = "X"
        if 400 < x < 600 and 200 < y < 400:
            if dict1[6] == "":
                pygame.draw.line(screen,red,(400,200),(600,400),10)
                pygame.draw.line(screen,red,(600,200),(400,400),10)
                c = c + 1
                dict1[6] = "X"
        if 0 < x < 200 and 400 < y < 600:
            if dict1[7] == "":
                pygame.draw.line(screen,red,(0,400),(200,600),10)
                pygame.draw.line(screen,red,(200,400),(0,600),10)
                c = c + 1
                dict1[7] = "X"
        if 200 < x < 400 and 400 < y < 600:
            if dict1[8] == "":
                pygame.draw.line(screen,red,(200,400),(400,600),10)
                pygame.draw.line(screen,red,(400,400),(200,600),10)
                c = c + 1
                dict1[8] = "X"
        if 400 < x < 600 and 400 < y < 600:
            if dict1[9] == "":
                pygame.draw.line(screen,red,(400,400),(600,600),10)
                pygame.draw.line(screen,red,(600,400),(400,600),10)
                c = c + 1
                dict1[9] = "X"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
