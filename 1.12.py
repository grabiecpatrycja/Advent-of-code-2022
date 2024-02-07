elf_kcal = []
sum_kcal = []
with open("input.txt") as file:
    for line in file:
        try:
            elf_kcal.append(int(line.rstrip()))
        except(ValueError):
            sum_kcal.append(sum(elf_kcal))
            elf_kcal.clear()
            continue

print(max(elf_kcal))

top_3 = sorted(sum_kcal)[-3:]

print(sum(top_3))




