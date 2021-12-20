n = 100

image = []

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

with open("input20.txt") as f:
    alg = f.readline().strip()
    _ = f.readline()
    for _ in range(n):
        image.append(f.readline().strip())

# Wrap a double frame of symbol c around the image im

def wrap2(im,c):
    d = len(im[0])
    im1 = [c*(d+4),c*(d+4)]
    for l in im:
        im1.append(c+c+l+c+c)
    im1.append(c*(d+4))
    im1.append(c*(d+4))
    return im1

def runalg(im):
    d = len(im[0])
    newim = []
    for i in range(1,d-1):
        newl = ''
        for j in range(1,d-1):
            ind = 0
            for dir in dirs:
                if im[i+dir[0]][j+dir[1]] == '.':
                    ind = 2*ind
                else:
                    ind = 2*ind+1
            newl += alg[ind]
        newim.append(newl)
    return newim

# Put range(1) here for Part 1

for _ in range(25):
    image = wrap2(image,'.')
    image = runalg(image)
    image = wrap2(image,'#')
    image = runalg(image)

cnt = 0

for l in image:
    for c in l:
        if c == '#':
            cnt += 1

print(cnt)