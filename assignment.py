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

#Links needed for sprites
#https://pokemondb.net/move/generation/5
#https://pokemondb.net/sprites

# Example file showing a basic pygame "game loop"
import pygame
import gif_pygame

userCharizardIdle = gif_pygame.load("charizard.gif")
opponentBlastoiseIdle = gif_pygame.load("blastoise.gif")

battleBg = pygame.image.load("battleBG2.jpg")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(battleBg,(0,0))

    # RENDER YOUR GAME HERE
    userCharizardIdle.render(screen,(80,100))
    opponentBlastoiseIdle.render(screen,(290,60))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()