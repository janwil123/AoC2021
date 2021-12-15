from collections import defaultdict

# Read input

ll = 100

rules = {}

with open("input14.txt") as f:
    start = f.readline().strip()
    l = f.readline()
    for _ in range(ll):
        l,r = f.readline().strip().split(' -> ')
        rules[l] = r

# Parts 1 & 2

pairs = defaultdict(int)

for i in range(len(start)-1):
    pairs[start[i:i+2]] += 1

rounds = 10 # Put 40 here for Part 2

for _ in range(rounds):
    newpairs = defaultdict(int)
    for p in pairs:
        c = rules[p]
        newpairs[p[0]+c] += pairs[p]
        newpairs[c+p[1]] += pairs[p]
    pairs = newpairs

cnt = defaultdict(int)

for p in pairs:
    cnt[p[0]] += pairs[p]
    cnt[p[1]] += pairs[p]

cnt[start[0]] += 1
cnt[start[-1]]+= 1

vs = sorted(cnt.values())

print((vs[-1]-vs[0])//2)