# Second attempt with textbook Dijkstra

from queue import PriorityQueue

# Read input

inp = []

# Uncomment this for Part 1

# with open("input15.txt") as f:
#     ls = f.readlines()
#     for l in ls:
#         inp.append([int(c) for c in l.strip()])

# Uncomment this for Part 2

with open("input15.txt") as f:
    ls = f.readlines()
    for l in ls:
        ns = []
        n = [int(c) for c in l.strip()]
        for i in range(5):
            ns += list(map(lambda x: x+i if x+i <=9 else x+i-9,n))
        inp.append(ns)
    ydim = len(inp)
    for i in range(1,5):
        for j in range(ydim):
            inp.append(list(map(lambda x: x+i if x+i <=9 else x+i-9,inp[j])))        

# From here the common part starts

xdim = len(inp[0])
ydim = len(inp)

black = set()
dist = [[10000000 for _ in range(xdim)] for _ in range(ydim)]
dist[0][0] = 0

q = PriorityQueue()
q.put((0,(0,0)))

while not q.empty():
    v = q.get()
    if not v in black:
        black.add(v)
        if v[1] == (ydim-1,xdim-1):
            print(v[0])
            break
        surround = []
        (i,j) = v[1]
        if i > 0:
            surround.append((i-1,j))
        if j > 0: 
            surround.append((i,j-1))
        if i < ydim-1:
            surround.append((i+1,j))
        if j < xdim-1:
            surround.append((i,j+1))
        for u in surround:
            dist_u = v[0] + inp[u[0]][u[1]]
            if dist_u < dist[u[0]][u[1]]:
                dist[u[0]][u[1]] = dist_u
                q.put((dist_u,u))
