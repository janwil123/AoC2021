# Read input

inp = [[0]*12]

with open("input11.txt") as f:
    for _ in range(10):
        l = f.readline().strip()
        inp.append([0]+list(map(int,list(l)))+[0])
    
inp.append([0]*12)

# Parts 1 & 2

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def findnines():
    res = []
    for i in range(1,11):
        for j in range(1,11):
            if inp[i][j] > 9:
                res.append((i,j))
    return res

flashes = 0
step = 0

while True:

    for i in range(1,11):
        for j in range(1,11):
            inp[i][j] += 1

    ns = findnines()
    nines = set(ns)
    newnines = ns 

    while newnines:
        for x in newnines:
            flashes += 1
            for d in dirs:
                inp[x[0]+d[0]][x[1]+d[1]]+=1
        ns = findnines()
        newnines = []
        for n in ns:
            if n not in nines:
                newnines.append(n)
                nines.add(n)

    for n in nines:
        inp[n[0]][n[1]] = 0

    if step == 99:
        print(f'Number of flashes within 100 steps: {flashes}')
    step += 1
    if len(nines)==100:
        print(f'The number of the step with first all-flash: {step}')
        break

