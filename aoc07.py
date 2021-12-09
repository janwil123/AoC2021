# Read input

with open("input07.txt") as f:
    inp = list(map(int,f.readline().split(',')))

posmin = min(inp)
posmax = max(inp)

# Part 1

minfuel = 1000000000

for i in range(posmin,posmax+1):
    less = list(filter(lambda x: x < i, inp))
    more = list(filter(lambda x: x > i, inp))
    s = sum([i-x for x in less])+sum([x-i for x in more])
    if s < minfuel:
        minfuel = s

print(minfuel)

# Part 2

def triang(n):
    return(n*(n+1)//2)

minfuel = 1000000000

for i in range(posmin,posmax+1):
    less = list(filter(lambda x: x < i, inp))
    more = list(filter(lambda x: x > i, inp))
    s = sum([triang(i-x) for x in less])+sum([triang(x-i) for x in more])
    if s < minfuel:
        minfuel = s

print(minfuel)