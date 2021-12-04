import functools
import operator
foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)

#Read input

f = open("input04.txt", "r")

nums = list(map(int,f.readline().split(',')))

# 3 for test, 100 for real input
bs = 100

boards = []
marked = []

for _ in range(bs):
    l = f.readline() #Empty line
    board = []
    m = []
    for _ in range(5):
        board.append(list(map(int,f.readline().split())))
        m.append([False,False,False,False,False])
    boards.append(board)
    marked.append(m)

def win(board):
    res = False
    for i in range(5):
        res = res or foldl(operator.and_, True,board[i])
    borad_tr = list(zip(*board))
    for i in range(5):
        res = res or foldl(operator.and_, True,borad_tr[i])
    return res

# Part 1

Iwin = False

for n in nums:
    for h in range(bs):
        for i in range(5):
            for j in range(5):
                if boards[h][i][j] == n:
                    marked[h][i][j] = True
                    if win(marked[h]):
                        # Compute the score for the board
                        sum = 0
                        for k in range(5):
                            for l in range(5):
                                if marked[h][k][l] == False:
                                    sum += boards[h][k][l] 
                        print(sum*n)
                        Iwin = True
                if Iwin:
                    break
            if Iwin:
                break
        if Iwin:
            break
    if Iwin:
        break

# Part 2

boards_won = 0
won = [False]*bs

for n in nums:
    for h in range(bs):
        for i in range(5):
            for j in range(5):
                if boards[h][i][j] == n:
                    marked[h][i][j] = True
                    if not(won[h]) and win(marked[h]):
                        won[h] = True
                        boards_won += 1
                        if boards_won == bs: 
                            # Compute the score for the last board
                            sum = 0
                            for k in range(5):
                                for l in range(5):
                                    if marked[h][k][l] == False:
                                        sum += boards[h][k][l] 
                            print(sum*n)
