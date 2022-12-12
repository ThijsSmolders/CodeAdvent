import string

f = open("/Users/tjams20/Documents/Other/Coding_Skills/Advent_Code_2022/Day_3/input.txt")
lns = f.readlines()

score = 0

for ln_id, ln in enumerate(lns):
    ln = ln.strip()
    mid_len = int(len(ln)/2)
    ln_left = ln[:mid_len]
    ln_right = ln[mid_len:]
    for i in ln_left:
        if i in ln_right:
            if i.isupper():
                score += string.ascii_uppercase.index(i) + 26 + 1
                break
            else:
                score += string.ascii_lowercase.index(i) + 1
                break


print(score)