from collections import defaultdict

pos1 = 3
pos2 = 7

# Part 1

class dice:
    def __init__(self):
        self.val = 0
        self.rolls = 0
    def roll(self):
        self.val = self.val +1 if self.val < 100 else 1
        self.rolls += 1
        return self.val
    def getrolls(self):
        return self.rolls

score1 = 0
score2 = 0
playertoroll = 1
die = dice()

while score1 < 1000 and score2 < 1000:
    spaces = die.roll() + die.roll() + die.roll()
    if playertoroll == 1:
        pos1 = (pos1 + spaces)%10
        score1 += (pos1 if pos1 > 0 else 10) 
    else:
        pos2 = (pos2 + spaces)%10
        score2 += (pos2 if pos2 > 0 else 10) 
    playertoroll = 3 - playertoroll

print(die.getrolls()*min(score1,score2))

# Part 2

pos1 = 3
pos2 = 7

# State counts worlds with tuples of the form 
# (pos1,score1,pos2,score2,playertoroll,steps)

state = defaultdict(int)
state[(pos1,0,pos2,0,1,0)] = 1
wins1 = 0
wins2 = 0

# Count the worlds cw[r] in how many of them a result
# r is thrown as a result of three throws.

cw = [0,0,0,1,3,6,7,6,3,1]

while state:
    tmpstate = state.copy()
    for s in tmpstate:
        for r in [3,4,5,6,7,8,9]:
            if s[4] == 1: # First player rolls
                p1 = (s[0]+r)%10
                s1 = s[1] + (p1 if p1 > 0 else 10) 
                p2 = s[2]
                s2 = s[3]
                ptr = 3 - s[4]
                step = s[5] + 1
                if s1 >= 21:
                    wins1 += cw[r]*state[s]
                else:
                    state[(p1,s1,p2,s2,ptr,step)] += cw[r]*state[s]
            else: # Second player rolls
                p1 = s[0]
                s1 = s[1]
                p2 = (s[2]+r)%10
                s2 = s[3] + (p2 if p2 > 0 else 10) 
                ptr = 3 - s[4]
                step = s[5] + 1
                if s2 >= 21:
                    wins2 += cw[r]*state[s]
                else:
                    state[(p1,s1,p2,s2,ptr,step)] += cw[r]*state[s]
        del state[s]

print(max(wins1,wins2))


