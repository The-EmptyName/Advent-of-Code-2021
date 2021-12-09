#file = open("test.txt")
file = open("input.txt")

hmap = [i.strip() for i in file]

risk = 0

for x in range(len(hmap)):
    for y in range(len(hmap[x])):
        if x == 0 and y == 0:
            if hmap[x][y] < hmap[x+1][y] and hmap[x][y] < hmap[x][y+1]:
                risk += int(hmap[x][y]) + 1
        elif x == len(hmap)-1 and y == len(hmap[x])-1:
            if hmap[x][y] < hmap[x-1][y] and hmap[x][y] < hmap[x][y-1]:
                risk += int(hmap[x][y]) + 1
        elif x == 0 and y == len(hmap[x])-1:
            if hmap[x][y] < hmap[x+1][y] and hmap[x][y] < hmap[x][y-1]:
                risk += int(hmap[x][y]) + 1
        elif x == len(hmap)-1 and y == 0:
            if hmap[x][y] < hmap[x-1][y] and hmap[x][y] < hmap[x][y+1]:
                risk += int(hmap[x][y]) + 1
        elif x == 0:
            if hmap[x][y] < hmap[x+1][y] and hmap[x][y] < hmap[x][y+1] and hmap[x][y] < hmap[x][y-1]:
                risk += int(hmap[x][y]) + 1
        elif y == 0:
            if hmap[x][y] < hmap[x+1][y] and hmap[x][y] < hmap[x][y+1] and hmap[x][y] < hmap[x-1][y]:
                risk += int(hmap[x][y]) + 1
        elif x == len(hmap)-1:
            if hmap[x][y] < hmap[x-1][y] and hmap[x][y] < hmap[x][y+1] and hmap[x][y] < hmap[x][y-1]:
                risk += int(hmap[x][y]) + 1
        elif y == len(hmap[x])-1:
            if hmap[x][y] < hmap[x-1][y] and hmap[x][y] < hmap[x][y-1] and hmap[x][y] < hmap[x+1][y]:
                risk += int(hmap[x][y]) + 1
        else:
            if hmap[x][y] < hmap[x+1][y] and hmap[x][y] < hmap[x][y+1] and hmap[x][y] < hmap[x-1][y] and hmap[x][y] < hmap[x][y-1]:
                risk += int(hmap[x][y]) + 1

print(risk)
