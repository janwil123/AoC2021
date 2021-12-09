# Read input

lx = 100
ly = 100

inp = []
inp.append([10]*(lx+2))

with open("input09.txt") as f:
    for _ in range(ly):
        l = f.readline()
        ns = [10]
        for c in l.strip():
            ns.append(int(c))
        ns.append(10)
        inp.append(ns)

inp.append([10]*(lx+2))

# Part 1

sum = 0
lows = []

for i in range(1,ly+1):
    for j in range(1,lx+1):
        n = inp[i][j]
        if n < inp[i-1][j] and n < inp[i+1][j] and n < inp[i][j-1] and n < inp[i][j+1]:
            lows.append((i,j))
            sum += n+1

print(sum)

# Part 2

def dfs(p):
    visited.add(p)
    h = inp[p[0]][p[1]]
    a = inp[p[0]-1][p[1]]
    b = inp[p[0]+1][p[1]]
    c = inp[p[0]][p[1]-1]
    d = inp[p[0]][p[1]+1]
    if not((p[0]-1,p[1]) in visited) and a > h and a < 9:
        dfs((p[0]-1,p[1]))
    if not((p[0]+1,p[1]) in visited) and b > h and b < 9:
        dfs((p[0]+1,p[1]))
    if not((p[0],p[1]-1) in visited) and c > h and c < 9:
        dfs((p[0],p[1]-1))
    if not((p[0],p[1]+1) in visited) and d > h and d < 9:
        dfs((p[0],p[1]+1))

lens = []

for pt in lows:
    visited = set()
    dfs(pt)
    lens.append(len(visited))

lens.sort()

print(lens[-1]*lens[-2]*lens[-3])


