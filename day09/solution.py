with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
    input_data = [list(x) for x in input_data]
    input_data = [[int(x) for x in y] for y in input_data]
def partOne(data):
    count = 0
    basin = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i > 0 and j > 0 and i < len(data)-1 and j < len(data[i])-1:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i+1][j] and data[i][j] < data[i][j-1] and data[i][j] < data[i][j+1]:
                    count += data[i][j]+1
                    basin.append([i,j])
            elif i == 0 and j > 0 and j < len(data[i])-1:
                if data[i][j] < data[i+1][j] and data[i][j] < data[i][j-1] and data[i][j] < data[i][j+1]:
                    count += data[i][j]+1
                    basin.append([i,j])
            elif i == len(data)-1 and j > 0 and j < len(data[i])-1:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i][j-1] and data[i][j] < data[i][j+1]:
                    count += data[i][j]+1
                    basin.append([i,j])
            elif j == 0 and i > 0 and i < len(data)-1:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i+1][j] and data[i][j] < data[i][j+1]:
                    count += data[i][j]+1
                    basin.append([i,j])
            elif j == len(data[i])-1 and i > 0 and i < len(data)-1:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i+1][j] and data[i][j] < data[i][j-1]:
                    count += data[i][j]+1
                    basin.append([i,j])
            elif i == 0 and j == 0:
                if data[i][j] < data[i+1][j] and data[i][j] < data[i][j+1]:
                    count += data[i][j]+1
                    basin.append([i,j])
            elif i == 0 and j == len(data[i])-1:
                if data[i][j] < data[i+1][j] and data[i][j] < data[i][j-1]:
                    count += data[i][j] +1
                    basin.append([i,j])
            elif i == len(data)-1 and j == 0:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i][j+1]:
                    count += data[i][j]
                    basin.append([i,j])
            elif i == len(data)-1 and j == len(data[i])-1:
                if data[i][j] < data[i-1][j] and data[i][j] < data[i][j-1]:
                    count += data[i][j]+1
                    basin.append([i,j])
    return count, basin
x = partOne(input_data)
print(x[0])
def check_basin(matrix, x, y, visited_nodes, r_len, c_len):
    if x < 0 or y < 0 or x > r_len or y > c_len \
            or matrix[x][y] == 9 \
            or (x, y) in visited_nodes:
        return

    visited_nodes.append((x, y))

    check_basin(matrix, x, y + 1, visited_nodes, r_len, c_len)
    check_basin(matrix, x, y - 1, visited_nodes, r_len, c_len)
    check_basin(matrix, x - 1, y, visited_nodes, r_len, c_len)
    check_basin(matrix, x + 1, y, visited_nodes, r_len, c_len)

def partTwo(data, basin):
    result = []
    for x in basin:
        i, j = x[0], x[1]
        visited = []
        check_basin(data, i, j, visited, len(data) - 1, len(data[0]) - 1)
        result.append(len(visited))
    result.sort(reverse=True)
    return result[0]*result[1]*result[2]
print(partTwo(input_data, x[1]))