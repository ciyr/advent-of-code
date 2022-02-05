import itertools
def calcScore(tick):
    score = 0
    for i in range(len(tick)):
        for j in range(len(tick[0])):
            if tick[i][j] != -1:
                score += tick[i][j]
    return score
with open("input.txt", "r") as f:
    input_data = f.read()
    """Split the input data into a list of strings"""
    input_data = input_data.split("\n\n")
numberList = input_data[0].split(",")
numberList = [int(i) for i in numberList]
bingo = []
for i in range(1,len(input_data)):
    indi = []
    indi = input_data[i].split("\n")
    for j in range(len(indi)):
        indi[j] = indi[j].split(" ")
        indi[j] = [int(x) for x in indi[j] if x != '']
    bingo.append(indi)
def partOne(ticket):
    tickCopy = ticket.copy()
    for i in range(len(numberList)):
        for x,y,z in itertools.product(range(len(tickCopy)),range(len(tickCopy[0])),range(len(tickCopy[0][0]))):
            if tickCopy[x][y][z] == numberList[i]:
                tickCopy[x][y][z] = -1
        for x in range(len(tickCopy)):
            for y in range(len(tickCopy[0])):
                if tickCopy[x][y][y] == -1:
                    if sum(tickCopy[x][y]) == -5:
                        print(calcScore(tickCopy[x])*numberList[i])
                        return 1
                    else:
                        coun = 0
                        for k in range(len(tickCopy[x])):
                            coun += tickCopy[x][k][y]
                        if coun == -5:
                            print(calcScore(tickCopy[x])*numberList[i])
                            return 1
                        else:
                            continue
def partTwo(ticket):
    tickCopy = ticket.copy()
    winCount = 0
    winList = []
    for i in range(len(numberList)):
        for x,y,z in itertools.product(range(len(tickCopy)),range(len(tickCopy[0])),range(len(tickCopy[0][0]))):
            if tickCopy[x][y][z] == numberList[i]:
                tickCopy[x][y][z] = -1
        for x in range(len(tickCopy)):
            for y in range(len(tickCopy[0])):
                if tickCopy[x][y][y] == -1:
                    if sum(tickCopy[x][y]) == -5 and x not in winList:
                        winList.append(x)
                        winCount += 1
                        if winCount == len(tickCopy):
                            print(calcScore(tickCopy[x])*numberList[i])
                            return 1
                    else:
                        coun = 0
                        for k in range(len(tickCopy[x])):
                            coun += tickCopy[x][k][y]
                        if coun == -5 and x not in winList:
                            winList.append(x)
                            winCount += 1
                            if winCount == len(tickCopy):
                                print(calcScore(tickCopy[x])*numberList[i])
                                return 1
                        else:
                            continue
partOne(bingo)
partTwo(bingo)