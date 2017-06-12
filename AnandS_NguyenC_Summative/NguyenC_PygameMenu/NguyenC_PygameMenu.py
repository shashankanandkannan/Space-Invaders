import pygame
from pygame.locals import *
pygame.mixer.init()

pygame.init()  

import os, time, random

import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

size = (640,480)  
screen = pygame.display.set_mode(size) 

pygame.display.set_caption("Space Invaders")

background = pygame.image.load("background\menu1.jpg").convert()
background2= pygame.image.load("background\menu2.jpg").convert()
background3= pygame.image.load("background\instructionsbkg.jpg").convert()

pygame.display.flip() 

clock = pygame.time.Clock() 
keepGoing = True 	    

pygame.font.init()
font_path = "PixelSplitter-Bold.ttf"
font_size = 10
fontObj = pygame.font.Font(font_path, font_size)

#objects
spaceship=pygame.image.load("spaceship1.png").convert_alpha()
asteroid=pygame.image.load("newast.png").convert_alpha()
ufo=pygame.image.load("UFO.png").convert_alpha()


#sound
mute=pygame.image.load("volume\mute.png").convert_alpha()
sound=pygame.image.load("volume\sound.png").convert_alpha()
mute2=pygame.image.load("volume\mute2.png").convert_alpha()
sound2=pygame.image.load("volume\sound2.png").convert_alpha()

#text
credit = fontObj.render(('Credits'), True, (255,255,255))
credittext1 = fontObj.render(('Graphic Designer'), True, (255,255,255))
credittext2 = fontObj.render(('Software Engineer'), True, (255,255,255))
musictext = fontObj.render(('Music'), True, (255,255,255))

instructionstext1 = fontObj.render(('Use arrow keys to move your spaceship'), True, (255,255,255))
instructionstext2 = fontObj.render(('Press spacebar to shoot'), True, (255,255,255))
instructionstext3 = fontObj.render(('Dodge lasers by hiding behind the asteroids'), True, (255,255,255))

hp=fontObj.render(('12 HP'), True, (0,245,46))
orange=fontObj.render(('10 pts'), True, (0,245,46))
blue=fontObj.render(('20 pts'), True, (0,245,46))
green=fontObj.render(('40 pts'), True, (0,245,46))
ufotext=fontObj.render(('??? pts'), True, (0,245,46))

#enemies
orangeenemy=pygame.image.load("enemy1.png").convert_alpha()
blueenemy=pygame.image.load("enemy2.png").convert_alpha()
greenenemy=pygame.image.load("enemy3.png").convert_alpha()

#buttons
btnStart=pygame.image.load("start\startbutt1.png").convert_alpha()
btnInstruct=pygame.image.load("instru\instrubutt1.png").convert_alpha()
btnExit=pygame.image.load("exit\exit1.png").convert_alpha()
btnBack1=pygame.image.load("back\\back1.png").convert_alpha()

credit2 = fontObj.render(('Credits'), True, (0,245,46))
btnStart2=pygame.image.load("start\startbutt2.png").convert_alpha()
btnInstruct2=pygame.image.load("instru\instrubutt2.png").convert_alpha()
btnExit2=pygame.image.load("exit\exit2.png").convert_alpha()
btnBack2=pygame.image.load("back\\back2.png").convert_alpha()

#variables
state="menu"
volume="sound"
music = "start"

#blit sound
m=screen.blit(mute, (600, 450))
s=screen.blit(sound, (600, 450))

#music
pygame.mixer.music.load("DANCE_TILL_YOURE_DEAD.wav")

