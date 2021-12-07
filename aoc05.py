# Read input

with open("input05.txt") as f:
    inputs = f.readlines()

inp = [s.strip() for s in inputs]

ll = len(inp)

lines = []

for i in range(ll):
    [left, right] = inp[i].split(' -> ')
    [x1,y1] = left.split(',')
    [x2,y2] = right.split(',')
    lines.append(((int(x1),int(y1)),(int(x2),int(y2))))


xmax = 1000
ymax = 1000

fill = []

for _ in range(ymax):
    fill.append([0]*xmax)

for l in lines:
    if l[0][0] == l[1][0]:
        a = min(l[0][1],l[1][1])
        b = max(l[0][1],l[1][1])
        for i in range(a,b+1):
            fill[i][l[0][0]] += 1 
        continue
    if l[0][1] == l[1][1]:
        a = min(l[0][0],l[1][0])
        b = max(l[0][0],l[1][0])
        for i in range(a,b+1):
            fill[l[0][1]][i] += 1 
        continue

    # Part 2; comment out for Part 1

    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    if a - b == c - d:
        if c < a:
            a,b,c,d = c,d,a,b
        for i in range(c-a+1):
            fill[b+i][a+i] += 1
        continue
    if a - c == d - b:
        if c < a:
            a,b,c,d = c,d,a,b
        for i in range(c-a+1):
            fill[b-i][a+i] += 1
        
cnt = 0

for i in range(ymax):
    for j in range(xmax):
        if fill[i][j] >= 2:
            cnt += 1

print(cnt)