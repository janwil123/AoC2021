import itertools

# Read input

inps = []
outs = []

ll = 200 

with open("input08.txt") as f:
    for _ in range(ll):
        [l,r] = f.readline().strip().split(' | ')
        inps.append(l.split(' '))
        outs.append(r.split(' '))

# Part 1

cnt = 0

for out in outs:
    for o in out:
        if len(o) in [2,3,4,7]:
            cnt += 1

print(cnt)

# Part 2

good = [['a','b','c','e','f','g'],
        ['c','f'],
        ['a','c','d','e','g'], 
        ['a','c','d','f','g'],
        ['b','c','d','f'], 
        ['a','b','d','f','g'],
        ['a','b','d','e','f','g'],
        ['a','c','f'],
        ['a','b','c','d','e','f','g'],
        ['a','b','c','d','f','g']]

def apply_perm(s,perm):
    res = []
    for c in s:
        n = ord(c)-97
        res.append(chr(97+perm[n]))
    return sorted(res)

summa = 0

for i in range(ll):
    inp = inps[i]
    out = outs[i]
    for p in itertools.permutations(range(7)):
        allgood = True
        for num in inp:
            guess = apply_perm(num,p)
            if not(guess in good):
                allgood = False
        if allgood:
            d = 0
            for num in out:
                guess = apply_perm(num,p)
                d = 10*d + good.index(guess)
            summa += d
            break

print(summa)
