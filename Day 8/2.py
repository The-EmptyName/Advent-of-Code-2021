#file = open("test.txt")
file = open("input.txt")

signals = [i.strip().split(" | ") for i in file]

result = 0

def is_in(needle, haystack): # str needle, str haystack
    found = 0
    for i in haystack:
        for n in needle:
            if i == n:
                found += 1
    return True if found == len(needle) else False

def decode(signal): # str[] signal
    inp = signal[0].split(" ")
    decoded = ['', '', '', '', '', '', '', '', '', '']
    top, ur, lr, bl = "", "", "", "" # top, upper right, lower right, bottom left line
    for i in inp:
        if len(i) == 2:
            decoded[1] = "".join(sorted(i))
        elif len(i) == 3:
            decoded[7] = "".join(sorted(i))
        elif len(i) == 4:
            decoded[4] = "".join(sorted(i))
        elif len(i) == 7:
            decoded[8] = "".join(sorted(i))
    for i in decoded[7]:
        if i not in decoded[1]:
            top = i
            break
    while '' in decoded:
        for i in inp:
            digit = "".join(sorted(i))
            if not digit in decoded:
                if is_in(decoded[1], digit) and is_in(decoded[4], digit) and is_in(decoded[7], digit):
                    decoded[9] = digit
                    for n in decoded[8]:
                        if not is_in(n, digit):
                            bl = n
                            break
                    continue
                elif len(digit) == 5 and (not bl == "") and decoded[2] == "":
                    if is_in(bl, digit):
                        decoded[2] = digit
                        continue
                elif len(digit) == 5:
                    if is_in(decoded[1], digit):
                        decoded[3] = digit
                    elif not decoded[2] == "":
                        decoded[5] = digit
                    continue
                elif len(digit) == 6:
                    if not decoded[9] == "":
                        if is_in(decoded[1], digit):
                            decoded[0] = digit
                        else:
                            decoded[6] = digit     
    return decoded

for i in signals:
    numbers = decode(i)
    output = ""
    for n in i[1].split(" "):
        for k in numbers:
            if k == "".join(sorted(n)):
                output += str(numbers.index("".join(sorted(n))))
                break
    result += int(output)

print(result)






    
