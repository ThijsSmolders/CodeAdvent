import string

f = open("/Users/tjams20/Documents/Other/Coding_Skills/Advent_Code_2022/Day_3/input.txt")
lns = f.readlines()

score = 0

for elf_group in range(int(len(lns)/3)):
    elf_A = lns[3*elf_group].strip()
    elf_B = lns[3*elf_group+1].strip()
    elf_C = lns[3*elf_group+2].strip()

    for let in elf_A:
        if (let in elf_B) and (let in elf_C):
            if let.isupper():
                print(elf_group)
                score += string.ascii_uppercase.index(let) + 26 + 1
                break
            else:
                print(elf_group)
                score += string.ascii_lowercase.index(let) + 1
                break

print(score)