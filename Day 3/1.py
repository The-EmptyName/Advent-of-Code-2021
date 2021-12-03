#file = open("./input.txt")
file = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

numbers = [i.strip() for i in file]

def bin_to_dec(x): # str x
    s = 0
    n = 0
    for i in x[::-1]:
        s += 2 ** n * int(i)
        n += 1
    return s

zeros = []
ones = []

for i in numbers:
    for n in range(len(i)):
        if len(zeros) == n:
            zeros.append(0)
            ones.append(0)
        if i[n] == "0":
            zeros[n] += 1
        else:
            ones[n] += 1

gamma = ""
epsilon = ""

for i in range(len(zeros)):
    if zeros[i] > ones[i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(bin_to_dec(gamma) * bin_to_dec(epsilon))
