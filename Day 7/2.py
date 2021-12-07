import functools as ft

#file = ["16,1,2,0,4,2,7,1,2,14"]
file = open("input.txt")

crabs = [i.strip() for i in file][0].split(",")
crabs = [int(i) for i in crabs]

lowest = 999999999999999999999999999999999999999999999999999

def cost(n):
    s = 0
    for i in range(n, 0, -1):
        s += i
    return s

for i in range(max(crabs)):
    s = 0
    for n in crabs:
        s += ft.reduce(lambda x, y: x + y, list(range(0, abs(i - n)+1)))
    if s < lowest:
        lowest = s

print(lowest)
