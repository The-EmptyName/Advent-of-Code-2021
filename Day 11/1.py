#file = open("test.txt")
file = open("input.txt")

dumbos = [list(i.strip()) for i in file]

temp = []
for i in range(len(dumbos[0])):
    temp.append("*")
    
dumbos.insert(0, temp)
dumbos.append(temp)

for i in range(len(dumbos)):
    dumbos[i].insert(0, "*")
    dumbos[i].append("*")

s = 0

changed = []

def add(x, y, dumbos): # int x, int y, str[][] dumbos
    global s
    global changed
    if not dumbos[y][x] == "*":
        dumbos[y][x] = str(int(dumbos[y][x]) + 1)
        if int(dumbos[y][x]) > 9:
            s += 1
            dumbos[y][x] = "*" #str(int(dumbos[y][x]) - 10)
            changed.append([x,y])
            add(x-1, y-1, dumbos)
            add(x, y-1, dumbos)
            add(x+1, y-1, dumbos)
            add(x-1, y, dumbos)
            add(x+1, y, dumbos)
            add(x, y+1, dumbos)
            add(x+1, y+1, dumbos)
            add(x-1, y+1, dumbos)
            dumbos[y][x] = "0"

for i in range(100):
    for y in range(len(dumbos)):
        for x in range(len(dumbos[y])):
            add(x, y, dumbos)
            for k in changed:
                dumbos[k[1]][k[0]] = "0"
    changed = []
        
print(s)
