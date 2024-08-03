import codes

class Grid:
    # Initialize grid object
    def __init__(self):
        self.cells = [[], [], []]
        self.height = 26
        self.cellIndex = 0

    # Write to grid
    def Write(self, line):
        if len(self.cells[self.cellIndex]) == 0:
            self.cells[self.cellIndex].append(line)

        else:
            prevLine = self.cells[self.cellIndex][len(self.cells[self.cellIndex]) - 1]

            if prevLine[len(prevLine) - 1] == '\n':
                self.cells[self.cellIndex].append(line)

            else:
                self.cells[self.cellIndex][len(self.cells[self.cellIndex]) - 1] += line

    # Print grid
    def Print(self):
        for i in range(0, self.height):
            if len(self.cells[0]) > i:
                print(self.cells[0][i].strip("\n") + "        " + self.cells[1][i].strip("\n") + codes.reset + "    " + self.cells[2][i].strip("\n"))