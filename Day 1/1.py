file = open("./input.txt")
#file = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

measurements = [int(i) for i in file]

larger = 0

for i in range(1, len(measurements)):
    if measurements[i-1] < measurements[i]:
        larger += 1

print(larger)
