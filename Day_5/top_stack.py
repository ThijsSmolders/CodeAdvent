#!/Users/tjams20/opt/anaconda3/envs/CCS/bin/python

import numpy as np

f = open("/Users/tjams20/Documents/Other/Coding_Skills/Advent_Code_2022/Day_5/init_stacks.txt")
lns = f.readlines()

cargo_numbers = lns[-1].strip()
cargo_pos = []

for elm_id, elm in enumerate(cargo_numbers):
    if elm:
        np.append(cargo_pos, elm_id+1)
        print(elm)

print(cargo_pos)

# cargos = [np.stack()

# for ln in lns:
    ln = ln.strip()
    print(ln)