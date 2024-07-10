from os.path import exists
import ctypes

import codes

def printl(arg):
    print(arg, end = "")

class Menu:
    def __init__(self, grid, character):
        self.grid = grid

        self.save = __file__ + "\\..\\save_" + character

        self.id = "MAIN"

        self.selected = 0

        self.shownIndex = 0

        self.data = [[], [], {}]

        self.Update()

    def Update(self):
        if exists(self.save):
                for idIndex in range(0, 3):
                    match idIndex:
                        case 0:
                            id = "SKILLS"
                        
                        case 1:
                            id = "MAGIC"

                        case 2:
                            id = "ITEMS"

                    file = open(self.save, "r")

                    content = file.readlines()

                    lineCount = 0

                    for line in content:
                        lineCount += 1
                        
                        if ("#" + id) in line:
                            for i in range(lineCount, len(content)):
                                if "#" in content[i]:
                                    break

                                else:
                                    if content[i] != "\n":
                                        if id != "ITEMS":
                                            self.data[idIndex].append(content[i].strip())

                                        else:
                                            buffer = content[i].split(", ")

                                            self.data[idIndex][buffer[0]] = int(buffer[1])

                            break

                    file.close()

        else:
            ctypes.windll.user32.MessageBoxW(0, "File doesn't exist", "Debug", 1)
        
    def Print(self):
        arrow = [chr(24), chr(25)]

        self.items = []

        if self.id == "MAIN":
            self.items = ["Attack", "Magic", "Items"]

            menuType = 0

        elif self.id == "SKILLS":
            self.items = self.data[0]

            menuType = 1

        elif self.id == "MAGIC":
            self.items = self.data[1]

            menuType = 1

        elif self.id == "ITEMS":
            self.items = list(self.data[2].keys())

            menuType = 1

        if menuType == 0:
            self.numLines = 3

        else:
            self.numLines = 5

        self.grid.Write(codes.fgLightWhite + "     _____________________    \n")
        
        if self.shownIndex > 0:
            self.grid.Write(codes.fgLightWhite + f"    |                     |{arrow[0]}  \n")

        else:
            self.grid.Write(codes.fgLightWhite +"    |                     |   \n")
        
        for i in range(0, self.numLines):
            if (self.shownIndex + i) < len(self.items):
                exhausted = False

            else:
                exhausted = True

            if exhausted == False:
                self.grid.Write(codes.fgLightWhite + "    |   ")
                    
                if (self.shownIndex + i) == self.selected:
                    self.grid.Write(codes.fgLightWhite + self.items[self.shownIndex + i] + "  " + chr(17) + codes.fgLightWhite)
                    
                else:
                    self.grid.Write(codes.fgWhite + self.items[self.shownIndex + i] + codes.fgLightWhite)
                
                if (self.shownIndex + i) == self.selected:
                    for j in range(0, (15 - len(self.items[self.shownIndex + i]))):
                        self.grid.Write(" ")
                        
                else:
                    for j in range(0, (18 - len(self.items[self.shownIndex + i]))):
                        self.grid.Write(" ")
                    
                self.grid.Write(codes.fgLightWhite + "|   \n")

            else:
                self.grid.Write(codes.fgLightWhite + "    |                     |   \n")
            
            if (self.shownIndex + i) != (self.shownIndex + 2) and menuType == 0:
                self.grid.Write(codes.fgLightWhite + "    |                     |   \n")
            
        if (self.shownIndex + (self.numLines - 1)) < (len(self.items) - 1):
            self.grid.Write(codes.fgLightWhite + f"    |_____________________|{arrow[1]}  \n")

        else:
            self.grid.Write(codes.fgLightWhite + "    |_____________________|   \n")

        if self.id == "MAGIC":
            pass

        elif self.id == "ITEMS":
            self.grid.Write(codes.fgLightWhite + "     (" + str(self.data[2][self.items[self.selected]]) + ")\n")