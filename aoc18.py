# Read input

inputs =[]

with open("input18.txt") as f:
    ls = f.readlines()
    for l in ls:
        inputs.append(eval(l))

# Utility functions

def parse(l):
    if type(l) == int:
        return({'':l})
    else:
        [a,b] = l
        pa = parse(a)
        pb = parse(b)
        res = {}
        for p in pa:
            res['l'+p] = pa[p]
        for p in pb:
            res['r'+p] =pb[p]
        return res

def explode(d):
    res = d.copy()
    sl = sorted(list(d))
    depthfound = False
    for k in sl:
        if len(k) >= 5:
            depthfound = True
            break
    if not depthfound:
        return res
    a = res[k]
    b = res[k[:-1]+'r']
    i = sl.index(k)
    if i > 0:
        res[sl[i-1]] += a
    if i < len(sl)-2:
        res[sl[i+2]] += b
    del res[k]
    del res[k[:-1]+'r']
    res[k[:-1]] = 0
    return res

def split(d):
    res = d.copy()
    sl = sorted(list(d))
    largefound = False
    for k in sl:
        if res[k] >= 10:
            largefound = True
            break
    if not largefound:
        return res
    res[k+'l'] = res[k]//2
    res[k+'r'] = res[k] - res[k]//2
    del res[k]
    return res

def reduce(d):
    needswork = True
    s = d.copy()
    while needswork:
        r = explode(s)
        while not (r == s):
            s = r.copy()
            r = explode(s)
        s = split(r)
        needswork = (s != r)

    return(s)

def add(d1,d2):
    res = {}
    for k in d1:
        res['l'+k] = d1[k]
    for k in d2:
        res['r'+k] = d2[k]
    return res    

def recover(d):
    if len(d) == 1:
        return(d[''])
    ld = {}
    rd = {}
    for k in d:
        if k[0] == 'l':
            ld[k[1:]] = d[k]
        elif k[0] == 'r':
            rd[k[1:]] = d[k]
    return([recover(ld),recover(rd)])

def magnitude(l):
    if type(l) == int:
        return(l)
    else:    
        [a,b] = l
        return(3*magnitude(a)+2*magnitude(b))

# Part 1

p1 = parse(inputs[0])

for i in range(1,len(inputs)):
    p2 = parse(inputs[i])
    p1 = reduce(add(p1,p2))

print(magnitude(recover(p1)))

# Part 2

maxsum = 0

for i in range(len(inputs)):
    for j in range(len(inputs)):
        p1 = parse(inputs[i])
        p2 = parse(inputs[j])
        s = magnitude(recover(reduce(add(p1,p2))))
        if s > maxsum:
            maxsum = s

print(maxsum)
