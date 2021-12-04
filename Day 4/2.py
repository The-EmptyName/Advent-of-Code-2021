file_1 = open("input_1.txt")
file_2 = open("input_2.txt")

numbers = [i.strip() for i in file_1][0].split(",")
boards = [i.strip() for i in file_2]
boards_split = []
boards_final = []
score = 0

def winning(board): # str[][] board
    wins = False
    for i in board:
        for n in i: # checking rows
            wins = True
            if n != "M":
                wins = False
                break
        if wins:
            return True
    for i in range(len(board)): # checking columns
        if board[0][i] == "M":
            wins = True
            for n in range(len(board[0])):
                if board[n][i] != "M":
                    wins = False
                    break
            if wins:
                return True
        else:
            continue
    return False

def sum_of_unmarked(board): # str[][] board
    s = 0
    for i in board:
        for n in i:
            if n != "M":
                s += int(n)
    return s

def mark(board, number): # str[][] board, str number
    for i in range(len(board)):
        for n in range(len(board[0])):
            if board[i][n] == number:
                board[i][n] = "M"
                return True
    return False

def clean_up(board): # str[][] board
    for i in range(len(board)):
        for n in range(len(board[i])):
            if n >= len(board[i]):
                break
            if board[i][n] == "":
                del board[i][n]

temp = []
for i in boards:
    if i == "":
        if temp != []:
            boards_split.append(temp)
            temp = []
        continue
    temp.append(i)

for i in boards_split:
    temp_2 = []
    for n in i:
        temp_2.append(n.split(" "))
    boards_final.append(temp_2)

for i in range(len(boards_final)):
    clean_up(boards_final[i])

won = False

for i in numbers:
    for n in boards_final:
        if mark(n, i):
            if winning(n):
                print(int(i) * sum_of_unmarked(n))
                boards_final[boards_final.index(n)] = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]
