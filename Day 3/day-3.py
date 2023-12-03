import re

class Part:
    def __init__(self, numberMatch, lineIndex):
        self.partNumber = int(numberMatch.group())
        self.lineIndex = lineIndex
        self.startIndex = numberMatch.start()
        self.endIndex = numberMatch.end() - 1
        self.isPart = False

class Symbol:
    def __init__(self, symbol, rowIndex, colIndex):
        self.symbol = symbol
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.adjacentParts = []

def extractParts(rows):
    return [Part(match, rowIndex) for rowIndex, row in enumerate(rows) for match in re.finditer("\d+", row)]

def extractSymbols(rows):
    return [Symbol(value, rowIndex, colIndex) for rowIndex, row in enumerate(rows) for colIndex, value in enumerate(row) if not (value.isdigit() or value == ".")]

def isVerticalMatch(part, symbol):
    return (symbol.rowIndex == part.lineIndex + 1 or symbol.rowIndex == part.lineIndex - 1) and (part.startIndex - 1 <= symbol.colIndex <= part.endIndex + 1)

def isHorizontalMatch(part, symbol):
    return symbol.rowIndex == part.lineIndex and (symbol.colIndex == part.startIndex - 1 or symbol.colIndex == part.endIndex + 1)

def validatePartNumbersAndGears(parts, symbols):
    for part in parts:
        for symbol in symbols:
            if isVerticalMatch(part, symbol) or isHorizontalMatch(part, symbol):
                part.isPart = True
                symbol.adjacentParts.append(part.partNumber)
    return parts

def sumPartNumbers(parts):
    return sum([part.partNumber for part in parts if part.isPart])

def determineGearRatios(symbols):
    return sum([symbol.adjacentParts[0] * symbol.adjacentParts[1] for symbol in symbols if len(symbol.adjacentParts) == 2])


def solve():
    with open("example.txt") as file:
        rows = [rows.strip() for rows in file.readlines()]
        possibleParts = extractParts(rows)
        symbols = extractSymbols(rows)
        
        # Part 1
        validatedPartNumbers = validatePartNumbersAndGears(possibleParts, symbols)
        print(sumPartNumbers(validatedPartNumbers))
        
        # Part 2
        print(determineGearRatios(symbols))


if __name__ == "__main__":
    solve()