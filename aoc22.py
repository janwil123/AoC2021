# Read input

ll = 420
cmd = []

with open("input22.txt") as f:
    for _ in range(ll):
        l = f.readline().strip()
        [com,p] = l.split(' ')
        pars = p.split(',')
        x1,x2 = map(int,pars[0][2:].split('..'))
        y1,y2 = map(int,pars[1][2:].split('..'))
        z1,z2 = map(int,pars[2][2:].split('..'))
        cmd.append((com,(x1,x2,y1,y2,z1,z2)))

# Part 1

lights = [[['off' for _ in range(-50,51)] for _ in range(-50,51) ] for _ in range(-50,51) ]

for n in range(20):
    for i in range(cmd[n][1][0],cmd[n][1][1]+1):
        for j in range(cmd[n][1][2],cmd[n][1][3]+1):
            for k in range(cmd[n][1][4],cmd[n][1][5]+1):
                lights[i][j][k] = cmd[n][0]

cnt = 0

for i in range(-50,51):
    for j in range(-50,51):
        for k in range(-50,51):
            if lights[i][j][k] == 'on':
                cnt += 1

print(cnt)

# Part 2

xss = set()
yss = set()
zss = set()

for c in cmd:
    xss.add((c[1][0],'b'))
    xss.add((c[1][1],'e'))
    yss.add((c[1][2],'b'))
    yss.add((c[1][3],'e'))
    zss.add((c[1][4],'b'))
    zss.add((c[1][5],'e'))

xs = sorted(list(xss))
ys = sorted(list(yss))   
zs = sorted(list(zss))

segx = []
x = xs[0][0]

for i in range(1,len(xs)):
    if xs[i][1] == 'b':
        if x <= xs[i][0]-1:
            segx.append((x,xs[i][0]-1))
        x = xs[i][0]
    else: # xs[i][1] == 'e':
        segx.append((x,xs[i][0]))
        x = xs[i][0] + 1

segy = []
y = ys[0][0]

for i in range(1,len(ys)):
    if ys[i][1] == 'b':
        if y <= ys[i][0]-1:
            segy.append((y,ys[i][0]-1))
        y = ys[i][0]
    else: # ys[i][1] == 'e':
        segy.append((y,ys[i][0]))
        y = ys[i][0] + 1

segz = []
z = zs[0][0]

for i in range(1,len(zs)):
    if zs[i][1] == 'b':
        if z <= zs[i][0]-1:
            segz.append((z,zs[i][0]-1))
        z = zs[i][0]
    else: # zs[i][1] == 'e':
        segz.append((z,zs[i][0]))
        z = zs[i][0] + 1

M = [[[False for _ in range(len(segz))] for _ in range(len(segy))] for _ in range(len(segx))]

for c in cmd:
    sxs = []
    sys = []
    szs = []
    for i in range(len(segx)):
        if segx[i][0] >= c[1][0] and segx[i][1] <= c[1][1]:
            sxs.append(i)
    for i in range(len(segy)):
        if segy[i][0] >= c[1][2] and segy[i][1] <= c[1][3]:
            sys.append(i)    
    for i in range(len(segz)):
        if segz[i][0] >= c[1][4] and segz[i][1] <= c[1][5]:
            szs.append(i)
    for i in sxs:
        for j in sys:
            for k in szs:
                M[i][j][k] = (c[0] == 'on')

cnt = 0 
for i in range(len(segx)):
    for j in range(len(segy)):
        for k in range(len(segz)):
            if M[i][j][k]:
                cnt += (segx[i][1]-segx[i][0]+1)*(segy[j][1]-segy[j][0]+1)*(segz[k][1]-segz[k][0]+1)

print(cnt)