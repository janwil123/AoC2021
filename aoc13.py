# Read input

ll = 741
cl = 12

dots = set()
cmds = []

with open("input13.txt") as f:
    for _ in range(ll):
        l = f.readline().strip()
        [x,y] = map(int,l.split(','))
        dots.add((x,y))
    l = f.readline()
    for _ in range(cl):
        l = f.readline().strip().split()[-1].split('=')
        cmds.append((l[0],int(l[1])))

# Part 1

c = cmds[0]

newdots = set()

if c[0] == 'x': # My input has this
    for d in dots:
        if d[0] < c[1]:
            newdots.add(d)
        else: 
            newdots.add((c[1]-(d[0]-c[1]),d[1]))

print(len(newdots))

# Part 2

def printdots():
    maxx = 0
    maxy = 0 

    for d in dots:
        if d[0] > maxx:
            maxx = d[0]
        if d[1] > maxy:
            maxy = d[1]

    M = [['.' for _ in range(maxy+1)] for _ in range(maxx+1)]

    for d in dots:
        M[d[0]][d[1]] = '#'

    M = list(zip(*M)) # Transpose the matrix for better readability

    for m in M:
        print(''.join(m))


for c in cmds:
    newdots = set()
    if c[0] == 'x':
        for d in dots:
            if d[0] < c[1]:
                newdots.add(d)
            else: 
                newdots.add((c[1]-(d[0]-c[1]),d[1]))
    else: # c[0] == 'y'
        for d in dots:
            if d[1] < c[1]:
                newdots.add(d)
            else: 
                newdots.add((d[0],c[1]-(d[1]-c[1])))
    dots = newdots      
    
printdots()     

