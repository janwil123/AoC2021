from collections import defaultdict

# Read input

scanreads = []
scanners = 31

with open("input19.txt") as f:
    ls = [l.strip() for l in f.readlines()]

i = 0 

for s in range(scanners):
    readings = set()
    while len(ls[i]) > 0:
        if ls[i][:3] != '---':
            reading = tuple(map(int,ls[i].split(',')))
            readings.add(reading)
        i += 1
    scanreads.append(readings)
    i += 1

# Utility functions for matrix and vector operations

def mm(M1,M2): # 3x3 Matrix multiplication
    M = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            M[i][j] = M1[i][0]*M2[0][j] + M1[i][1]*M2[1][j] + M1[i][2]*M2[2][j]
    return ((tuple(M[0]),tuple(M[1]),tuple(M[2])))

def mv(M,v): # Matrix x vector multiplication
    r = []
    for i in range(3):
        r.append(M[i][0]*v[0]+M[i][1]*v[1]+M[i][2]*v[2])
    return(tuple(r))

def av(v1,v2): # Add vectors
    return((v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]))

def ds(v1,v2): # Distance squared
    return((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2)

def neg(v):
    return(((-1)*v[0],(-1)*v[1],(-1)*v[2]))

def distprofile(s):
    res = set()
    for a in s:
        for b in s:
            if a!=b:
                res.add(ds(a,b))
    return res

def compose(trans1,trans2):
    return( (mm(trans2[0],trans1[0]) , av(mv(trans2[0],trans1[1]),trans2[1])) )


# Generate all rotation matrices from the basic rotations

id   = ((1,0,0),(0,1,0),(0,0,1))
rotx = ((1,0,0),(0,0,-1),(0,1,0))
roty = ((0,0,1),(0,1,0),(-1,0,0))
rotz = ((0,-1,0),(1,0,0),(0,0,1))

rotmats = set([id,rotx,roty,rotz])

while True:
    newmats = set()
    for mat in rotmats:
        if mm(mat,rotx) not in rotmats:
            newmats.add(mm(mat,rotx))
        if mm(mat,roty) not in rotmats:
            newmats.add(mm(mat,roty))
        if mm(mat,rotz) not in rotmats:
            newmats.add(mm(mat,rotz))
    if len(newmats) == 0:
        break
    else:
        rotmats = rotmats.union(newmats)

# The graph representing overlapping scans
G = defaultdict(list)

for i in range(scanners-1):
    for j in range (i+1,scanners):
        if len(distprofile(scanreads[i]).intersection(distprofile(scanreads[j]))) >= 66:
            G[i].append(j)
            G[j].append(i)

# It is probably not the most optimal way of finding matching scans, but O(n^4) 
# for n being the the average number of beacons around one scanner is good enough.

def findtrans(i,j):
    matchfound = False
    for a in scanreads[i]:
        for b in scanreads[i]:
            if a != b:
                for d in scanreads[j]:
                    for e in scanreads[j]:
                        if ds(a,b) == ds(d,e):
                            for c in scanreads[i]:
                                for f in scanreads[j]:
                                    if (d!=e and e!=f and f!=d) and ds(b,c) == ds(e,f) and ds(c,a) == ds(f,d):
                                        matchfound = True
                                        break
                                if matchfound:
                                    break
                        if matchfound:
                            break
                    if matchfound:
                        break
            if matchfound:
                break
        if matchfound:
            break

    for rotmat in rotmats:
        if av(mv(rotmat,d),neg(a)) == av(mv(rotmat,e),neg(b)) == av(mv(rotmat,f),neg(c)):
            return((rotmat,neg(av(mv(rotmat,f),neg(c)))))

visited = [False for _ in range(scanners)]
transitions = [(((1,0,0),(0,1,0),(0,0,1)),(0,0,0)) for _ in range(scanners)]
beacons = scanreads[0].copy()

def dfs(n):
    visited[n] = True
    for m in G[n]:
        if not(visited[m]):
            t = findtrans(n,m)
            t1 = compose(t,transitions[n])
            transitions[m] = t1
            for p in scanreads[m]:
                beacons.add(av(mv(t1[0],p),t1[1]))
            dfs(m)

dfs(0)

# Part one

print(len(beacons))

# Part two

ds = [t[1] for t in transitions]

maxdist = 0

for i in range(scanners-1):
    for j in range(i,scanners):
        d = abs(ds[i][0]-ds[j][0]) + abs(ds[i][1]-ds[j][1]) + abs(ds[i][2]-ds[j][2])  
        if d > maxdist:
            maxdist = d

print(maxdist)