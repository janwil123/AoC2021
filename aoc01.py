# Read input

with open("input01.txt") as f:
    ns = f.readlines()

nums = [int(n) for n in ns]

l = len(nums)

# First task

c = 0

for i in range(1,l):
    if nums[i-1] < nums[i]:
        c+=1

print(c)

# Second task

c = 0
d = nums[0]+nums[1]+nums[2]

for i in range(0,l-3):
    e = d - nums[i]+nums[i+3]
    if d < e:
        c+=1
    d = e

print(c)