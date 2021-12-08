#file = open("test.txt")
file = open("input.txt")

signals = [i.strip() for i in file]
outputs = [i.split(" | ")[1] for i in signals]

result = 0

for i in outputs:
    for n in i.split(" "):
        lenn = len(n)
        if lenn == 2 or lenn == 4 or lenn == 3 or lenn == 7:
            result += 1

print(result)
