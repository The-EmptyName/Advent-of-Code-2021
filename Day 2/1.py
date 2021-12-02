file = open("./input.txt")
#file = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

moves = [i.split(" ") for i in file]

depth, position = 0, 0

for i in moves:
    if i[0] == "forward":
        position += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])
    else:
        depth += int(i[1])

print(depth * position)
