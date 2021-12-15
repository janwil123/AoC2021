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

risk = [[0 for _ in range(xdim)] for _ in range(ydim)]

# First we run a regular dynamic programming routine,
# but this does not account for up and left steps.

s = 0
for i in range(1,xdim):
    s = s+inp[0][i]
    risk[0][i] = s

s = 0
for i in range(1,ydim):
    s = s+inp[i][0]
    risk[i][0] = s

for i in range(1,ydim):
    for j in range(1,xdim):
        m = min(risk[i][j-1],risk[i-1][j])
        risk[i][j] = m + inp[i][j]

# Find the places where taking a detour would make the 
# path less risky.

def findfaults():
    res = []
    for i in range(ydim):
        for j in range(xdim):
            if i+j>0:
                surround = []
                if i > 0:
                    surround.append(risk[i-1][j])
                if j > 0: 
                    surround.append(risk[i][j-1])
                if i < ydim-1:
                    surround.append(risk[i+1][j])
                if j < xdim-1:
                    surround.append(risk[i][j+1])           
                if risk[i][j] > min(surround) + inp[i][j]:
                    res.append((i,j,min(surround) + inp[i][j]))   
    return res

# Fix the risk estimates

def fixrisks():
    for i in range(ydim):
        for j in range(xdim):
            if i+j>0:
                surround = []
                if i > 0:
                    surround.append(risk[i-1][j])
                if j > 0: 
                    surround.append(risk[i][j-1])
                if i < ydim-1:
                    surround.append(risk[i+1][j])
                if j < xdim-1:
                    surround.append(risk[i][j+1])           
                if risk[i][j] > min(surround) + inp[i][j]:
                    risk[i][j] = min(surround) + inp[i][j]   

# Run the suboptimality detection and fixing as long as there is need
# and hope this process won't take forever.
# On my machine it takes about 20 seconds for the full problem.

faults = findfaults()

while faults:
    for f in faults:
        risk[f[0]][f[1]] = f[2]
    fixrisks()
    faults = findfaults()

print(risk[ydim-1][xdim-1])
