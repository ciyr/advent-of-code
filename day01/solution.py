with open("input.txt", "r") as f:
    input_data = f.read()
    """convert input data to list of ints"""
    input_data = [int(x) for x in input_data.split()]
def increaseList(data):
    """check how many elements in list are greater than previous one"""
    count = 0
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            count += 1
    return count
def threeElementMonty(data):
    count = 0
    for i in range(len(data)-3):
        if data[i]  < data[i+3]:
            count += 1
    return count
print(increaseList(input_data))
print(threeElementMonty(input_data))