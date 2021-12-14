#file = open("test.txt")
file = open("input.txt")

manual = [i.strip() for i in file]
template = manual[0]
rules = [manual[i] for i in range(2, len(manual))]

for k in range(10):
    finished = template[0]
    for i in range(0, len(template)-1):
        pair = template[i] + template[i+1]
        for n in rules:
            rule = n.split(" -> ")
            if rule[0] == pair:
                finished += rule[1] + pair[1]
                break
    template = finished

elements = list(set(template))
quantity = [0 for i in range(len(elements))]

for i in template:
    for n in range(len(elements)):
        if i == elements[n]:
            quantity[n] += 1
            break

print(max(quantity)-min(quantity))
