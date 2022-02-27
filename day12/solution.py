from collections import defaultdict
with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split("\n")
edges = defaultdict(list)
for line in input_data:
    line = line.split("-")
    edges[line[0]].append(line[1])
    edges[line[1]].append(line[0])
walks = []
walk = []
def find_walks(node):
    walk.append(node)
    if node == "end":
        walks.append(walk.copy())
        walk.pop()
        return
    for neighbor in edges[node]:
        if neighbor not in walk or neighbor.isupper():
            find_walks(neighbor)
    walk.pop()
find_walks("start")
print("Part 1: ", len(walks))
walks = []
walk = []
def find_walks2(node, double):
    walk.append(node)
    if node == "end":
        walks.append(walk.copy())
        walk.pop()
        return
    for neighbor in edges[node]:
        if (neighbor not in walk or neighbor.isupper()) and neighbor != double:
            find_walks2(neighbor, double)
        elif neighbor == double and walk.count(double) < 2:
            find_walks2(neighbor, double)
    walk.pop()
for edge in edges:
    if edge.islower() and edge != "start" and edge != "end":
        find_walks2("start", edge)
walks = [tuple(i) for i in walks]
walks = set(walks)
print("Part 2: ", len(walks))