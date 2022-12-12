#!/usr/bin/env python3

elf_cnt = 1
elf_max = -1
cur_cal = 0
cals = []

f = open("/Users/tjams20/Documents/Other/Coding_Skills/Advent_Code_2022/Day_1/Elves_Calories.txt")
lns = f.readlines()
for ln in lns:
    cal = ln.strip()
    if not cal:
        print("Elf {} has {} calories.".format(elf_cnt, cur_cal))
        cals.append(cur_cal)
        cur_cal = 0
        elf_cnt += 1
    else: 
        # print("Elf {} is carrying at least {} calories".format(elf_cnt, cal))
        cur_cal += int(cal)
    
print(sum(sorted(cals)[-3:]))