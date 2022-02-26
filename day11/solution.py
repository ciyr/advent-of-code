with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
    input_data = [list(x) for x in input_data]
    input_data = [[int(x) for x in y] for y in input_data]
def testBorders(matrix, x, y):
    if x < 0 or y < 0:
        return 0
    if x > len(matrix)-1 or y > len(matrix[0])-1:
        return 0
    return 1
def incrementNeighbors(matrix, x, y):
    for i in range(x-1, x+2):
        for m in range(y-1, y+2):
            if testBorders(matrix, i, m) and not (i == x and m == y):
                matrix[i][m] += 1
    return matrix
def partOne(data):
    result = 0
    for i in range(100):
        finish = []
        minisum = 0
        for m in range(len(data)):
            for n in range(len(data[0])):
                data[m][n] += 1
        for y in data:
            minisum += y.count(10)
        cnt = minisum
        while cnt > 0:
            minisum = 0
            for j in range(len(data)):
                for k in range(len(data[0])):
                    if data[j][k] > 9:
                        result += 1
                        data = incrementNeighbors(data, j, k)
                        finish.append([j, k])
                        data[j][k] = -100
            for x in data:
                for l in x:
                    if l > 9:
                        minisum += 1
            cnt = minisum
        for t in finish:
            data[t[0]][t[1]] = 0
    return result
def partTwo(data):
    i = 1
    while(True):
        result = 0
        finish = []
        minisum = 0
        for m in range(len(data)):
            for n in range(len(data[0])):
                data[m][n] += 1
        for y in data:
            minisum += y.count(10)
        cnt = minisum
        while cnt > 0:
            minisum = 0
            for j in range(len(data)):
                for k in range(len(data[0])):
                    if data[j][k] > 9:
                        result += 1
                        data = incrementNeighbors(data, j, k)
                        finish.append([j, k])
                        data[j][k] = -100
            for x in data:
                for l in x:
                    if l > 9:
                        minisum += 1
            cnt = minisum
        for t in finish:
            data[t[0]][t[1]] = 0
        if result == 100:
            return i + 100 
        i += 1
print(partOne(input_data))
print(partTwo(input_data))