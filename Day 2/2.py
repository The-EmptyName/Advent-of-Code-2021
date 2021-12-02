file = open("./input.txt")
#file = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

moves = [i.split(" ") for i in file]

position, depth, aim = 0, 0, 0

for i in moves:
    if i[0] == "forward":
        position += int(i[1])
        depth += int(i[1]) * aim
    elif i[0] == "up":
        aim -= int(i[1])
    else:
        aim += int(i[1])

print(depth * position)
