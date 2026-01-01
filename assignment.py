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

charizard = pygame.image.load("charizard.png")
opponentBlastoise = pygame.image.load("blastoise.png")

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

pokemonStats = {
    "charizard": {
        "pokemon": charizard,
        "hp": 150,
        "maxHP": 150,
        "x": 100,
        "y": 325,
        "xOG": 100,
        "yOG": 325,
        "moves": {
            "fireBlast": {"type": "FIRE","power": 20,"pp": 5,"maxPP": 5},
            "dragonClaw": {"type": "DRAGON","power": 30,"pp": 3,"maxPP": 3},
            "slash": {"type": "NORMAL","power": 15,"pp": 10,"maxPP": 10}
        }
    }
}

opponentStats = {   
    "blastoise": {
        "pokemon": opponentBlastoise,
        "hp": 160,
        "maxHP": 160,
        "x": 710,
        "y": 55,
        "xOG": 710,
        "yOG": 55,
        "moves": {
            "hydroPump": {"type": "WATER","power": 40,"pp": 5,"maxPP": 5},
            "bite": {"type": "DARK","power": 25,"pp": 10,"maxPP": 10},
            "tackle": {"type": "NORMAL","power": 15,"pp": 15,"maxPP": 15}
        }
    }
}

gamestate = "battleMenu"
playerPokemon = "charizard"
opponentPokemon = "blastoise"
isAttacking = False
opponentAttack = False
attackPos = 0

