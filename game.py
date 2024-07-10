import os
import math
import time
import msvcrt

import codes
import character
import grid
import menu

def cls():
    os.system("cls")
    
def printl(arg):
    print(arg, end = "")

def printg(arg):
    grid.Write(arg)

def LoadAscii(id):
    tags = ["<fBlk>", "<fR>", "<fG>", "<fY>", "<fB>", "<fP>", "<fW>",
        "<fLBlk>", "<fLR>", "<fLG>", "<fLY>", "<fLB>", "<fLP>", "<fLW>",
        "<bR>", "<bG>", "<bY>", "<bB>", "<bP>", "<bW>",
        "<bLBlk>", "<bLR>", "<bLG>", "<bLY>", "<bLB>", "<bLP>", "<bLW>",
        "<re>"]

    escape = [codes.fgBlack, codes.fgRed, codes.fgGreen, codes.fgYellow, codes.fgBlue, codes.fgPurple, codes.fgWhite,
        codes.fgGray, codes.fgLightRed, codes.fgLightGreen, codes.fgLightYellow, codes.fgLightBlue, codes.fgLightPurple, codes.fgLightWhite,
        codes.bgRed, codes.bgGreen, codes.bgYellow, codes.bgBlue, codes.bgPurple, codes.bgWhite,
        codes.bgGray, codes.bgLightRed, codes.bgLightGreen, codes.bgLightYellow, codes.bgLightBlue, codes.bgLightPurple, codes.bgLightWhite,
        codes.reset]

    file = open(__file__ + "\\..\\ascii_" + id)

    content = file.readlines()

    file.close()

    lineCount = 0

    for line in content:
        for i in range(0, len(tags)):
            if tags[i] in line:
                content[lineCount] = content[lineCount].replace(tags[i], escape[i])

        lineCount += 1

    return content
    
def PrintBar(label, current, max, style):
    if style == 0:
        barLength = 28

    elif style == 1 or style == 2:
        barLength = 18

        label = str(current) + "/" + str(max)

    barSplitIndex = int(math.ceil(barLength * (current / max)))

    labelPosition = int(math.ceil(barLength / (len(label) / 2)))

    labelIndex = 0

    if style == 0:
        printl(codes.fgLightWhite + codes.bgLightGreen)
        
    elif style == 1:
        printg(codes.fgLightWhite + codes.bgBlue)

    for i in range(0, barLength):
        if i == barSplitIndex:
            if style == 0:
                printl(codes.bgGreen)
            
            elif style == 1:
                printg(codes.bgLightBlue)

            elif style == 2:
                printg(codes.fgGray)
            
        if i < labelPosition or i > (labelPosition + len(label) - 1):
            if style == 0:
                printl(" ")
    
            elif style == 1:
                printg(" ")

            elif style == 2:
                printg(chr(22))
            
        elif style == 0 or style == 1:
            if style == 0:
                printl(label[labelIndex])

            elif style == 1:
                printg(label[labelIndex])
            labelIndex += 1

        elif style == 2:
                printg(chr(22))
            
    if style == 0:
        printl(codes.reset)

    else:
        printg(codes.reset)

def PrintStats():
    margin = "     "

    blankLine = "                              \n"

    printg(margin + codes.fgGray + "Level: " + codes.fgLightWhite + "1                 \n")

    printg(blankLine)

    printg(margin + codes.fgGray + "Exp: " + codes.fgLightWhite + "112/200             \n")

    printg(blankLine)
    printg(blankLine)
    printg(blankLine)
    printg(blankLine)
    printg(blankLine)

    printg(margin + codes.fgLightWhite + "Health: " + "127/150          \n")

    printg(blankLine)

    printg(margin + codes.fgLightWhite + "Status: " + codes.fgLightPurple + "cursed" + codes.fgWhite + "           \n")

    #printg(margin + codes.fgPurple + "cursed" + codes.fgWhite + ", " + codes.fgLightBlue + "frozen           \n")

    printg(blankLine)
    printg(blankLine)

    # TODO: print status effects
    
