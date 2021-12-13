#file = open("test.txt")
file = open("input.txt")

paper = [i.strip() for i in file]
instructions = [paper[i] for i in range(paper.index("")+1, len(paper))]
dots = [paper[i] for i in range(paper.index(""))]

def fold_y(y, dots): # int y, str[] dots
    for i in range(len(dots)):
        if int(dots[i].split(",")[1]) > y:
            dots[i] = dots[i].split(",")[0] + "," + str( int(dots[i].split(",")[1]) - 2 * (int(dots[i].split(",")[1])-y) )

def fold_x(x, dots): # int x, str[] dots
    for i in range(len(dots)):
        if int(dots[i].split(",")[0]) > x:
            dots[i] = str( int(dots[i].split(",")[0]) - 2 * (int(dots[i].split(",")[0])-x) ) + "," + dots[i].split(",")[1]

#fold_y(7, dots)
#fold_x(5, dots)

for i in range(len(instructions)):
    first = (instructions[i].split(" ")[-1]).split("=")
    if first[0] == "x":
        fold_x(int(first[1]), dots)
    else:
        fold_y(int(first[1]), dots)

print(len(set(dots)))

def display_test(dots):
    for y in range(6):
        for x in range(7 + 8*4):
            dot = False
            for i in range(len(dots)):
                if int(dots[i].split(",")[0]) == x and int(dots[i].split(",")[1]) == y:
                    print("#", end = "")
                    dot = True
                    break
            if not dot:
                print(".", end = "")
        print()

display_test(dots)
