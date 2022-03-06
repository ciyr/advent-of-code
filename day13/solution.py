import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n\n")
coords = input_data[0].split("\n")
coords = [x.split(",") for x in coords]
coords = [[int(x) for x in y] for y in coords]
folds = input_data[1].split("\n")
folds = [x.split("=") for x in folds]
coord_2 = coords.copy()
for i in folds:
    i[0] = i[0].replace("fold along ", "")
for coord in coords:
    if coord[0] > int(folds[0][1]):
        coord[0] = (2 * int(folds[0][1])) - coord[0]
coords = [tuple(x) for x in coords]
final = set(coords)
print(len(final))
for i in folds:
    if i[0] == "x":
        for coord in coord_2:
            if coord[0] > int(i[1]):
                coord[0] = coord[0] - int(i[1]) - 1
            else:
                coord[0] =  int(i[1]) - coord[0] - 1
    elif i[0] == "y":
        for coord in coord_2:
            if coord[1] > int(i[1]):
                coord[1] = coord[1] - int(i[1]) - 1
            else:
                coord[1] =  int(i[1]) - coord[1] - 1
coord_2 = [tuple(x) for x in coord_2]
final = set(coord_2)
final = list(final)
x_cords = [x[0] for x in final]
y_cords = [x[1] for x in final]
plt.scatter(x_cords, y_cords)
plt.show()