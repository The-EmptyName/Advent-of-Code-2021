# very slow

#file = ["3,4,3,1,2"]
file = open("input.txt")

fish = [i.strip() for i in file][0].split(",")

for i in range(256):
    if i % 25 == 0:
        print(i, "/256")
    for n in range(len(fish)):
        if int(fish[n]) > 0:
            fish[n] = str(int(fish[n])-1)
        else:
            fish[n] = "6"
            fish.append("8")

print(len(fish))
