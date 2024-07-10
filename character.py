from os.path import exists

class Character:
    def __init__(self, name):
        self.name = name

        self.magic = [[], [], [], []]

        self.LoadMagic()

        self.maxHealth = 150
        self.currentHealth = self.maxHealth
        # maxMana from file
        # self.currentMana = self.maxMana
        # attack from file
       
    def LoadMagic(self):
        self.magic = [[], [], [], []]

        saveFileName = __file__ + "\\..\\save_" + self.name

        labels = []

        details = []

        found = False

        if exists(saveFileName):
            file = open(saveFileName, "r")

            content = file.readlines()

            lineCount = 0

            for line in content:
                line.strip()

                if "#MAGIC" in line:
                    found = True

                    for i in range(lineCount, len(content)):
                        if "#" not in content[i]:
                            labels.append(content[i].strip())

                        else:
                            break

                if found == True:
                    break

                lineCount += 1

            file.close()

        else:
            print("Failed to open save file.\n")

            quit()

        if found == True and exists(__file__ + "\\..\\magic"):
            file = open(__file__ + "\\..\\magic", "r")

            content = file.readlines()

            for i in range(0, len(labels)):
                for j in range(0, len(content)):
                    if '#' in content[j] and labels[i] in content[j]:
                        self.magic[0].append(labels[i])
                        self.magic[1].append(content[j+1])
                        self.magic[2].append(content[j+2])
                        self.magic[3].append(content[j+3])

                        break
                            
            file.close()

        else:
            print("Failed to open magic data file.\n" + str(found))

            quit()