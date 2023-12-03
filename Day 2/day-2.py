import re

maxRed = 12
maxGreen = 13
maxBlue = 14

class Game:
    def __init__(self, gameID, maxBlueObs, maxGreenObs, maxRedObs):
        self.gameID = gameID
        self.maxBlueObs = maxBlueObs
        self.maxGreenObs = maxGreenObs
        self.maxRedObs = maxRedObs

def getMaxObs(line, colour):
    obs = re.findall("\d+(?= {})".format(colour), line)
    return 0 if len(obs) == 0 else max([int(obsCount) for obsCount in obs])

def gameWasPossible(game):
    return game.maxBlueObs <= maxBlue and game.maxGreenObs <= maxGreen and game.maxRedObs <= maxRed

def solve():
    with open("example.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        games = [Game(lineIndex + 1, getMaxObs(line, "blue"), getMaxObs(line, "green"), getMaxObs(line, "red")) for lineIndex, line in enumerate(lines)]

        # Part 1
        print(sum([game.gameID for game in games if gameWasPossible(game)]))

        # Part 2
        print(sum([game.maxBlueObs * game.maxGreenObs * game.maxRedObs for game in games]))

if __name__ == "__main__":
    solve()