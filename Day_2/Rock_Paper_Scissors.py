import string

f = open("/Users/tjams20/Documents/Other/Coding_Skills/Advent_Code_2022/Day_2/input.txt")
lns = f.readlines()
tot_score = 0

def score(instruc_1, instruc_2):
    i1 = string.ascii_uppercase.index(instruc_1)
    i2 = string.ascii_uppercase.index(instruc_2) - 23
    print(instruc_1, instruc_2, i1, i2, (i2-i1)%3)
    win_lose_draw_score = [3,6,0][(i2-i1)%3]
    score = win_lose_draw_score + i2 + 1 
    return score

for ln in lns:
    instruc = ln.split()
    tot_score += score(instruc[0], instruc[1])

print(tot_score)


