from collections import defaultdict, Counter

# Read input

G = defaultdict(list)

with open("input12.txt") as f:
    lines = f.readlines()
    for l in lines:
        [u,v] = l.strip().split('-')
        G[u].append(v)
        G[v].append(u)

# Part 1

endpaths = 0

def dfs1(path):
    global endpaths
    l = path[-1]
    vs = G[l]
    for v in vs:
        if v == 'end':
            endpaths += 1
        elif v != 'start':
            if (ord(v[0]) >= 65 and ord(v[0])<= 90):
                dfs1(path+[v])
            else:
                if not v in path:
                    dfs1(path+[v])

dfs1(['start'])

print(endpaths)

# Part 2

def twice(p):
    cnt = Counter(p)
    twicefound = False
    for k in cnt:
        if (ord(k[0])>=97 and ord(k[0])<=122) and cnt[k]>=2:
            twicefound = True
    return twicefound

endpaths = 0

def dfs2(path):
    global endpaths
    l = path[-1]
    vs = G[l]
    for v in vs:
        if v == 'end':
            endpaths += 1
        elif v != 'start':
            if (ord(v[0]) >= 65 and ord(v[0])<= 90):
                dfs2(path+[v])
            else:
                if not twice(path) or not v in path:
                    dfs2(path+[v])

dfs2(['start'])

print(endpaths)

