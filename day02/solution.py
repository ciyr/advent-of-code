hpos, vpos = 0, 0
coords = []
with open("input.txt", "r") as f:
    input_data = f.read()
    """Split the input data into a list of strings"""
    input_data = input_data.split("\n")
for x in input_data:
    x = x.split(" ")
    coords.append(x)
# part 1
for i in range(len(coords)):
    if coords[i][0] == "up":
        vpos -= int(coords[i][1])
    elif coords[i][0] == "down":
        vpos += int(coords[i][1])
    else:
        hpos += int(coords[i][1])
print(hpos*vpos)
#part 2
hpos, vpos, aim = 0, 0, 0
for i in range(len(coords)):
    if coords[i][0] == "up":
        aim -= int(coords[i][1])
    elif coords[i][0] == "down":
        aim += int(coords[i][1])
    else:
        hpos += int(coords[i][1])
        vpos += aim*int(coords[i][1])
print(hpos*vpos)