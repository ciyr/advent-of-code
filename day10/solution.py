from collections import deque
import statistics
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
count = 0
final = []
for i in range(len(input_data)):
    stack = []
    for j in range(len(input_data[i])):
        if input_data[i][j] == "(" or input_data[i][j] == "[" or input_data[i][j] == "{" or input_data[i][j] == "<":
            stack.append(input_data[i][j])
        else:
            if input_data[i][j] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    count += 3
                    break
            if input_data[i][j] == "]" :
                if stack[-1] == "[":
                    stack.pop()
                else:
                    count += 57
                    break
            if input_data[i][j] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    count += 1197
                    break
            if input_data[i][j] == ">":
                if stack[-1] == "<":
                    stack.pop()
                else:
                    count += 25137
                    break
        if j == len(input_data[i]) - 1:
            if len(stack) != 0:
                final.append(stack)
print(count)
result = []
for i in final:
    #reverse i (closing bracket stack will be opposite of opening bracket stack)
    i.reverse()
    score = 0
    for j in i:
        score = score*5
        if j == "(":
            score += 1
        elif j == "[":
            score += 2
        elif j == "{":
            score += 3
        else:
            score += 4
    result.append(score)
print(statistics.median(result))