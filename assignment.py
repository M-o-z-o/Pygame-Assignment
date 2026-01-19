'''
-----------------------------------------------------------------------------
Program Name: Pymon Mewtwo's Reign 
Program Description: Pymon Mewtwo's Reign is a turn-based battle game inspired by the Pokémon
games. The player controls a team of five Pokémon and battles against an
computer controlled team of three Pokémon. Each Pokémon has unique stats, health
points, and a set of moves with limited PP. The player can attack, switch
Pokémon, and use their team to defeat the enemy Pokémon.

-----------------------------------------------------------------------------
References:

(https://www.pygame.org/docs/) 
https://stackoverflow.com/questions/918154/relative-paths-in-python used it for the relative file paths in pygame.

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(random)
(os)
-----------------------------------------------------------------------------

Known bugs: 

(none)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level 4+ because i made a full
turn-based battle system where the opponent is controlled by the computer and
selects moves randomly, and I also met all the minimum requirements of the project.

Level 3 Requirements Met:
The game uses user events (keyboard and/or mouse input from the user)
All user input is sanitized (ie, won't crash your program)
The program must use a variable.
Use appropriate data types (int, String, long).
Use conditional structures (if-statement, boolean operators).
Use loop structures (for, while).
Create and use custom functions.
Encapsulate the final program to include multiple screens with a menu system to move between them. (For example: an intro screen, main screen, and end screen).
The program should have clear instructions on how to use/play.
The program must have a soundtrack and sounds.
The program uses images
Coding decisions should make sense and not include grossly inefficient code.
The program must have collision detection
The program must have a custom downloaded font

Code Organization (level 3)
Your code should follow internal documentation standards: 
Program and methods should have headers.
Do not put your name in the header!
Summary
Description
Parameter list
Returns
Warning
Raises/Exceptions
Frequent comments to help future readers understand code.
Proper Indentation
Use names that are descriptive and make sense when making variables, lists, methods etc….
Names are as short as possible without losing descriptive meaning..
Names use proper naming conventions such as CamelCase for Java or snake_case for Python and capitalized Object names etc…


Features Added Beyond Level 3 Requirements:
Random computer picked attacks for turn based combat.
-----------------------------------------------------------------------------
'''

#Links needed for sprites
#https://pokemondb.net/move/generation/5
#https://pokemondb.net/sprites

# Libraries 
import pygame
import random
import os

dir = os.path.dirname(os.path.abspath(__file__))    

# Sprites
charizard = pygame.image.load(os.path.join(dir,"charizard.png"))
charizardMini = pygame.image.load(os.path.join(dir,"charizard mini.png"))
pikachu = pygame.image.load(os.path.join(dir,"pikachu.png"))
pickachuMini = pygame.image.load(os.path.join(dir,"pikachu mini.png"))
gardevoir = pygame.image.load(os.path.join(dir,"gardevoir.png"))
gardevoirMini = pygame.image.load(os.path.join(dir,"gardevoir mini.png"))
celebi = pygame.image.load(os.path.join(dir,"celebi.png"))
celebiMini = pygame.image.load(os.path.join(dir,"celebi mini.png"))
lucario = pygame.image.load(os.path.join(dir,"lucario.png"))
lucarioMini = pygame.image.load(os.path.join(dir,"lucario mini.png"))

opponentBlastoise = pygame.image.load(os.path.join(dir,"blastoise.png"))
opponentGengar = pygame.image.load(os.path.join(dir,"gengar.png"))
opponentMewtwo = pygame.image.load(os.path.join(dir,"mewtwo.png"))

# UI
mainMenuBg = pygame.image.load(os.path.join(dir,"pokeball bg.webp"))
mainMenuBg = pygame.image.load(os.path.join(dir,"mewtwos reign bg.jpg"))
battleBg = pygame.image.load(os.path.join(dir,"battlebggold (1).png"))
aiGround = pygame.image.load(os.path.join(dir,"aiground (1).png"))
playerGround = pygame.image.load(os.path.join(dir,"playerground.png"))
fightUI = pygame.image.load(os.path.join(dir,"battleUI.png"))
fightUI2 = pygame.image.load(os.path.join(dir,"pixil-frame-0 (1).png"))
pKMenuUI = pygame.image.load(os.path.join(dir,"pixil-frame-0 (5).png"))
opponentHealthBar = pygame.image.load(os.path.join(dir,"pixil-frame-0 (8).png"))
playerHealthBar = pygame.image.load(os.path.join(dir,"pixil-frame-0 (10).png"))