try:
    while keepGoing:
        clock.tick(60)
        screen.blit(background, (0, 0))
        
        x=265
        y=200
        if state=="menu":
            if volume=="sound":
                s=screen.blit(sound, (600, 450))

            if volume=="mute":
                m=screen.blit(mute, (600, 450))
                
            a=pygame.mouse.get_pos()
        
            bn=screen.blit(btnStart,(x,y))    
            bi=screen.blit(btnInstruct,(x,y+50))    
            be=screen.blit(btnExit,(x,y+100))

            c=screen.blit(credit, (x-240, y+250))

            if bn.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart2, (x, y))
                bi=screen.blit(btnInstruct,(x,y+50))    
                be=screen.blit(btnExit,(x,y+100))
                screen.blit(credit, (x-240, y+250))
                
            if bi.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart, (x, y))
                bi=screen.blit(btnInstruct2,(x,y+50))    
                be=screen.blit(btnExit,(x,y+100))
                screen.blit(credit, (x-240, y+250))

            if be.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart, (x, y))
                bi=screen.blit(btnInstruct,(x,y+50))    
                be=screen.blit(btnExit2,(x,y+100))
                screen.blit(credit, (x-240, y+250))

            if c.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart, (x, y))
                bi=screen.blit(btnInstruct,(x,y+50))    
                be=screen.blit(btnExit,(x,y+100))
                screen.blit(credit2, (x-240, y+250))
                

            if s.collidepoint(a) and volume!="mute":
                screen.blit(sound2, (600, 450))

            if music == "start" and volume == "sound":
                pygame.mixer.music.play(-1)
                music = "playing"
            elif volume == "mute":
                pygame.mixer.music.pause()
                music = "stopped"
                if m.collidepoint(a):
                    screen.blit(mute2, (600, 450))
            elif music == "stopped" and volume == "sound":
                pygame.mixer.music.unpause()
                music = "playing"
                if s.collidepoint(a):
                    screen.blit(sound2, (600, 450))
                
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    if bn.collidepoint(a):
                        state="game"
                    elif bi.collidepoint(a):
                        state="instructions"
                    elif be.collidepoint(a):
                        keepGoing = False
                    elif c.collidepoint(a):
                        state="credits"
                    else:
                         if m.collidepoint(a) or s.collidepoint(a):
                            if volume=="sound":
                                volume="mute"
                            else:
                                volume="sound"

        if state=="game":  
            # ---------------code for the game-------------------               
            a=pygame.mouse.get_pos()

            screen.blit(background3, (0, 0))
            bb=screen.blit(btnBack1,(x,y+200))


            if bb.collidepoint(a):
                screen.blit(background3, (0, 0))
                bb=screen.blit(btnBack2, (x, y+200))

            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: 
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bb.collidepoint(a):
                        state="menu"

           
        if state=="instructions":
            a=pygame.mouse.get_pos()

        
            screen.blit(background3, (0, 0))

            if volume=="sound":
                s=screen.blit(sound, (600, 450))

            if volume=="mute":
                m=screen.blit(mute, (600, 450))
                
            bb=screen.blit(btnBack1,(x,y+200))

            screen.blit(instructionstext1, (25,125))
            screen.blit(instructionstext2, (25,150))
            screen.blit(instructionstext3, (25,175))
            
            screen.blit(orangeenemy, (425,250))
            screen.blit(blueenemy, (375,250))
            screen.blit(greenenemy, (325,250))

            screen.blit(orange, (425,275))
            screen.blit(blue, (375,275))
            screen.blit(green, (325,275))
            screen.blit(ufotext, (175,275))

            screen.blit(spaceship, (350, 100))
            screen.blit(asteroid, (25, 250))
            screen.blit(ufo, (175, 250))

            screen.blit(hp, (25, 250))


            if bb.collidepoint(a):
                screen.blit(background3, (0, 0))
                screen.blit(instructionstext1, (25,125))
                screen.blit(instructionstext2, (25,150))
                screen.blit(instructionstext3, (25,175))
                screen.blit(orangeenemy, (425,250))
                screen.blit(blueenemy, (375,250))
                screen.blit(greenenemy, (325,250))

                screen.blit(orange, (425,275))
                screen.blit(blue, (375,275))
                screen.blit(green, (325,275))
                screen.blit(ufotext, (175,275))

                screen.blit(spaceship, (350, 100))
                screen.blit(asteroid, (25, 250))
                screen.blit(ufo, (175, 250))

                screen.blit(hp, (25, 250)) 
                bb=screen.blit(btnBack2, (x, y+200))

            if s.collidepoint(a) and volume!="mute":
                screen.blit(sound2, (600, 450))

            if music == "start" and volume == "sound":
                pygame.mixer.music.play(-1)
                music = "playing"
            elif volume == "mute":
                pygame.mixer.music.pause()
                music = "stopped"
                if m.collidepoint(a):
                    screen.blit(mute2, (600, 450))
            elif music == "stopped" and volume == "sound":
                pygame.mixer.music.unpause()
                music = "playing"
                if s.collidepoint(a):
                    screen.blit(sound2, (600, 450))
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    if bb.collidepoint(a):
                        state="menu"
                    else:
                         if m.collidepoint(a) or s.collidepoint(a):
                            if volume=="sound":
                                volume="mute"
                            else:
                                volume="sound"


        if state=="credits":
            a=pygame.mouse.get_pos()

            screen.blit(background3, (0, 0))
            screen.blit(credittext1, (25,125))
            screen.blit(credittext2, (25,150))
            screen.blit(musictext, (25,175))
            bb=screen.blit(btnBack1,(x,y+200))


            if bb.collidepoint(a):
                screen.blit(background3, (0, 0))
                bb=screen.blit(btnBack2, (x, y+200))

            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: 
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bb.collidepoint(a):
                        state="menu"

                  
        pygame.display.flip()
              
                    

finally:
    pygame.quit()  
