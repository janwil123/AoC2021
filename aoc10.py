# Read input

with open("input10.txt") as f:
    inp = [x.strip() for x in f.readlines()]

# Parts 1 & 2

score = 0
fine = {')':3, ']':57, '}':1197, '>':25137}
prem = {'(':1, '[':2, '{':3, '<': 4}
results = []

for l in inp:
    s = []
    i = 0
    for c in l:
        i += 1
        if c in ['(','[','{','<']:
            s.append(c)
        else:
            d = s.pop()
            if not (d,c) in [('(',')'),('[',']'),('{','}'),('<','>')]: # We found the first illegal character
                score += fine[c]
                break
        if i == len(l): # We are at the end of an incomplete input
            res = 0
            for _ in range(len(s)):
                e = s.pop()
                res = 5*res + prem[e]
            results.append(res)

# Part 1 
print(score) 

# Part 2
results.sort()
print(results[len(results)//2])