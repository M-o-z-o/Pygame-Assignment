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
import random

charizard = pygame.image.load("charizard.png")
charizardMini = pygame.image.load("charizard mini.png")
pikachu = pygame.image.load("pikachu.png")
pickachuMini = pygame.image.load("pikachu mini.png")
gardevoir = pygame.image.load("gardevoir.png")
gardevoirMini = pygame.image.load("gardevoir mini.png")
celebi = pygame.image.load("celebi.png")
celebiMini = pygame.image.load("celebi mini.png")
lucario = pygame.image.load("lucario.png")
lucarioMini = pygame.image.load("lucario mini.png")

opponentBlastoise = pygame.image.load("blastoise.png")
opponentGengar = pygame.image.load("gengar.png")
opponentMewtwo = pygame.image.load("mewtwo.png")

mainMenuBg = pygame.image.load("pokeball bg.webp")
battleBg = pygame.image.load("battlebggold (1).png")
aiGround = pygame.image.load("aiground (1).png")
playerGround = pygame.image.load("playerground.png")
fightUI = pygame.image.load("battleUI.png")
fightUI2 = pygame.image.load("pixil-frame-0 (1).png")
pKMenuUI = pygame.image.load("pixil-frame-0 (5).png")

RED = (239, 57, 56)
ORANGE = (232, 155, 39)
BLUE = (42, 148, 206)
GREEN = (90, 181, 41)
BEIGE = (239, 255, 216)
GRAY = (49, 49, 49)
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
    },
    "pikachu": {
        "pokemon": pikachu,
        "hp": 100,
        "maxHP": 100,
        "x": 100,
        "y": 325,
        "xOG": 100,
        "yOG": 325,
        "moves": {
            "thunderbolt": {"type": "ELECTRIC","power": 25,"pp": 5,"maxPP": 5},
            "quickAttack": {"type": "NORMAL","power": 15,"pp": 10,"maxPP": 10},
            "tackle": {"type": "NORMAL","power": 15,"pp": 15,"maxPP": 15}
        }
    },
    "gardevoir": {
        "pokemon": gardevoir,
        "hp": 120,
        "maxHP": 120,
        "x": 50,
        "y": 325,
        "xOG": 50,
        "yOG": 325,
        "moves": {
            "psychic": {"type": "PSYCHIC","power": 25,"pp": 5,"maxPP": 5},
            "moonblast": {"type": "FAIRY","power": 30,"pp": 5,"maxPP": 5},
            "tackle": {"type": "NORMAL","power": 15,"pp": 15,"maxPP": 15}
        }
    },
    "celebi": {
        "pokemon": celebi,
        "hp": 140,
        "maxHP": 140,
        "x": 50,
        "y": 325,
        "xOG": 50,
        "yOG": 325,
        "moves": {
            "psystrike": {"type": "PSYCHIC","power": 30,"pp": 5,"maxPP": 5},
            "moonblast": {"type": "FAIRY","power": 30,"pp": 5,"maxPP": 5},
            "tackle": {"type": "NORMAL","power": 10,"pp": 15,"maxPP": 15}
        }
    },
    "lucario": {
        "pokemon": lucario,
        "hp": 130,
        "maxHP": 130,
        "x": 50,
        "y": 325,
        "xOG": 50,
        "yOG": 325,
        "moves": {
            "aurasphere": {"type": "FIGHTING","power": 25,"pp": 5,"maxPP": 5},
            "dragonPulse": {"type": "DRAGON","power": 30,"pp": 5,"maxPP": 5},
            "tackle": {"type": "NORMAL","power": 10,"pp": 15,"maxPP": 15}
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
            "hydroPump": {"type": "WATER","power": 30,"pp": 5,"maxPP": 5},
            "bite": {"type": "DARK","power": 20,"pp": 10,"maxPP": 10},
            "tackle": {"type": "NORMAL","power": 15,"pp": 15,"maxPP": 15}
        }
    },
    "gengar": {
        "pokemon": opponentGengar,
        "hp": 140,
        "maxHP": 140,
        "x": 710,
        "y": 55,
        "xOG": 710,
        "yOG": 55,
        "moves": {
            "shadowBall": {"type": "GHOST","power": 25,"pp": 5,"maxPP": 5},
            "darkPulse": {"type": "DARK","power": 30,"pp": 5,"maxPP": 5},
            "tackle": {"type": "NORMAL","power": 15,"pp": 15,"maxPP": 15}
        }
    },
    "mewtwo": {
        "pokemon": opponentMewtwo,
        "hp": 180,
        "maxHP": 180,
        "x": 710,
        "y": 40,
        "xOG": 710,
        "yOG": 40,
        "moves": {
            "futureSight": {"type": "PSYCHIC","power": 45,"pp": 3,"maxPP": 5},
            "shadowBall": {"type": "GHOST","power": 25,"pp": 5,"maxPP": 5},
            "tackle": {"type": "NORMAL","power": 10,"pp": 15,"maxPP": 15}
        }
    }
}

