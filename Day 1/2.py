file = open("./input.txt")
#file = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

m = [int(i) for i in file]

l = 0

for i in range(3, len(m)):
    if m[i-3] + m[i-2] + m[i-1] < m[i-2] + m[i-1] + m[i]:
        l += 1

print(l)