# Colours
RED = (239, 57, 56)
ORANGE = (232, 155, 39)
BLUE = (42, 148, 206)
GREEN = (90, 181, 41)
BEIGE = (239, 255, 216)
GRAY = (49, 49, 49)
LIGHTGRAY = (184, 184, 184)
WHITE = (248, 248, 248)
SKYBLUE = (74,107,138)

# Nested dictionaries for player pokenmon 
pokemonStats = {
    # Stores image for charizard spirte, postion, HP, moves, PP, and damage
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
    # Stores image for pikachu spirte, postion, HP, moves, PP, and damage
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
    # Stores image for gardevoir spirte, postion, HP, moves, PP, and damage
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
    # Stores image for celebi spirte, postion, HP, moves, PP, and damage
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
    # Stores image for lucario spirte, postion, HP, moves, PP, and damage
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

# Nested dictionaries for opponent pokemon
opponentStats = {   
    # Stores image for blastoise spirte, postion, HP, moves, PP, and damage
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
    # Stores image for gengar spirte, postion, HP, moves, PP, and damage
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
    # Stores image for mewtwo spirte, postion, HP, moves, PP, and damage
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

# Variables
gamestate = "homeMenu"
# list for the player team
playerTeam = ["pikachu", "gardevoir", "celebi", "lucario", "charizard"]
# varbiable for index so I able to go through the opponent team
playerTeamNumber = 0
playerPokemon = playerTeam[4]
# list for the opponent team
opponentTeam = ["blastoise", "gengar", "mewtwo"]
# varbiable for index so I able to go through the opponent team
opponentTeamNumber = 0
opponentPokemon = opponentTeam[opponentTeamNumber]
turn = "player"
isAttacking = False
opponentAttacking = False
opponentIsAttacking = False
playerPokemonFainted = False
currentMusic = False
opponentAttackPos = 0
attackPos = 0
pKMenuColor = (113,154,154)
playerHP = pokemonStats[playerPokemon]["hp"]
playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
opponentHP = opponentStats[opponentPokemon]["hp"]
opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]

# pygame setup
pygame.init()
pygame.mixer.init()

# Sounds Effects and Music
# Main menu theme
mainMenuMusic = pygame.mixer.Sound(os.path.join(dir,"_Mewtwos Theme_ - Pokmon Suite.mp3"))
mainMenuMusic.set_volume(0.3)
# Battle theme against blastoise and gengar
battleMusic = pygame.mixer.Sound(os.path.join(dir,"Pokmon Sun  Moon - Battle Legend Red  Blue Battle Music HQ.mp3"))
battleMusic.set_volume(0.3)
# Mewtwo boss theme
mewtwoBattleMusic = pygame.mixer.Sound(os.path.join(dir,"Pokmon The Origins Recreation - Mewtwo Battle HQ.mp3"))
mewtwoBattleMusic.set_volume(0.3)
# Button sound effect
buttonClickedSound = pygame.mixer.Sound(os.path.join(dir,"Pokemon A Button - Sound Effect HD.mp3"))
buttonClickedSound.set_volume(0.5)

# Fonts
menuFont = pygame.font.Font(os.path.join(dir,"PokemonGb-RAeo.ttf"), 65)
buttonFont = pygame.font.Font(os.path.join(dir,"PokemonGb-RAeo.ttf"), 50)
pokemonNameFont = pygame.font.Font(os.path.join(dir,"PokemonGb-RAeo.ttf"), 30)
moveFont = pygame.font.Font(os.path.join(dir,"PokemonGb-RAeo.ttf"), 35)
whatWillFont = pygame.font.Font(os.path.join(dir,"PokemonGb-RAeo.ttf"), 20)
attackTypeFont = pygame.font.Font(os.path.join(dir,"PokemonGb-RAeo.ttf"), 15)

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

# Displays the main battle screen
def drawBattleScreen():
        playerHP = pokemonStats[playerPokemon]["hp"]
        playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
        opponentHP = opponentStats[opponentPokemon]["hp"]
        opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]
        screen.blit(battleBg,(0,0))
        screen.blit(aiGround,(690,280))
        screen.blit(playerGround,(50,500))
        screen.blit(pokemonStats[playerPokemon]["pokemon"],(pokemonStats[playerPokemon]["x"],pokemonStats[playerPokemon]["y"]))
        screen.blit(opponentStats[opponentPokemon]["pokemon"],(opponentStats[opponentPokemon]["x"],opponentStats[opponentPokemon]["y"]))
        screen.blit(fightUI,(0,575))
        screen.blit(playerHealthBar, (700, 360))
        screen.blit(opponentHealthBar, (-68, -25))
        pygame.draw.rect(screen, RED, (982, 493, 192, 12))
        pygame.draw.rect(screen, GREEN, (982, 493, 192 * (playerHP / playerMaxHP), 12))
        pygame.draw.rect(screen, RED, (203, 136, 192, 12))
        pygame.draw.rect(screen, GREEN, (203, 136, 192 * (opponentHP / opponentMaxHP), 12))

