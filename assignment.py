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

battleBg = pygame.image.load("battleBG.png")
dsBG = pygame.image.load("DS BG.png")
bg = pygame.image.load("r1UVBhX.png")

RED = (239, 57, 56)
ORANGE = (232, 155, 39)
BLUE = (42, 148, 206)
GREEN = (90, 181, 41)
BEIGE = (239, 255, 216)

# pygame setup
pygame.init()
font = pygame.font.Font("PokemonGb-RAeo.ttf", 20)

screen = pygame.display.set_mode((700, 727))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouseX, mouseY = pygame.mouse.get_pos()

    # fill the screen with a color to wipe away anything from last frame
    print(mouseX, mouseY)
    screen.blit(dsBG,(0,0))    
    screen.blit(battleBg,(187,53))
    #screen.blit(bg,(100,-250))

    pygame.draw.rect(screen, BEIGE, (186, 423, 328, 247))

    #pygame.draw.rect(screen, 'white', (250, 440, 200, 120), border_radius = 10)
    pygame.draw.rect(screen, 'black', (255, 445, 190, 115), border_radius = 10)
    pygame.draw.rect(screen, RED, (255, 445, 190, 110), border_radius = 10)
    textSurface = font.render("FIGHT", True, 'black')
    screen.blit(textSurface, (300, 490))


    pygame.draw.rect(screen, ORANGE, (190, 570, 105, 90), border_radius = 10)
    textSurface = font.render("BAG", True, 'black')
    screen.blit(textSurface, (220, 610))

    pygame.draw.rect(screen, BLUE, (315, 570, 105, 90), border_radius = 10)
    textSurface = font.render("RUN", True, 'black')
    screen.blit(textSurface, (340, 610))

    pygame.draw.rect(screen, GREEN, (440, 570, 105, 90), border_radius = 10)
    textSurface = font.render("POKéMON", True, 'black')
    screen.blit(textSurface, (460, 610))



    # RENDER YOUR GAME HERE
    userCharizardIdle.render(screen,(210,180))
    opponentBlastoiseIdle.render(screen,(390,110))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()