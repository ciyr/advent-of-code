import re
import statistics
with open("input.txt", "r") as f:
    input_data = f.read()
    """Split the input data into a list of strings"""
    input_data = input_data.split("\n")
def convertBinaryToDecimal(binary_string):
    """Convert a binary string to decimal"""
    decimal = 0
    for i in range(len(binary_string)):
        decimal += int(binary_string[i]) * (2 ** (len(binary_string) - i - 1))
    return decimal
def transpose2dList(list_2d):
    """Transpose a 2d list"""
    return [list(i) for i in zip(*list_2d)]
def modeList(data):
    """Return the mode of a list"""
    x = statistics.multimode(data)
    if len(x) > 1:
        return "1"
    return x[0]
def solution_part_one(data):
    x = []
    data = transpose2dList(data)
    y = "1"*len(data)
    for i in range(len(data)):
        x.append(modeList(data[i]))
    y = str(int(y) - int("".join(x)))
    return convertBinaryToDecimal("".join(x))*convertBinaryToDecimal(y)
def o2_scrubber(data):
    x = ""
    z = len(data[0])
    for i in range(z):
        newLis = []
        newData = transpose2dList(data)
        x += modeList(newData[i])
        reg = x + "."*(len(data[0])-i-1)
        newLis = (re.findall(reg, "\n".join(data)))
        data = newLis.copy()
    return convertBinaryToDecimal(x)
def co2_scrubber(data):
    x = ""
    z = len(data[0])
    for i in range(0,z):
        newLis = []
        newData = transpose2dList(data)
        if len(newData[0]) == 1:
            x = "".join(data)
            return convertBinaryToDecimal(x)
        x += str(1 - int(modeList(newData[i])))
        reg = x + "."*(len(data[0])-i-1)
        newLis = (re.findall(reg, "\n".join(data)))
        data = newLis.copy()
    return convertBinaryToDecimal(x)
print(solution_part_one(input_data))
print(o2_scrubber(input_data) * co2_scrubber(input_data))