# pygame setup
pygame.init()
buttonFont = pygame.font.Font("PokemonGb-RAeo.ttf", 50)
moveFont = pygame.font.Font("PokemonGb-RAeo.ttf", 35)  
whatWillFont = pygame.font.Font("PokemonGb-RAeo.ttf", 20)
attackTypeFont = pygame.font.Font("PokemonGb-RAeo.ttf", 15)

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

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
                if playerPokemon == "charizard":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["fireBlast"]["power"]
                            isAttacking = True
                            opponentAttack = True
                            print("Fire Blast used! PP left:", pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["slash"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["slash"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["slash"]["power"]
                            isAttacking = True
                            opponentAttack = True
                            print("Slash used! PP left:", pokemonStats[playerPokemon]["moves"]["slash"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        if pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["dragonClaw"]["power"]
                            isAttacking = True
                            opponentAttack = True
                            print("Dragon Claw used! PP left:", pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"])
                    elif 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                        gamestate = "battleMenu"
    
    if isAttacking:
        if attackPos < 10:
            pokemonStats[playerPokemon]["x"] += 5
            pokemonStats[playerPokemon]["y"] -= 3
        elif attackPos < 20:    
            pokemonStats[playerPokemon]["x"] -= 5
            pokemonStats[playerPokemon]["y"] += 3
        else:
            pokemonStats[playerPokemon]["x"] = pokemonStats[playerPokemon]["xOG"]
            pokemonStats[playerPokemon]["y"] = pokemonStats[playerPokemon]["yOG"]
            isAttacking = False
        attackPos += 1
    else:
        attackPos = 0
    
    if opponentAttack:
        if attackPos < 10:
            opponentStats[opponentPokemon]["x"] -= 5
            opponentStats[opponentPokemon]["y"] += 3
        elif attackPos < 20:    
            opponentStats[opponentPokemon]["x"] += 5
            opponentStats[opponentPokemon]["y"] -= 3
        else:
            opponentStats[opponentPokemon]["x"] = opponentStats[opponentPokemon]["xOG"]
            opponentStats[opponentPokemon]["y"] = opponentStats[opponentPokemon]["yOG"]
            opponentAttack = False
        attackPos += 1

    if gamestate == "homeMenu":  
        screen.blit(battleBg,(0,0))
        screen.blit(aiGround,(690,280))
        screen.blit(fightUI,(0,575))

    if gamestate == "battleMenu":
        playerHP = pokemonStats[playerPokemon]["hp"]
        playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
        opponentHP = opponentStats[opponentPokemon]["hp"]
        opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]
        screen.blit(battleBg,(0,0))
        screen.blit(aiGround,(690,280))
        screen.blit(playerGround,(50,500))
        screen.blit(pokemonStats[playerPokemon]["pokemon"],(pokemonStats[playerPokemon]["x"],pokemonStats[playerPokemon]["y"]))
        screen.blit(opponentStats[opponentPokemon]["pokemon"],(opponentStats[opponentPokemon]["x"],opponentStats[opponentPokemon]["y"]))
        pygame.draw.rect(screen, RED, (100, 280, 200, 20))
        pygame.draw.rect(screen, GREEN, (100, 280, 200 * (playerHP / playerMaxHP), 20))
        pygame.draw.rect(screen, RED, (700, 20, 200, 20))
        pygame.draw.rect(screen, GREEN, (700, 20, 200 * (opponentHP / opponentMaxHP), 20))
        screen.blit(fightUI,(0,575))

        # Buttons
        fightText = buttonFont.render("FIGHT", True, WHITE)   
        screen.blit(fightText, (120, 622))
        backText = buttonFont.render("BACK", True, WHITE)   
        screen.blit(backText, (585, 622))
        pokemonText = buttonFont.render("POKéMON", True, WHITE)   
        screen.blit(pokemonText, (60, 722))
        runText = buttonFont.render("RUN", True, WHITE)   
        screen.blit(runText, (605, 722))
        whatWillText = whatWillFont.render("WHAT WILL", True, 'black')   
        screen.blit(whatWillText, (965, 630))
        yourPokemonText = whatWillFont.render("YOUR", True, 'black')   
        screen.blit(yourPokemonText, (1010, 660))
        PokeText = whatWillFont.render("POKéMON", True, 'black')   
        screen.blit(PokeText, (980, 690))
        doText = whatWillFont.render("DO?", True, 'black')   
        screen.blit(doText, (1020, 720))
        
        # Mouse Hover Effect
        if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
            #screen.blit(fightUI2,(0,513))
            fightText = buttonFont.render("FIGHT", True, LIGHTGRAY)   
            screen.blit(fightText, (120, 622))
        if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
            backText = buttonFont.render("BACK", True, LIGHTGRAY)   
            screen.blit(backText, (585, 622))
        if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
            pokemonText = buttonFont.render("POKéMON", True, LIGHTGRAY)   
            screen.blit(pokemonText, (60, 722))
        if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
            runText = buttonFont.render("RUN", True, LIGHTGRAY)   
            screen.blit(runText, (605, 722))
    
    if gamestate == "fightMenu":
            playerHP = pokemonStats[playerPokemon]["hp"]
            playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
            opponentHP = opponentStats[opponentPokemon]["hp"]
            opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]
            screen.blit(battleBg,(0,0))
            screen.blit(aiGround,(690,280))
            screen.blit(playerGround,(50,500))
            screen.blit(pokemonStats[playerPokemon]["pokemon"],(pokemonStats[playerPokemon]["x"],pokemonStats[playerPokemon]["y"]))
            screen.blit(opponentStats[opponentPokemon]["pokemon"],(opponentStats[opponentPokemon]["x"],opponentStats[opponentPokemon]["y"]))
            pygame.draw.rect(screen, RED, (100, 280, 200, 20))
            pygame.draw.rect(screen, GREEN, (100, 280, 200 * (playerHP / playerMaxHP), 20))
            pygame.draw.rect(screen, RED, (700, 20, 200, 20))
            pygame.draw.rect(screen, GREEN, (700, 20, 200 * (opponentHP / opponentMaxHP), 20))
            screen.blit(fightUI,(0,575))

            if playerPokemon == "charizard":
                fireBlastText = moveFont.render("FIRE BLAST", True, WHITE)   
                screen.blit(fireBlastText, (70, 622))
                backText = moveFont.render("SLASH", True, WHITE)   
                screen.blit(backText, (590, 622))
                dragonClawText = moveFont.render("DRAGON CLAW", True, WHITE)   
                screen.blit(dragonClawText, (45, 722))
                slashText = buttonFont.render("RUN", True, WHITE)   
                screen.blit(slashText, (605, 722))

                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    fireBlastText = moveFont.render("FIRE BLAST", True, LIGHTGRAY)   
                    screen.blit(fireBlastText, (70, 622))
                    attackTypeText = attackTypeFont.render("TYPE: FIRE", True, 'red')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["fireBlast"]["maxPP"]), True, 'black')
                    screen.blit(PPText, (975, 685))

                if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    backText = moveFont.render("SLASH", True, LIGHTGRAY)   
                    screen.blit(backText, (590, 622))
                    attackTypeText = attackTypeFont.render("TYPE: NORMAL", True, 'black')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["slash"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["slash"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))      

                if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    dragonClawText = moveFont.render("DRAGON CLAW", True, LIGHTGRAY)   
                    screen.blit(dragonClawText, (45, 722))
                    attackTypeText = attackTypeFont.render("TYPE: DRAGON", True, 'blue')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["dragonClaw"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))
                    
                if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                    slashText = buttonFont.render("RUN", True, LIGHTGRAY)   
                    screen.blit(slashText, (605, 722))

        # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()