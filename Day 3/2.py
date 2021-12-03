file = open("./input.txt")
#file = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

numbers = [i.strip() for i in file]

oxygen, co2 = "", ""

def bin_to_dec(x): # str x
    s = 0
    n = 0
    for i in x[::-1]:
        s += 2 ** n * int(i)
        n += 1
    return s

co2_viable, oxygen_viable = numbers, numbers

for i in range(len(numbers[0])):
    ones, zeros = 0, 0
    has_0, has_1 = [], []
    for n in co2_viable:
        if n[i] == "0":
            zeros += 1
            has_0.append(n)
        else:
            ones += 1
            has_1.append(n)
    if zeros > ones:
        co2_viable = has_1
    else:
        co2_viable = has_0
    if len(co2_viable) == 1:
        break

for i in range(len(numbers[0])):
    ones, zeros = 0, 0
    has_0, has_1 = [], []
    for n in oxygen_viable:
        if n[i] == "0":
            zeros += 1
            has_0.append(n)
        else:
            ones += 1
            has_1.append(n)
    if zeros > ones:
        oxygen_viable = has_0
    else:
        oxygen_viable = has_1
    if len(oxygen_viable) == 1:
        break

print(bin_to_dec(co2_viable[0]) * bin_to_dec(oxygen_viable[0]))
