from collections import Counter
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split(",")
def partOne(data):
    data = [int(x) for x in data]
    for i in range(80):
        x = data.copy()
        x += ([9]*len([point for point in data if point == 0]))
        data = x.copy()
        data = [7 if number == 0 else number for number in data]
        data = [number - 1 for number in data]
    print(len(data))
    return 1
def partTwo(data):
    countAge = [0]*9
    for i in data:
        countAge[int(i)] += 1
    for i in range(256):
        ageCopy = countAge.copy()
        for j in range(9):
            countAge[j] = ageCopy[(j+1)%9]
        countAge[6] += ageCopy[0]
    print(sum(countAge))
partOne(input_data)
partTwo(input_data)