with open("input16.txt") as f:
    inp = f.readline().strip()

def b2d(s):
    return int('0b'+s,2)

def parse(l):
    version = b2d(l[:3])
    global versionsum
    versionsum += version
    type = b2d(l[3:6])
    if type ==4: # We found a literal
        i = 6
        s = ''
        while l[i] == '1':
            s += l[i+1:i+5]
            i += 5
        # The last number pre-padded with 0 must be read as well
        s += l[i+1:i+5]
        return((i+5,b2d(s))) # We return how many bits we actually read, and the result
    else: # We have an operator
        # Parse the arguments
        lentype = l[6]
        if lentype == '0':
            vs = []
            lenpacks = b2d(l[7:22])
            (n,v) = parse(l[22:22+lenpacks])
            vs.append(v)
            totlen = n
            j = 22
            while totlen < lenpacks:
                j += n
                (n,v) = parse(l[j:22+lenpacks])
                totlen += n
                vs.append(v)
            reslen = 22+totlen
        else: # lentype == '1'
            vs = []
            numpacks = b2d(l[7:18])
            j = 18 
            for _ in range(numpacks):
                (n,v) = parse(l[j:])
                j += n
                vs.append(v)
            reslen = j

        # Compute the result
        if type == 0:
            res = sum(vs)
        elif type == 1:
            res = 1
            for v in vs:
                res *= v
        elif type == 2:
            res = min(vs)
        elif type == 3:
            res = max(vs)
        elif type == 5:
            res = (1 if vs[0] > vs[1] else 0)
        elif type == 6:
            res = (1 if vs[0] < vs[1] else 0)
        elif type == 7:
            res = (1 if vs[0] == vs[1] else 0)

        return((reslen,res))

b = bin(int('8'+inp, 16))[6:]
versionsum = 0
(n,v) = parse(b)
print(f'Sum of version numbers: {versionsum}')
print(f'Value of the expression is {v}')