def Draw(state):
    cls()

    grid.cells = [[], [], []]

    margin = "     "

    blankLine = "                              \n"
    
    match state:
        case "BATTLE":
            # Print health bars
            printl("\n\n\t\t\t\t   ")

            PrintBar(player.name, 127, player.maxHealth, 0)

            printl("\t\t\t  ")

            PrintBar("Death", 20, 60, 0)
            
            printl("\n")

            # -------------------------------------
            #      Grid begins (cell index 0)
            # -------------------------------------
            grid.cellIndex = 0

            printg(blankLine)
            printg(blankLine)

            # Print stats
            PrintStats()

            # Print action bar
            printg(codes.fgLightWhite)

            printg(margin)

            PrintBar("", 8, 60, 2)

            printg(codes.reset)

            printg("       \n")
            
            # Print mana bar
            printg(margin)

            PrintBar("", 20, 105, 1)

            printg("       \n")
            
            # Print selection menu
            menu.Print()

            # Grid cell 1
            grid.cellIndex = 1

            # Print player
            for line in ascii[0]:
                printg(line)

            # Grid cell 2
            grid.cellIndex = 2

            # Print enemy
            for line in ascii[1]:
                printg(line)

            grid.Print()

        case "PAUSE0" | "PAUSE1" | "PAUSE2":
            margin = "\t\t\t\t\t\t    "
            
            style = [codes.fgLightGreen, codes.fgLightGreen, codes.fgLightGreen, codes.fgLightGreen]

            match state[5]:
                case '0':
                    style[0] = codes.fgLightWhite

                case '1':
                    style[1] = codes.fgLightWhite

                case '2':
                    style[2] = codes.fgLightWhite
            
            print(codes.fgLightGreen)

            print("\n\n\n\n\n\n\n")

            print(margin + f" ______________")
            print(margin + f"|              |")
            print(margin + f"|    {style[0]}Resume{style[3]}    |")
            print(margin + f"|              |")
            print(margin + f"|  {style[1]}Save Game{style[3]}   |")
            print(margin + f"|              |")
            print(margin + f"|     {style[2]}Exit{style[3]}     |")
            print(margin + f"|______________|")
            

# -------------------------
#      Entry point
# -------------------------

playerName = "Entheo"
        
player = character.Character(playerName)

grid = grid.Grid()

menu = menu.Menu(grid, playerName)

ascii = ["", ""]

ascii[0] = LoadAscii("player")

ascii[1] = LoadAscii("enemy")

state = "BATTLE"

prevState = state

userInput = "\0"

Draw(state)

# Game loop
while True:
    userInput = "\0"

    match state:
        case "BATTLE":
            while userInput != b'\r' and userInput != b' ':
                userInput = msvcrt.getch()
                    
                if userInput == codes.DOWN and menu.selected < (len(menu.items) - 1):
                    if menu.selected == (menu.shownIndex + (menu.numLines - 1)):
                        menu.shownIndex += 1

                        Draw(state)

                    menu.selected += 1
                        
                elif userInput == codes.UP and menu.selected > 0:
                    if menu.selected == (menu.shownIndex):
                        menu.shownIndex -= 1

                        Draw(state)
   
                    menu.selected -= 1

                elif userInput == codes.ESC:
                    if menu.id != "MAIN":
                        menu.id = "MAIN"

                        menu.selected = -1

                        menu.shownIndex = 0

                    else:
                        prevState = state

                        state = "PAUSE"

                    break
                        
                else:
                    continue
                    
                if userInput != b'\xe0':
                    Draw(state)
            
            match menu.selected:
                case 0:
                    # Attack
                    pass

                case 1:
                    menu.id = "MAGIC"

                case 2:
                    menu.id = "ITEMS"

            menu.selected = 0

            Draw(state)

        case "PAUSE":
            selected = 0

            while userInput != b'\r':
                Draw(state + str(selected))
                
                userInput = msvcrt.getch()

                if userInput == codes.DOWN and selected < 2:
                    selected += 1
                        
                elif userInput == codes.UP and selected > 0:
                    selected -= 1

                elif userInput == codes.ESC:
                    state = prevState

                    Draw(state)

                    break
                        
                else:
                    continue

            if userInput == codes.ESC:
                continue

            match selected:
                case 0:
                    state = prevState

                    Draw(state)

                case 1:
                    # Save
                    pass

                case 2:
                    cls()

                    quit()