gamestate = "battleMenu"
playerTeam = ["pikachu", "gardevoir", "celebi", "lucario", "charizard"]
playerTeamNumber = 0
playerPokemon = playerTeam[4]
opponentTeam = ["blastoise", "gengar", "mewtwo"]
opponentTeamNumber = 0
opponentPokemon = opponentTeam[opponentTeamNumber]
turn = "player"
isAttacking = False
opponentAttacking = False
opponentIsAttacking = False
playerPokemonFainted = False
opponentAttackPos = 0
attackPos = 0
pKMenuColor = (113,154,154)

# pygame setup
pygame.init()
menuFont = pygame.font.Font("PokemonGb-RAeo.ttf", 65)
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
        #print(mouseX, mouseY)

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
            
            elif gamestate == "pokemonMenu":
                if 10 <= mouseX <= 340 and 195 <= mouseY <= 310 and pokemonStats[playerTeam[0]]["hp"] > 0:
                    playerPokemon = playerTeam[0]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 440 <= mouseX <= 770 and 195 <= mouseY <= 310 and pokemonStats[playerTeam[1]]["hp"] > 0:
                    playerPokemon = playerTeam[1]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 10 <= mouseX <= 340 and 350 <= mouseY <= 470 and pokemonStats[playerTeam[2]]["hp"] > 0:
                    playerPokemon = playerTeam[2]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 440 <= mouseX <= 770 and 350 <= mouseY <= 470 and pokemonStats[playerTeam[3]]["hp"] > 0:
                    playerPokemon = playerTeam[3]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 855 <= mouseX <= 1180 and 280 <= mouseY <= 400 and pokemonStats[playerTeam[4]]["hp"] > 0:
                    playerPokemon = playerTeam[4]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 1100 <= mouseX <= 1175 and 450 <= mouseY <= 470 and not playerPokemonFainted:
                    gamestate = "battleMenu"

            elif gamestate == "fightMenu" and turn == "player" and not isAttacking:
                if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                       gamestate = "battleMenu"

                if playerPokemon == "charizard":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["fireBlast"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Fire Blast used! PP left:", pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["slash"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["slash"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["slash"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Slash used! PP left:", pokemonStats[playerPokemon]["moves"]["slash"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        if pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["dragonClaw"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Dragon Claw used! PP left:", pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"])

                if playerPokemon == "pikachu":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["thunderbolt"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Thunderbolt used! PP left:", pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["quickAttack"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Quick Attack used! PP left:", pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

                if playerPokemon == "gardevoir":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["psychic"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["psychic"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["psychic"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Psychic used! PP left:", pokemonStats[playerPokemon]["moves"]["psychic"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["moonblast"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Moonblast used! PP left:", pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

                if playerPokemon == "celebi":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["psystrike"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Psystrike used! PP left:", pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"])
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["moonblast"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Moonblast used! PP left:", pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])
                
                if playerPokemon == "lucario":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["aurasphere"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Aurasphere used! PP left:", pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"])
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        if pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["dragonPulse"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Dragon Pulse used! PP left:", pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

    if opponentPokemon == "blastoise":
        moveList = ["hydroPump", "bite", "tackle"]
    elif opponentPokemon == "gengar":
        moveList = ["shadowBall", "darkPulse", "tackle"]
    elif opponentPokemon == "mewtwo":
        moveList = ["futureSight", "shadowBall", "tackle"]

    hasPP = False
    for moveName in moveList:
        if opponentStats[opponentPokemon]["moves"][moveName]["pp"] > 0:
            hasPP = True

    if hasPP == True:
        chosenMove = random.choice(moveList)
        while opponentStats[opponentPokemon]["moves"][chosenMove]["pp"] == 0:
            chosenMove = random.choice(moveList)
        move = opponentStats[opponentPokemon]["moves"][chosenMove]

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
            if opponentStats[opponentPokemon]["hp"] < 0:
                opponentStats[opponentPokemon]["hp"] = 0
        attackPos += 1
    else:
        attackPos = 0   
        if turn == "opponent":
            opponentIsAttacking = True
        
    if opponentIsAttacking:
        if opponentAttackPos < 10:
            opponentStats[opponentPokemon]["x"] -= 5
            opponentStats[opponentPokemon]["y"] += 3
        elif opponentAttackPos < 20:    
            opponentStats[opponentPokemon]["x"] += 5
            opponentStats[opponentPokemon]["y"] -= 3
        else:
            opponentStats[opponentPokemon]["x"] = opponentStats[opponentPokemon]["xOG"]
            opponentStats[opponentPokemon]["y"] = opponentStats[opponentPokemon]["yOG"]
            opponentIsAttacking = False
            opponentAttackPos = 0
            if opponentAttacking and hasPP == True:
                pokemonStats[playerPokemon]["hp"] -= move["power"]
                opponentStats[opponentPokemon]["moves"][chosenMove]["pp"] -= 1
                print(chosenMove + " used! PP left:", move["pp"])
            if pokemonStats[playerPokemon]["hp"] < 0:
                pokemonStats[playerPokemon]["hp"] = 0
            turn = "player"
            gamestate = "battleMenu"

        opponentAttackPos += 1

    if opponentStats[opponentPokemon]["hp"] == 0:
        opponentTeamNumber += 1
        if opponentTeamNumber < len(opponentTeam):
            opponentPokemon = opponentTeam[opponentTeamNumber]
            opponentStats[opponentPokemon]["hp"] = opponentStats[opponentPokemon]["maxHP"]
            opponentStats[opponentPokemon]["x"] = opponentStats[opponentPokemon]["xOG"]
            opponentStats[opponentPokemon]["y"] = opponentStats[opponentPokemon]["yOG"]
        else:
            gamestate = "homeMenu"
            
    if pokemonStats[playerPokemon]["hp"] == 0 and not playerPokemonFainted:
        playerPokemonFainted = True
        gamestate = "pokemonMenu"

    if ( pokemonStats["charizard"]["hp"] == 0 and
         pokemonStats["pikachu"]["hp"] == 0 and
         pokemonStats["gardevoir"]["hp"] == 0 and
         pokemonStats["celebi"]["hp"] == 0 and
         pokemonStats["lucario"]["hp"] == 0):
        gamestate = "homeMenu"

    if gamestate == "homeMenu":  
        screen.fill(GRAY)
        screen.blit(mainMenuBg,(285,90))
        homeMenuText = menuFont.render("PYMON", True, 'black')   
        screen.blit(homeMenuText, (400, 375))
    
    if gamestate == "pokemonMenu":
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

        BG = pygame.Surface((1200, 800))
        BG.set_alpha(120)  
        BG.fill("black")
        screen.blit(BG, (0, 0))

        pkMenuBG = pygame.Surface((1200, 350))
        pkMenuBG.set_alpha(240)  
        pkMenuBG.fill(pKMenuColor)
        screen.blit(pkMenuBG, (0, 150))
        screen.blit(pKMenuUI,(-60,175))

        backText = whatWillFont.render("BACK", True, WHITE)
        screen.blit(backText, (1100, 450))

        screen.blit(pickachuMini,(-35,100))
        pickachuNameText = whatWillFont.render("PIKACHU", True, "black")   
        screen.blit(pickachuNameText, (135, 230))

        screen.blit(gardevoirMini,(420,170))
        gardevoirNameText = whatWillFont.render("GARDEVOIR", True, "black")   
        screen.blit(gardevoirNameText, (545, 230))

        screen.blit(celebiMini,(-45,255))
        celebiNameText = whatWillFont.render("CELEBI", True, "black")
        screen.blit(celebiNameText, (135, 385))

        screen.blit(lucarioMini,(430,325))
        lucarioNameText = whatWillFont.render("LUCARIO", True, "black")
        screen.blit(lucarioNameText, (560, 385))

        screen.blit(charizardMini,(855,260))
        charizardNameText = whatWillFont.render("CHARIZARD", True, "black")
        screen.blit(charizardNameText, (970, 315))

        screen.blit(whatWillFont.render(str(pokemonStats["pikachu"]["hp"]) + "/" + str(pokemonStats["pikachu"]["maxHP"]), True, "black"), (145, 285))
        screen.blit(whatWillFont.render(str(pokemonStats["gardevoir"]["hp"]) + "/" + str(pokemonStats["gardevoir"]["maxHP"]), True, "black"), (570, 285))
        screen.blit(whatWillFont.render(str(pokemonStats["celebi"]["hp"]) + "/" + str(pokemonStats["celebi"]["maxHP"]), True, "black"), (145, 440))
        screen.blit(whatWillFont.render(str(pokemonStats["lucario"]["hp"]) + "/" + str(pokemonStats["lucario"]["maxHP"]), True, "black"), (570, 440))
        screen.blit(whatWillFont.render(str(pokemonStats["charizard"]["hp"]) + "/" + str(pokemonStats["charizard"]["maxHP"]), True, "black"), (985, 370))

        if pokemonStats["pikachu"]["hp"] == 0:
            pygame.draw.line(screen, RED, (10, 195), (340, 310), 5)
            pygame.draw.line(screen, RED, (340, 195), (10, 310), 5)
        if pokemonStats["gardevoir"]["hp"] == 0:
            pygame.draw.line(screen, RED, (440, 195), (770, 310), 5)
            pygame.draw.line(screen, RED, (770, 195), (440, 310), 5)
        if pokemonStats["celebi"]["hp"] == 0:
            pygame.draw.line(screen, RED, (10, 350), (340, 465), 5)
            pygame.draw.line(screen, RED, (340, 350), (10, 465), 5)
        if pokemonStats["lucario"]["hp"] == 0:
            pygame.draw.line(screen, RED, (440, 350), (770, 465), 5)
            pygame.draw.line(screen, RED, (770, 350), (440, 465), 5)
        if pokemonStats["charizard"]["hp"] == 0:
            pygame.draw.line(screen, RED, (855, 280), (1180, 395), 5)
            pygame.draw.line(screen, RED, (1180, 280), (855, 395), 5)

        if 1100 <= mouseX <= 1175 and 450 <= mouseY <= 470:
            backText = whatWillFont.render("BACK", True, LIGHTGRAY)
            screen.blit(backText, (1100, 450))
        if 10 <= mouseX <= 340 and 195 <= mouseY <= 310:
           pygame.draw.rect(screen, LIGHTGRAY, (10, 195, 330, 115), 5)
        if 440 <= mouseX <= 770 and 195 <= mouseY <= 310:
           pygame.draw.rect(screen, LIGHTGRAY, (440, 195, 330, 115), 5)
        if 10 <= mouseX <= 340 and 350 <= mouseY <= 470:
           pygame.draw.rect(screen, LIGHTGRAY, (10, 350, 330, 115), 5)
        if 440 <= mouseX <= 770 and 350 <= mouseY <= 470:
           pygame.draw.rect(screen, LIGHTGRAY, (440, 350, 330, 115), 5)
        if 855 <= mouseX <= 1180 and 280 <= mouseY <= 400:
           pygame.draw.rect(screen, LIGHTGRAY, (855, 280, 325, 115), 5)
       
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
                '''slashText = buttonFont.render("RUN", True, WHITE)   
                screen.blit(slashText, (605, 722))'''

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
                    
                '''if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                    slashText = buttonFont.render("RUN", True, LIGHTGRAY)   
                    screen.blit(slashText, (605, 722))'''
            
            if playerPokemon == "pikachu":
                thunderboltText = moveFont.render("THUNDERBOLT", True, WHITE)   
                screen.blit(thunderboltText, (50, 622))
                quickAttackText = moveFont.render("QUICK ATTACK", True, WHITE)   
                screen.blit(quickAttackText, (470, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    thunderboltText = moveFont.render("THUNDERBOLT", True, LIGHTGRAY)   
                    screen.blit(thunderboltText, (50, 622))
                    attackTypeText = attackTypeFont.render("TYPE: ELECTRIC", True, 'yellow')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["thunderbolt"]["maxPP"]), True, 'black')
                    screen.blit(PPText, (975, 685))

                if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    quickAttackText = moveFont.render("QUICK ATTACK", True, LIGHTGRAY)   
                    screen.blit(quickAttackText, (470, 622))
                    attackTypeText = attackTypeFont.render("TYPE: NORMAL", True, 'black')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["quickAttack"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))      

                if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    tackleText = moveFont.render("TACKLE", True, LIGHTGRAY)   
                    screen.blit(tackleText, (120, 722))
                    attackTypeText = attackTypeFont.render("TYPE: NORMAL", True, 'black')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))

            if playerPokemon == "gardevoir":
                psychicText = moveFont.render("PSYCHIC", True, WHITE)   
                screen.blit(psychicText, (115, 622))
                moonblastText = moveFont.render("MOONBLAST", True, WHITE)   
                screen.blit(moonblastText, (520, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    psychicText = moveFont.render("PSYCHIC", True, LIGHTGRAY)   
                    screen.blit(psychicText, (115, 622))
                    attackTypeText = attackTypeFont.render("TYPE: PSYCHIC", True, 'purple')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["psychic"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["psychic"]["maxPP"]), True, 'black')
                    screen.blit(PPText, (975, 685))

                if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    moonblastText = moveFont.render("MOONBLAST", True, LIGHTGRAY)   
                    screen.blit(moonblastText, (520, 622))
                    attackTypeText = attackTypeFont.render("TYPE: FAIRY", True, 'pink')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["moonblast"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))      

                if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    tackleText = moveFont.render("TACKLE", True, LIGHTGRAY)   
                    screen.blit(tackleText, (120, 722))
                    attackTypeText = attackTypeFont.render("TYPE: NORMAL", True, 'black')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))

            if playerPokemon == "celebi":
                psystrikeText = moveFont.render("PSYSTRIKE", True, WHITE)   
                screen.blit(psystrikeText, (80, 622))
                moonblastText = moveFont.render("MOONBLAST", True, WHITE)   
                screen.blit(moonblastText, (520, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    psystrikeText = moveFont.render("PSYSTRIKE", True, LIGHTGRAY)   
                    screen.blit(psystrikeText, (80, 622))
                    attackTypeText = attackTypeFont.render("TYPE: PSYCHIC", True, 'purple')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["psystrike"]["maxPP"]), True, 'black')
                    screen.blit(PPText, (975, 685))

                if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    moonblastText = moveFont.render("MOONBLAST", True, LIGHTGRAY)   
                    screen.blit(moonblastText, (520, 622))
                    attackTypeText = attackTypeFont.render("TYPE: FAIRY", True, 'pink')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["moonblast"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))      

                if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    tackleText = moveFont.render("TACKLE", True, LIGHTGRAY)   
                    screen.blit(tackleText, (120, 722))
                    attackTypeText = attackTypeFont.render("TYPE: NORMAL", True, 'black')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))
            
            if playerPokemon == "lucario":
                aurasphereText = moveFont.render("AURASPHERE", True, WHITE)   
                screen.blit(aurasphereText, (70, 622))
                dragonPulseText = moveFont.render("DRAGON PULSE", True, WHITE)   
                screen.blit(dragonPulseText, (465, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    aurasphereText = moveFont.render("AURASPHERE", True, LIGHTGRAY)   
                    screen.blit(aurasphereText, (70, 622))
                    attackTypeText = attackTypeFont.render("TYPE: FIGHTING", True, 'orange')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["aurasphere"]["maxPP"]), True, 'black')
                    screen.blit(PPText, (975, 685))

                if 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    dragonPulseText = moveFont.render("DRAGON PULSE", True, LIGHTGRAY)   
                    screen.blit(dragonPulseText, (465, 622))
                    attackTypeText = attackTypeFont.render("TYPE: DRAGON", True, 'blue')   
                    screen.blit(attackTypeText, (950, 655))
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["dragonPulse"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))      

                if 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    tackleText = moveFont.render("TACKLE", True, LIGHTGRAY)   
                    screen.blit(tackleText, (120, 722))
                    attackTypeText = attackTypeFont.render("TYPE: NORMAL", True, 'black')   
                    screen.blit(attackTypeText, (950, 655))

        # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()