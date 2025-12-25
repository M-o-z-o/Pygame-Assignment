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

userCharizardIdle = pygame.image.load("charizard.png")
opponentBlastoiseIdle = pygame.image.load("blastoise.png")

battleBg = pygame.image.load("battlebggold (1).png")
aiGround = pygame.image.load("aiground (1).png")
playerGround = pygame.image.load("playerground.png")
fightUI = pygame.image.load("battleUI.png")
fightUI2 = pygame.image.load("pixil-frame-0 (1).png")

RED = (239, 57, 56)
ORANGE = (232, 155, 39)
BLUE = (42, 148, 206)
GREEN = (90, 181, 41)
BEIGE = (239, 255, 216)
GRAY = (145, 145, 145)
LIGHTGRAY = (184, 184, 184)
WHITE = (248, 248, 248)

gamestate = "battleMenu"

# pygame setup
pygame.init()
font = pygame.font.Font("PokemonGb-RAeo.ttf", 50)

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clickX, clickY = event.pos

            if gamestate == "battleMenu":
                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    gamestate = "fightMenu"
                elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    gamestate = "homeMenu"
                elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    gamestate = "pokemonMenu"
                elif 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                    gamestate = "runMenu"

            elif gamestate == "fightMenu":
                if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    gamestate = "battleMenu"

    if gamestate == "homeMenu":  
        screen.blit(battleBg,(0,0))
        screen.blit(aiGround,(690,280))
        screen.blit(fightUI,(0,575))

    if gamestate == "battleMenu":
        screen.blit(battleBg,(0,0))
        screen.blit(aiGround,(690,280))
        screen.blit(playerGround,(50,500))
        screen.blit(userCharizardIdle,(100,325))
        screen.blit(opponentBlastoiseIdle,(710,55))
        screen.blit(fightUI,(0,575))

        # Buttons
        fightText = font.render("FIGHT", True, WHITE)   
        screen.blit(fightText, (120, 622))
        backText = font.render("BACK", True, WHITE)   
        screen.blit(backText, (585, 622))
        pokemonText = font.render("POKéMON", True, WHITE)   
        screen.blit(pokemonText, (60, 722))
        runText = font.render("RUN", True, WHITE)   
        screen.blit(runText, (605, 722))

        # Mouse Hover Effect
        if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
            #screen.blit(fightUI2,(0,513))
            fightText = font.render("FIGHT", True, LIGHTGRAY)   
            screen.blit(fightText, (120, 622))
        if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
            backText = font.render("BACK", True, LIGHTGRAY)   
            screen.blit(backText, (585, 622))
        if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
            pokemonText = font.render("POKéMON", True, LIGHTGRAY)   
            screen.blit(pokemonText, (60, 722))
        if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
            runText = font.render("RUN", True, LIGHTGRAY)   
            screen.blit(runText, (605, 722))
    
    if gamestate == "fightMenu":
        screen.blit(battleBg,(0,0))
        screen.blit(aiGround,(690,280))
        screen.blit(playerGround,(50,500))
        screen.blit(userCharizardIdle,(100,325))
        screen.blit(opponentBlastoiseIdle,(710,55))
        screen.blit(fightUI,(0,575))

        backText = font.render("BACK", True, WHITE)   
        screen.blit(backText, (585, 622))

        if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
            backText = font.render("BACK", True, LIGHTGRAY)   
            screen.blit(backText, (585, 622))


        # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()