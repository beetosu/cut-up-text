import math

def cut_up(texts, interval):
    separateWords = []
    splitLetter = []
    smallestLetter = math.inf
    newLetter = ""
    intervalCount = 0
    wordCount = 0
    currentLetter = 0
    for file in texts:
        with open(file) as f:
            for line in f:
                splitLetter = line.split()
                separateWords.append(splitLetter)
    for i in separateWords:
        if len(i) < smallestLetter:
            smallestLetter = len(i)
    while wordCount < smallestLetter - 1:
        if intervalCount < interval:
            newLetter += separateWords[currentLetter][wordCount] + " "
            intervalCount += 1
            wordCount += 1
        else:
            intervalCount = 0
            if currentLetter == len(separateWords) - 1:
                currentLetter = 0
            else:
                currentLetter += 1
    return newLetter