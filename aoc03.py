# Read input

with open("input03.txt") as f:
    inputs = f.readlines()

inp = [s.strip() for s in inputs]

l = len(inp)

m = len(inp[0])

# Part one

cnt = []

for i in range(m):
    c = 0
    for j in range(l):
        if inp[j][i] == '1':
            c+=1
    if c > l//2:
        cnt.append(1)
    else:
        cnt.append(0)

gamma = 0
epsilon = 0

for c in cnt:
    if c == 0:
        gamma *= 2
        epsilon = 2*epsilon + 1
    else:
        gamma = 2*gamma+1
        epsilon *= 2

print(gamma*epsilon)


# Part two

oxinds = set(range(l))

pos = 0

while len(oxinds) > 1:
    cnt = 0
    inds1 = set([])
    inds0 = set([])
    for i in oxinds:
        if inp[i][pos] == '1':
            cnt+=1
            inds1.add(i)
        else:
            inds0.add(i)
    if 2*cnt >= len(oxinds):
        oxinds = oxinds - inds0
    else:
        oxinds = oxinds - inds1
    pos += 1

co2inds = set(range(l))

pos = 0

while len(co2inds) > 1:
    cnt = 0
    inds1 = set([])
    inds0 = set([])
    for i in co2inds:
        if inp[i][pos] == '0':
            cnt+=1
            inds0.add(i)
        else:
            inds1.add(i)
    if 2*cnt <= len(co2inds):
        co2inds = co2inds - inds1
    else:
        co2inds = co2inds - inds0
    pos += 1

def bin2dec(ds):
    r = 0
    for d in ds:
        if d=='0':
            r*=2
        else:
            r = 2*r + 1
    return(r)

ox = list(oxinds)[0]
co2 = list(co2inds)[0]

print(bin2dec(inp[ox])*bin2dec(inp[co2]))
