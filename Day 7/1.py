#file = ["16,1,2,0,4,2,7,1,2,14"]
file = open("input.txt")

crabs = [i.strip() for i in file][0].split(",")
crabs = [int(i) for i in crabs]

lowest = 999999999999999999999999999999999999999999999999999

for i in range(max(crabs)):
    s = 0
    for n in crabs:
        s += abs(i - n)
    if s < lowest:
        lowest = s

print(lowest)
