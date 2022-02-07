with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
def partOne(data):
    #split each element of data with '|' delimite
    data = [x.split(" | ")[1] for x in data]
    data = [x.split(" ") for x in data]
    data = [item for sublist in data for item in sublist]
    count = 0
    test = [2,3,4,7]
    for i in data:
        if len(i) in test:
            count += 1
    return count
print(partOne(input_data))
def partTwo(data):
    codes = [x.split(" | ")[0].split(" ") for x in data]
    output = [x.split(" | ")[1].split(" ") for x in data]
    sum = 0
    for i in range(len(codes)):
        digMap = {}
        for x in codes[i]:
            if len(x) == 2:
                digMap[1] = x
            elif len(x) == 3:
                digMap[7] = x
            elif len(x) == 4:
                digMap[4] = x
            elif len(x) == 7:
                digMap[8] = x
        for x in codes[i]:
            if len(x) == 6:
                if set(digMap[4]).issubset(set(x)):
                    digMap[9] = x
                elif set(digMap[1]).issubset(set(x)):
                    digMap[0] = x
                else:
                    digMap[6] = x
        for x in codes[i]:
            if len(x) == 5:
                if set(x).issubset(set(digMap[6])):
                    digMap[5] = x
                elif set(digMap[7]).issubset(set(x)):
                    digMap[3] = x
                else:
                    digMap[2] = x
        x = ""
        for y in output[i]:
            for key, value in digMap.items():
                if set(value) == set(y):
                    x += str(key)
        sum += int(x)
    return sum
print(partTwo(input_data))