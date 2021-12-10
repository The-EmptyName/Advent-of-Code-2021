#file = open("test.txt")
file = open("input.txt")

lines = [i.strip() for i in file]

closing = [")", "]", "}", ">"]
scoring = [1, 2, 3, 4]

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
    return False

points = []

for i in lines:
    opened = []
    corrupt = False
    for n in i:
        if n in closing:
            op = "(" if n == ")" else ("[" if n == "]" else ("{" if n == "}" else "<"))
            if not op == last_open(opened):
                corrupt = True
                break
        opened.append(n)
    if corrupt:
        continue
    complete = False
    completion = ""
    while not complete:
        o = last_open(opened)
        if o is False:
            complete = True
            break
        op = ")" if o == "(" else ("]" if o == "[" else ("}" if o == "{" else ">"))
        completion += op
        opened.append(op)
    s = 0
    for n in completion:
        s = s * 5 + scoring[closing.index(n)]
    points.append(s)

points.sort()

print(points[int((len(points)-1)/2)])
