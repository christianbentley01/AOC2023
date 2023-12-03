import re

def getCalibrationValueForLine(line):
    digits = re.findall("\d", line)
    return int(digits[0]) * 10 + int(digits[len(digits) - 1])

def replaceStringDigits(line):
    stringsToInts = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    for string in stringsToInts:
        line = line.replace(string, string + stringsToInts[string] + string)
    return line

def solve():
    with open("example.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        
        # Part 1
        calibrationValues = [getCalibrationValueForLine(line) for line in lines]
        print(sum(calibrationValues))

        # Part 2
        digitisedLines = [replaceStringDigits(line) for line in lines]
        calibrationValues = [getCalibrationValueForLine(line) for line in digitisedLines]
        print(sum(calibrationValues))


if __name__ == "__main__":
    solve()