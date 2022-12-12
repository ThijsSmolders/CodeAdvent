f = open("/Users/tjams20/Documents/Other/Coding_Skills/Advent_Code_2022/Day_4/input.txt")
lns = f.readlines()

nr_slack = 0

for ln in lns:
    ln = ln.strip()
    left_elf, right_elf = ln.split(',')
    left_min, left_max = left_elf.split('-')
    right_min, right_max = right_elf.split('-')

    left_min = int(left_min)
    left_max = int(left_max)
    right_min = int(right_min)
    right_max = int(right_max) 

    if ((left_min <=right_min) and (left_max >= right_max)) or ((left_min >= right_min) and (left_max <= right_max)):
        nr_slack += 1

print(nr_slack)