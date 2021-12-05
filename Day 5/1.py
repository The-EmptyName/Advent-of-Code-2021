file = open("input.txt")

vents = [i.strip() for i in file]

ans = 0

holes = []
overlaps = []

def horizontal(line): # str[][] line
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return True
    return False

for i in vents:
    splt = i.split(" -> ")
    splt = [splt[0].split(","), splt[1].split(",")] # ex.: [ ['1', '1'], ['1, 3'] ]
    if horizontal(splt):
        if int(splt[0][0]) > int(splt[1][0]) or int(splt[0][1]) > int(splt[1][1]):
            splt[0], splt[1] = splt[1], splt[0]
        for x in range(int(splt[0][0]), int(splt[1][0]) + 1):
            for y in range(int(splt[0][1]), int(splt[1][1]) + 1):
                holes.append(str(x) + "," + str(y))
   
for i in holes:
    number = 0
    for n in holes:
        if i == n:
            number += 1
    if number > 1:
        overlaps.append(i)

print(len(list(set(overlaps))))
