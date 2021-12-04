# Read input

with open("input02.txt") as f:
    ns = f.readlines()

inp = [s.strip() for s in ns]

l = len(inp)

# First task

hor = 0
ver = 0

for s in inp:
    com = s.split()
    if com[0] == 'down':
        ver += int(com[1])
    elif com[0] == 'up':
        ver -= int(com[1])
    elif com[0] == 'forward':
        hor += int(com[1])

print(hor*ver)

# Second task

hor = 0
ver = 0
aim = 0

for s in inp:
    com = s.split()
    if com[0] == 'down':
        aim += int(com[1])
    elif com[0] == 'up':
        aim -= int(com[1])
    elif com[0] == 'forward':
        hor += int(com[1])
        ver += aim*int(com[1])

print(hor*ver)