while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #print(mouseX, mouseY)

        # Checking if left mouse button is down
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Resetting game after win or lose
            if gamestate == "winMenu" or gamestate == "loseMenu":
                if 360 <= mouseX <= 865 and 500 <= mouseY <= 585:
                    buttonClickedSound.play()
                    gamestate = "homeMenu"
                    # resets every pokemons moves back to max PP
                    for move in pokemonStats["charizard"]["moves"]:
                        pokemonStats["charizard"]["moves"][move]["pp"] = pokemonStats["charizard"]["moves"][move]["maxPP"]
                    for move in pokemonStats["pikachu"]["moves"]:
                        pokemonStats["pikachu"]["moves"][move]["pp"] = pokemonStats["pikachu"]["moves"][move]["maxPP"]
                    for move in pokemonStats["gardevoir"]["moves"]:
                        pokemonStats["gardevoir"]["moves"][move]["pp"] = pokemonStats["gardevoir"]["moves"][move]["maxPP"]
                    for move in pokemonStats["celebi"]["moves"]:
                        pokemonStats["celebi"]["moves"][move]["pp"] = pokemonStats["celebi"]["moves"][move]["maxPP"]
                    for move in pokemonStats["lucario"]["moves"]:
                        pokemonStats["lucario"]["moves"][move]["pp"] = pokemonStats["lucario"]["moves"][move]["maxPP"]
                    for move in opponentStats["blastoise"]["moves"]:
                        opponentStats["blastoise"]["moves"][move]["pp"] = opponentStats["blastoise"]["moves"][move]["maxPP"]
                    for move in opponentStats["gengar"]["moves"]:
                        opponentStats["gengar"]["moves"][move]["pp"] = opponentStats["gengar"]["moves"][move]["maxPP"]
                    for move in opponentStats["mewtwo"]["moves"]:
                        opponentStats["mewtwo"]["moves"][move]["pp"] = opponentStats["mewtwo"]["moves"][move]["maxPP"]

                    # Resets every pokemons HP back to max HP
                    pokemonStats["charizard"]["hp"] = pokemonStats["charizard"]["maxHP"]    
                    pokemonStats["pikachu"]["hp"] = pokemonStats["pikachu"]["maxHP"]
                    pokemonStats["gardevoir"]["hp"] = pokemonStats["gardevoir"]["maxHP"]
                    pokemonStats["celebi"]["hp"] = pokemonStats["celebi"]["maxHP"]
                    pokemonStats["lucario"]["hp"] = pokemonStats["lucario"]["maxHP"]
                    opponentStats["blastoise"]["hp"] = opponentStats["blastoise"]["maxHP"]
                    opponentStats["gengar"]["hp"] = opponentStats["gengar"]["maxHP"]
                    opponentStats["mewtwo"]["hp"] = opponentStats["mewtwo"]["maxHP"]
                    
                    # Resets variables
                    playerTeamNumber = 0
                    playerPokemon = playerTeam[playerTeamNumber]
                    opponentTeamNumber = 0
                    opponentPokemon = opponentTeam[opponentTeamNumber]
                    turn = "player"
                    isAttacking = False
                    opponentAttacking = False
                    opponentIsAttacking = False
                    playerPokemonFainted = False
                    currentMusic = False
            
            # Changing gamestates depending on when/where button is clicked and playing a click sound
            # If in the home menu the user will have the option to click on the 
            # how to play button or the start/ battle button.
            elif gamestate == "homeMenu":  
                if 310 <= mouseX <= 915 and 375 <= mouseY <= 460:
                    buttonClickedSound.play()
                    gamestate = "battleMenu"
                if 310 <= mouseX <= 915 and 505 <= mouseY <= 590:
                    buttonClickedSound.play()
                    gamestate = "howToMenu"

            # If the user wants to exit the how to play menu they will
            # be able to click on the back button to go back to the home menu
            elif gamestate == "howToMenu":
                if 955 <= mouseX <= 1195 and 735 <= mouseY <= 795:
                    buttonClickedSound.play()
                    gamestate = "homeMenu"

            # If the user is in the battle menu they will have 4 choices,
            # either change pokemon, fight, back, or run
            elif gamestate == "battleMenu":
                if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                    buttonClickedSound.play()
                    gamestate = "fightMenu"
                elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                    buttonClickedSound.play()
                    gamestate = "homeMenu"
                elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                    buttonClickedSound.play()
                    gamestate = "pokemonMenu"
                elif 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                    buttonClickedSound.play()
                    gamestate = "homeMenu"

            # Changing the players pokemon by going through a list 
            # depending on the button clicked 
            elif gamestate == "pokemonMenu":
                if 10 <= mouseX <= 340 and 195 <= mouseY <= 310 and pokemonStats[playerTeam[0]]["hp"] > 0:
                    buttonClickedSound.play()
                    playerPokemon = playerTeam[0]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 440 <= mouseX <= 770 and 195 <= mouseY <= 310 and pokemonStats[playerTeam[1]]["hp"] > 0:
                    buttonClickedSound.play()
                    playerPokemon = playerTeam[1]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 10 <= mouseX <= 340 and 350 <= mouseY <= 470 and pokemonStats[playerTeam[2]]["hp"] > 0:
                    buttonClickedSound.play()
                    playerPokemon = playerTeam[2]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 440 <= mouseX <= 770 and 350 <= mouseY <= 470 and pokemonStats[playerTeam[3]]["hp"] > 0:
                    buttonClickedSound.play()
                    playerPokemon = playerTeam[3]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 855 <= mouseX <= 1180 and 280 <= mouseY <= 400 and pokemonStats[playerTeam[4]]["hp"] > 0:
                    buttonClickedSound.play()
                    playerPokemon = playerTeam[4]
                    playerPokemonFainted = False
                    gamestate = "battleMenu"
                elif 1100 <= mouseX <= 1175 and 450 <= mouseY <= 470 and not playerPokemonFainted:
                    buttonClickedSound.play()
                    gamestate = "battleMenu"

            # Switching back to the battle menu after animations
            elif gamestate == "fightMenu" and turn == "player" and not isAttacking:
                if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                    buttonClickedSound.play()
                    gamestate = "battleMenu"

                # Removes one PP from the players pokemon after a move is used 
                # And removes HP from the oppononet pokemon
                if playerPokemon == "charizard":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["fireBlast"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Fire Blast used! PP left:", pokemonStats[playerPokemon]["moves"]["fireBlast"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["slash"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["slash"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["slash"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Slash used! PP left:", pokemonStats[playerPokemon]["moves"]["slash"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["dragonClaw"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Dragon Claw used! PP left:", pokemonStats[playerPokemon]["moves"]["dragonClaw"]["pp"])

                # Removes one PP from the players pokemon after a move is used 
                # And removes HP from the oppononet pokemon
                if playerPokemon == "pikachu":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["thunderbolt"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Thunderbolt used! PP left:", pokemonStats[playerPokemon]["moves"]["thunderbolt"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["quickAttack"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Quick Attack used! PP left:", pokemonStats[playerPokemon]["moves"]["quickAttack"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

                # Removes one PP from the players pokemon after a move is used 
                # And removes HP from the oppononet pokemon
                if playerPokemon == "gardevoir":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["psychic"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["psychic"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["psychic"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Psychic used! PP left:", pokemonStats[playerPokemon]["moves"]["psychic"]["pp"])                    
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["moonblast"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Moonblast used! PP left:", pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

                # Removes one PP from the players pokemon after a move is used 
                # And removes HP from the oppononet pokemon
                if playerPokemon == "celebi":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["psystrike"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Psystrike used! PP left:", pokemonStats[playerPokemon]["moves"]["psystrike"]["pp"])
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["moonblast"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Moonblast used! PP left:", pokemonStats[playerPokemon]["moves"]["moonblast"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

                # Removes one PP from the players pokemon after a move is used 
                # And removes HP from the oppononet pokemon
                if playerPokemon == "lucario":
                    if 15 <= mouseX <= 450 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["aurasphere"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Aurasphere used! PP left:", pokemonStats[playerPokemon]["moves"]["aurasphere"]["pp"])
                    elif 460 <= mouseX <= 890 and 592 <= mouseY <= 692:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["dragonPulse"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Dragon Pulse used! PP left:", pokemonStats[playerPokemon]["moves"]["dragonPulse"]["pp"])
                    elif 15 <= mouseX <= 450 and 702 <= mouseY <= 787:
                        buttonClickedSound.play()
                        if pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] > 0:
                            pokemonStats[playerPokemon]["moves"]["tackle"]["pp"] -= 1
                            opponentStats[opponentPokemon]["hp"] -= pokemonStats[playerPokemon]["moves"]["tackle"]["power"]
                            isAttacking = True
                            opponentAttacking = True
                            turn = "opponent"
                            print("Tackle used! PP left:", pokemonStats[playerPokemon]["moves"]["tackle"]["pp"])

    # Animation for the player pokemon
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
        # After the animation is done it will start the opponrnet attacking
        attackPos = 0   
        if turn == "opponent":
            opponentIsAttacking = True

    # List for opponnet pokemon moves
    if opponentPokemon == "blastoise":
        moveList = ["hydroPump", "bite", "tackle"]
    elif opponentPokemon == "gengar":
        moveList = ["shadowBall", "darkPulse", "tackle"]
    elif opponentPokemon == "mewtwo":
        moveList = ["futureSight", "shadowBall", "tackle"]

    # Checks if opponnet pokemon has any moves with PP
    hasPP = False
    for moveName in moveList:
        if opponentStats[opponentPokemon]["moves"][moveName]["pp"] > 0:
            hasPP = True

    # If opponnet pokemon has a move with PP it will choose a random one from the list
    if hasPP == True:
        chosenMove = random.choice(moveList)
        while opponentStats[opponentPokemon]["moves"][chosenMove]["pp"] == 0:
            chosenMove = random.choice(moveList)
        move = opponentStats[opponentPokemon]["moves"][chosenMove]

    # Animations for the opponent pokemon
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
            # Removes HP from player pokemon and removes PP from opponent pokemon
            if opponentAttacking and hasPP == True:
                pokemonStats[playerPokemon]["hp"] -= move["power"]
                opponentStats[opponentPokemon]["moves"][chosenMove]["pp"] -= 1
                print(chosenMove + " used! PP left:", move["pp"])
            if pokemonStats[playerPokemon]["hp"] < 0:
                pokemonStats[playerPokemon]["hp"] = 0
            turn = "player"
            gamestate = "battleMenu"

        opponentAttackPos += 1

    # If an opponent pokemon dies it will switch to the next one in the team
    if opponentStats[opponentPokemon]["hp"] == 0:
        opponentTeamNumber += 1
        # Checks if the index number of the team is less than the length 
        # if it is, it will switch to the next in the team, else you win
        if opponentTeamNumber < len(opponentTeam):
            opponentPokemon = opponentTeam[opponentTeamNumber]
            opponentStats[opponentPokemon]["hp"] = opponentStats[opponentPokemon]["maxHP"]
            opponentStats[opponentPokemon]["x"] = opponentStats[opponentPokemon]["xOG"]
            opponentStats[opponentPokemon]["y"] = opponentStats[opponentPokemon]["yOG"]
        else:
            gamestate = "winMenu"

    # If player pokemon HP is 0 than it will send you to the pokemon menu 
    # too pick your next one
    if pokemonStats[playerPokemon]["hp"] == 0 and not playerPokemonFainted:
        playerPokemonFainted = True
        gamestate = "pokemonMenu"

    # If all of the players pokemon are fainted then you are sent to the lose menu
    if ( pokemonStats["charizard"]["hp"] == 0 and
         pokemonStats["pikachu"]["hp"] == 0 and
         pokemonStats["gardevoir"]["hp"] == 0 and
         pokemonStats["celebi"]["hp"] == 0 and
         pokemonStats["lucario"]["hp"] == 0):
        gamestate = "loseMenu"

    # win menu with the text, buttons, and hover effect of the buttons
    if gamestate == "winMenu":
        pygame.mixer.music.stop()
        screen.fill(BEIGE)
        winText = menuFont.render("YOU WIN!", True, 'green')   
        screen.blit(winText, (350, 375))
        pygame.draw.rect(screen, LIGHTGRAY, (355, 500, 510, 85))
        playAgainText = buttonFont.render("PLAY AGAIN", True, 'black')
        screen.blit(playAgainText, (365, 525))

        if 355 <= mouseX <= 865 and 500 <= mouseY <= 585:
            pygame.draw.rect(screen, 'darkgray', (355, 500, 510, 85))
            playAgainText = buttonFont.render("PLAY AGAIN", True, 'black')
            screen.blit(playAgainText, (365, 525))

    # Lose menu with the text, buttons, and hover effect of the buttons
    if gamestate == "loseMenu":
        pygame.mixer.music.stop()
        screen.fill(BEIGE)
        loseText = menuFont.render("YOU LOSE!", True, 'red')   
        screen.blit(loseText, (320, 375))
        pygame.draw.rect(screen, LIGHTGRAY, (360, 500, 505, 85))
        playAgainText = buttonFont.render("PLAY AGAIN", True, 'black')
        screen.blit(playAgainText, (365, 525))

        if 360 <= mouseX <= 865 and 500 <= mouseY <= 585:
            pygame.draw.rect(screen, 'darkgray', (360, 500, 505, 85))
            playAgainText = buttonFont.render("PLAY AGAIN", True, 'black')
            screen.blit(playAgainText, (365, 525))

    # Home menu with the text, buttons, and hover effect of the buttons
    if gamestate == "homeMenu":  
        screen.fill('black')
        screen.blit(mainMenuBg,(0,20))
        homeMenuText = menuFont.render("PYMON", True, 'black')       
        screen.blit(homeMenuText, (445, 45))
        titleText = buttonFont.render("MewTwo's", True, 'purple')   
        screen.blit(titleText, (260, 135))
        titleText2 = buttonFont.render("Reign", True, 'white')
        screen.blit(titleText2, (700, 135))
        pygame.draw.rect(screen, 'black', (305, 370, 615, 95))
        pygame.draw.rect(screen, SKYBLUE, (310, 375, 605, 85))
        pygame.draw.rect(screen, 'black', (305, 500, 615, 95))
        pygame.draw.rect(screen, SKYBLUE, (310, 505, 605, 85))
        startText = buttonFont.render("START BATTLE", True, 'black')
        screen.blit(startText, (315, 395))
        howToText = buttonFont.render("HOW TO PLAY!", True, 'black')
        screen.blit(howToText, (315, 525))
        
        # Hover effect for start button
        if mouseX >= 310 and mouseX <= 915 and mouseY >= 375 and mouseY <= 460:
            pygame.draw.rect(screen, 'black', (305, 370, 615, 95))
            pygame.draw.rect(screen, 'lightblue', (310, 375, 605, 85))
            startText = buttonFont.render("START BATTLE", True, 'black')
            screen.blit(startText, (315, 395))

        # Hover effect for how to play button
        if mouseX >= 310 and mouseX <= 915 and mouseY >= 505 and mouseY <= 590:
            pygame.draw.rect(screen, 'black', (305, 500, 615, 95))
            pygame.draw.rect(screen, 'lightblue', (310, 505, 605, 85))
            howToText = buttonFont.render("HOW TO PLAY!", True, 'black')
            screen.blit(howToText, (315, 525))

    # How to play menu with the text, buttons, and hover effect of the buttons
    if gamestate == "howToMenu":
        screen.fill('black')
        screen.blit(mainMenuBg,(0,20))
        homeMenuText = menuFont.render("HOW TO PLAY", True, "black")   
        pygame.draw.rect(screen, 'white', (0, 145, 1200, 600))  
        screen.blit(homeMenuText, (250, 50))
        titleText = attackTypeFont.render("THIS GAME IS A TURN BASED FIGHTING GAME (INSPIRED BY POKEMON)", True, 'black')   
        screen.blit(titleText, (45, 175))
        titleText = attackTypeFont.render("YOU WILL GO AGAINST A TEAM OF 3 POKEMON EACH ONE VARYING IN STATS", True, 'black')   
        screen.blit(titleText, (45, 275))
        titleText = attackTypeFont.render("YOU WILL HAVE A TEAM OF POKEMON THAT YOU CAN SWITCH THROUGH", True, 'black')   
        screen.blit(titleText, (45, 375))
        titleText = attackTypeFont.render("EACH OF YOUR POKEMON HAS DIFFERENT ATTACKS THEY CAN USE", True, 'black')   
        screen.blit(titleText, (45, 475))
        titleText = attackTypeFont.render("YOU CAN ONLY USE EACH ATTACK A CERTAIN AMOUNT OF TIMES", True, 'black')   
        screen.blit(titleText, (45, 575))
        titleText = attackTypeFont.render("IF THE POKEMON YOU ARE USING FAINTS, THEN YOU WILL BE FORECD TO CHANGE", True, 'black')   
        screen.blit(titleText, (45, 675))

        pygame.draw.rect(screen, 'black', (950, 730, 250, 70))
        pygame.draw.rect(screen, SKYBLUE, (955, 735, 240, 60))
        backText = pokemonNameFont.render("BACK", True, 'black')
        screen.blit(backText, (1020, 752))

        # Hover effect for back button
        if mouseX >= 955 and mouseX <= 1195 and mouseY >= 735 and mouseY <= 795:
            pygame.draw.rect(screen, 'black', (950, 730, 250, 70))
            pygame.draw.rect(screen, "lightblue", (955, 735, 240, 60))
            backText = pokemonNameFont.render("BACK", True, 'black')
            screen.blit(backText, (1020, 752))

    # Pokemon menu with the text, buttons, and hover effect of the buttons
    if gamestate == "pokemonMenu":
        playerHP = pokemonStats[playerPokemon]["hp"]
        playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
        opponentHP = opponentStats[opponentPokemon]["hp"]
        opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]
        drawBattleScreen()
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

        pokemonNameText = pokemonNameFont.render(playerPokemon.upper(), True, 'black')   
        screen.blit(pokemonNameText, (795, 445))
        pokemonHealthText = whatWillFont.render(str(playerHP) + "/" + str(playerMaxHP), True, 'black')
        screen.blit(pokemonHealthText, (1010, 527))
        opponentNameText = pokemonNameFont.render(opponentPokemon.upper(), True, 'black')   
        screen.blit(opponentNameText, (30, 85))
        
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

        # Mini icon for pikachu in the pokemon menu
        screen.blit(pickachuMini,(-35,100))
        pickachuNameText = whatWillFont.render("PIKACHU", True, "black")   
        screen.blit(pickachuNameText, (135, 230))

        # Mini icon for gardevoir in the pokemon menu
        screen.blit(gardevoirMini,(420,170))
        gardevoirNameText = whatWillFont.render("GARDEVOIR", True, "black")   
        screen.blit(gardevoirNameText, (545, 230))

        # Mini icon for celeb in the pokemon menu
        screen.blit(celebiMini,(-45,255))
        celebiNameText = whatWillFont.render("CELEBI", True, "black")
        screen.blit(celebiNameText, (135, 385))

        # Mini icon for lucario in the pokemon menu
        screen.blit(lucarioMini,(430,325))
        lucarioNameText = whatWillFont.render("LUCARIO", True, "black")
        screen.blit(lucarioNameText, (560, 385))

        # Mini icon for charizard in the pokemon menu
        screen.blit(charizardMini,(855,260))
        charizardNameText = whatWillFont.render("CHARIZARD", True, "black")
        screen.blit(charizardNameText, (970, 315))

        # Displays HP for your pokemon
        screen.blit(whatWillFont.render(str(pokemonStats["pikachu"]["hp"]) + "/" + str(pokemonStats["pikachu"]["maxHP"]), True, "black"), (145, 285))
        screen.blit(whatWillFont.render(str(pokemonStats["gardevoir"]["hp"]) + "/" + str(pokemonStats["gardevoir"]["maxHP"]), True, "black"), (570, 285))
        screen.blit(whatWillFont.render(str(pokemonStats["celebi"]["hp"]) + "/" + str(pokemonStats["celebi"]["maxHP"]), True, "black"), (145, 440))
        screen.blit(whatWillFont.render(str(pokemonStats["lucario"]["hp"]) + "/" + str(pokemonStats["lucario"]["maxHP"]), True, "black"), (570, 440))
        screen.blit(whatWillFont.render(str(pokemonStats["charizard"]["hp"]) + "/" + str(pokemonStats["charizard"]["maxHP"]), True, "black"), (985, 370))

        # Displays a red X on the pokemon if it is fainted
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

        # Hover effect for the back button and the buttons for the 
        # pokemon in the pokemon menu 
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

    # Battle menu with the text, buttons, and hover effect of the buttons
    if gamestate == "battleMenu":
        playerHP = pokemonStats[playerPokemon]["hp"]
        playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
        opponentHP = opponentStats[opponentPokemon]["hp"]
        opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]
        drawBattleScreen()
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
        pokemonNameText = pokemonNameFont.render(playerPokemon.upper(), True, 'black')   
        screen.blit(pokemonNameText, (795, 445))
        pokemonHealthText = whatWillFont.render(str(playerHP) + "/" + str(playerMaxHP), True, 'black')
        screen.blit(pokemonHealthText, (1010, 527))
        opponentNameText = pokemonNameFont.render(opponentPokemon.upper(), True, 'black')   
        screen.blit(opponentNameText, (30, 85))

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

    # Fight menu with the text, buttons, and hover effect of the buttons
    if gamestate == "fightMenu":
            playerHP = pokemonStats[playerPokemon]["hp"]
            playerMaxHP = pokemonStats[playerPokemon]["maxHP"]
            opponentHP = opponentStats[opponentPokemon]["hp"]
            opponentMaxHP = opponentStats[opponentPokemon]["maxHP"]
            drawBattleScreen()
            screen.blit(fightUI,(0,575))
            pokemonNameText = pokemonNameFont.render(playerPokemon.upper(), True, 'black')   
            screen.blit(pokemonNameText, (795, 445))
            pokemonHealthText = whatWillFont.render(str(playerHP) + "/" + str(playerMaxHP), True, 'black')
            screen.blit(pokemonHealthText, (1010, 527))
            opponentNameText = pokemonNameFont.render(opponentPokemon.upper(), True, 'black')   
            screen.blit(opponentNameText, (30, 85))
            backText = buttonFont.render("BACK", True, WHITE)   
            screen.blit(backText, (585, 722))

            if 460 <= mouseX <= 890 and 702 <= mouseY <= 787:
                backText = buttonFont.render("BACK", True, LIGHTGRAY)   
                screen.blit(backText, (585, 722))

            # Displays the differnet attacks of the pokenmon
            if playerPokemon == "charizard":
                fireBlastText = moveFont.render("FIRE BLAST", True, WHITE)   
                screen.blit(fireBlastText, (70, 622))
                backText = moveFont.render("SLASH", True, WHITE)   
                screen.blit(backText, (590, 622))
                dragonClawText = moveFont.render("DRAGON CLAW", True, WHITE)   
                screen.blit(dragonClawText, (45, 722))

                # If player curosr is hovering over a move it will display its 
                # attack type and the amount of PP it has/left
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

            # Displays the differnet attacks of the pokenmon
            if playerPokemon == "pikachu":
                thunderboltText = moveFont.render("THUNDERBOLT", True, WHITE)   
                screen.blit(thunderboltText, (50, 622))
                quickAttackText = moveFont.render("QUICK ATTACK", True, WHITE)   
                screen.blit(quickAttackText, (470, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                # If player curosr is hovering over a move it will display its 
                # attacck type and the amount of PP it has/left
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

            # Displays the differnet attacks of the pokenmon
            if playerPokemon == "gardevoir":
                psychicText = moveFont.render("PSYCHIC", True, WHITE)   
                screen.blit(psychicText, (115, 622))
                moonblastText = moveFont.render("MOONBLAST", True, WHITE)   
                screen.blit(moonblastText, (520, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                # If player curosr is hovering over a move it will display its 
                # attacck type and the amount of PP it has/left
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

            # Displays the differnet attacks of the pokenmon
            if playerPokemon == "celebi":
                psystrikeText = moveFont.render("PSYSTRIKE", True, WHITE)   
                screen.blit(psystrikeText, (80, 622))
                moonblastText = moveFont.render("MOONBLAST", True, WHITE)   
                screen.blit(moonblastText, (520, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                # If player curosr is hovering over a move it will display its 
                # attacck type and the amount of PP it has/left
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

            # Displays the differnet attacks of the pokenmon
            if playerPokemon == "lucario":
                aurasphereText = moveFont.render("AURASPHERE", True, WHITE)   
                screen.blit(aurasphereText, (70, 622))
                dragonPulseText = moveFont.render("DRAGON PULSE", True, WHITE)   
                screen.blit(dragonPulseText, (465, 622))
                tackleText = moveFont.render("TACKLE", True, WHITE)   
                screen.blit(tackleText, (120, 722))

                # If player curosr is hovering over a move it will display its 
                # attacck type and the amount of PP it has/left
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
                    PPText = attackTypeFont.render("PP:" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["pp"]) + "/" + str(pokemonStats[playerPokemon]["moves"]["tackle"]["maxPP"]), True, 'black')   
                    screen.blit(PPText, (975, 685))
        
    # If in home menu it will play the menu music
    if gamestate == "homeMenu" and currentMusic != "menu":
        battleMusic.stop()
        mewtwoBattleMusic.stop()
        mainMenuMusic.play(-1)  
        currentMusic = "menu"
    
     # If in battle menu and the opponent pokemon is Mewtwo it will play the mewtwo music
    if gamestate == "battleMenu" and opponentPokemon == "mewtwo" and currentMusic != "mewtwoBattle":
        battleMusic.stop()
        mainMenuMusic.stop()
        mewtwoBattleMusic.play(-1)
        currentMusic = "mewtwoBattle"

    # If in battle menu and the opponent pokemin is not Mewtwo it will play the battle music
    if gamestate == "battleMenu" and currentMusic != "battle" and opponentPokemon != "mewtwo":
        mainMenuMusic.stop()
        mewtwoBattleMusic.stop()
        battleMusic.play(-1)
        currentMusic = "battle"

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
    pygame.quit