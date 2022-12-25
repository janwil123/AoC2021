# Read input

with open("input25.txt") as f:
    M = list(map(lambda l:list(l.strip()), f.readlines()))

xdim = len(M[0])
ydim = len(M)

def printM():
    for j in range(ydim):
        print(''.join(M[j]))

# Part 1

step = 1

while True:
    moveRight = []
    for j in range(ydim):
        for i in range(xdim):
            if M[j][i] == '>' and M[j][(i+1)%xdim] == '.':
                moveRight.append((i,j))
    for (i,j) in moveRight:
        M[j][i] = '.'
        M[j][(i+1)%xdim] = '>'
    moveDown = []
    for j in range(ydim):
        for i in range(xdim):
            if M[j][i] == 'v' and M[(j+1)%ydim][i] == '.':
                moveDown.append((i,j))
    for (i,j) in moveDown:
        M[j][i] = '.'
        M[(j+1)%ydim][i] = 'v'
    if len(moveRight) == 0 and len(moveDown) == 0:
        print(f'Last step: {step}')
        break
    else:
        step += 1
