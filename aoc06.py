# Read input

with open("input06.txt") as f:
    inp = list(map(int,f.readline().split(',')))

inpl = [0]*9

for i in inp:
    inpl[i] += 1

# Part 1; replace 80 with 256 for Part 2

for _ in range(80):
    next = [0]*9
    for j in range(8):
        next[j] = inpl[j+1]
    next[6] += inpl[0]
    next[8] = inpl[0]
    inpl = next

print(sum(inpl))