#file = open("test.txt")
file = open("input.txt")

lines = [i.strip() for i in file]

corrupt = [0, 0, 0, 0]
closing = [")", "]", "}", ">"]


def last_open(line): # str[] line
    opening = ["(", "[", "{", "<"]
    for i in range(len(line)-1, -1, -1):
        if line[i] in opening:
            op = ")" if line[i] == "(" else ("]" if line[i] == "[" else ("}" if line[i] == "{" else ">")) # oposite
            closed = False
            for n in range(len(line)-1, i, -1):
                if line[n] == op:
                    closed = True
                    line[i] = "."
                    line[n] = "."
                    break
            if not closed:
                return line[i]
    return ""

for i in lines:
    opened = []
    for n in i:
        if n in closing:
            op = "(" if n == ")" else ("[" if n == "]" else ("{" if n == "}" else "<"))
            if not op == last_open(opened):
                if n == ")":
                    corrupt[0] += 1
                elif n == "]":
                    corrupt[1] += 1
                elif n == "}":
                    corrupt[2] += 1
                else:
                    corrupt[3] += 1
                break
        opened.append(n)

print(corrupt[0] * 3 + corrupt[1] * 57 + corrupt[2] * 1197 + corrupt[3] * 25137)


# "[({<)"
