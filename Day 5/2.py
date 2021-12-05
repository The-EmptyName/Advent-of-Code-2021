file = open("input.txt")
holes = open("holes.txt", "w")

vents = [i.strip() for i in file]

ans = 0

overlaps = []

def horizontal(line): # str[][] line
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return True
    return False

#I = 0

for i in vents:
    splt = i.split(" -> ")
    splt = [splt[0].split(","), splt[1].split(",")] # ex.: [ ['1', '1'], ['1, 3'] ]
    #print(splt, i)
    X, Y = 1, 1
    #if int(splt[0][0]) > int(splt[1][0]):
    #    X = -1
    #if int(splt[0][1]) > int(splt[1][1]):
    #    Y = -1
    #if horizontal(splt):
    #    for x in range(int(splt[0][0]), int(splt[1][0]) + X, X):
    #        for y in range(int(splt[0][1]), int(splt[1][1]) + Y, Y):
    #            holes.write(str(x) + "," + str(y)+".")
    #else:
    current = splt[0]
    holes.write(splt[0][0]+","+splt[0][1]+"\n")
    while not ( int(current[0]) == int(splt[1][0]) and int(current[1]) == int(splt[1][1]) ):
        if int(current[0]) < int(splt[1][0]):
            current[0] = str(int(current[0])+1)
        elif int(current[0]) > int(splt[1][0]):
            current[0] = str(int(current[0])-1)
        if int(current[1]) < int(splt[1][1]):
            current[1] = str(int(current[1])+1)
        elif int(current[1]) > int(splt[1][1]):
            current[1] = str(int(current[1])-1)
        #print(current, splt[1], i)
        holes.write(current[0]+","+current[1]+"\n")
    #print(I)
    #I += 1

holes.close()
file_2 = open("holes.txt")

Holes = [i.strip() for i in file_2]

I = 0

for i in Holes:
    number = 0
    for n in Holes:
        if i == n:
            number += 1
    if number > 1:
        overlaps.append(i)
    if I % 1000 == 0:
        print(I, "/", len(Holes))
    I += 1

print(len(list(set(overlaps))))

def display(holes, size):
    print()
    for y in range(size):
        for x in range(size):
            h = 0
            for i in holes:
                if int(i[0]) == x and int(i[2]) == y:
                    h += 1
            if h == 0:
                print(".", end = "")
            else:
                print(str(h), end = "")
        print()








