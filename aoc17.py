# Apologies to the reader: several constants are hand-tuned. 

from collections import defaultdict

x1,x2,y1,y2 = 137,171,-98,-73

# Part 1

y1a = (-1)*y1
print(y1a*(y1a-1)//2)

# Part 2

xsteps = defaultdict(list)
ysteps = defaultdict(list)

for xtarget in range(x1,x2+1):
    for vvx in range(200,16,-1):
        vx = vvx
        x = 0
        step = 0
        while x <= x2 and vx > 0:
            x += vx
            step += 1
            if x == xtarget:
                xsteps[xtarget].append((step,vvx))
            if vx>0:
                vx -= 1
            
xsteps[153] += [(i,17) for i in range(18,200)]
xsteps[171] += [(i,18) for i in range(19,200)]

for ytarget in range(y1,y2+1):
    for vvy in range(-100,100):
        vy = vvy
        y = 0
        step = 0
        while y >= y1:
            y += vy
            step += 1
            if y == ytarget:
                ysteps[ytarget].append((step,vvy))
            vy -= 1

initvs = []

for xtarget in xsteps:
    for ytarget in ysteps:
        xlst = xsteps[xtarget]
        ylst = ysteps[ytarget]
        for xl in xlst:
            for yl in ylst:
                if xl[0] == yl[0]:
                    initvs.append((xl[1],yl[1]))

# Convert to set as some initial velocities may give several hits

print(len(set(initvs))) 
