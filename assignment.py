'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

import pygame
pygame.init()

# *********SETUP**********
deadPoolSpriteSheet = pygame.image.load('idle3.png')

windowWidth = 1200
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate
deadPoolPatchSize = [0,0,84.5,114]
deadPoolPatchNum = 0
numOfDeadPoolPatches = 12

deadPoolFrameRate = 6
frameCount = 0

deadPoolPos = [700,500]

# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop
   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
    if (frameCount % deadPoolFrameRate == 0):
        if (deadPoolPatchNum < numOfDeadPoolPatches - 1):
            deadPoolPatchNum += 1
            deadPoolPatchSize[0] += deadPoolPatchSize[2]
        else:
            deadPoolPatchNum = 0
            deadPoolPatchSize[0] = 0
    frameCount += 1

    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********
    window.fill((255,255,255))  #clear screen by filling it with black
    window.blit(deadPoolSpriteSheet, deadPoolPos, deadPoolPatchSize)

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''
    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()