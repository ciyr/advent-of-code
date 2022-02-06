from collections import Counter
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
def partOne(data):
    listTup = []
    for i in range(len(data)):
        data[i] = data[i].split(" -> ")
    for i in range(len(data)):
        data[i][1] = data[i][1].split(",")
        data[i][0] = data[i][0].split(",")
    for i in range(len(data)):
        for j in range(len(data[i][0])):
            data[i][0][j] = int(data[i][0][j])
            data[i][1][j] = int(data[i][1][j])
    for i in range(len(data)):
        if data[i][0][0] == data[i][1][0]:
            for j in range(min(data[i][0][1], data[i][1][1]),(max(data[i][0][1], data[i][1][1])+1)):
                listTup.append(tuple([data[i][0][0],j]))
        elif data[i][0][1] == data[i][1][1]:
            for k in range(min(data[i][0][0], data[i][1][0]),(max(data[i][0][0], data[i][1][0])+1)):
                listTup.append(tuple([k, data[i][0][1]]))
    print(len([point for point in Counter(listTup).values() if point > 1]))
    return 1
def partTwo(dxta):
    listTup = []
    for i in range(len(dxta)):
        dxta[i] = dxta[i].split(" -> ")
    for i in range(len(dxta)):
        dxta[i][1] = dxta[i][1].split(",")
        dxta[i][0] = dxta[i][0].split(",")
    for i in range(len(dxta)):
        for j in range(len(dxta[i][0])):
            dxta[i][0][j] = int(dxta[i][0][j])
            dxta[i][1][j] = int(dxta[i][1][j])
    for i in range(len(dxta)):
        if dxta[i][0][0] == dxta[i][1][0]:
            for j in range(min(dxta[i][0][1], dxta[i][1][1]),(max(dxta[i][0][1], dxta[i][1][1])+1)):
                listTup.append(tuple([dxta[i][0][0],j]))
        elif dxta[i][0][1] == dxta[i][1][1]:
            for k in range(min(dxta[i][0][0], dxta[i][1][0]),(max(dxta[i][0][0], dxta[i][1][0])+1)):
                listTup.append(tuple([k, dxta[i][0][1]]))
        else:
            if (dxta[i][0][0] - dxta[i][1][0]) == (dxta[i][0][1] - dxta[i][1][1]):
                l = min(dxta[i][0][1], dxta[i][1][1])
                for k in range(min(dxta[i][0][0], dxta[i][1][0]),(max(dxta[i][0][0], dxta[i][1][0])+1)):
                    listTup.append(tuple([k, l]))
                    l += 1
            else:
                l = max(dxta[i][0][1], dxta[i][1][1])
                for k in range(min(dxta[i][0][0], dxta[i][1][0]),(max(dxta[i][0][0], dxta[i][1][0])+1)):
                    listTup.append(tuple([k, l]))
                    l -= 1
    print(len([point for point in Counter(listTup).values() if point > 1]))
    return 1
ipdata = input_data.copy()
partOne(ipdata)
partTwo(input_data)