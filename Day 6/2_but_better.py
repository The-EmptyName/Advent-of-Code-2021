#file = ["3,4,3,1,2"]
file = open("input.txt")

fish = [i.strip() for i in file][0].split(",")

fish_sorted = [0 for i in range(9)]

for i in fish:
    fish_sorted[int(i)] += 1

for i in range(256):
    fish_changed = [0 for i in range(9)]
    for n in range(len(fish_sorted)):
        if n == 0:
            fish_changed[8], fish_changed[6], fish_sorted[0] = fish_sorted[0], fish_sorted[0], 0
        else:
            fish_changed[n-1] += fish_sorted[n]
    fish_sorted = fish_changed
            
s = 0
for i in fish_sorted:
    s += i

print(s)
