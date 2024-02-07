data = open("input_5.txt").readlines()

stacks = []
for col in range(1, 36, 4):
    stack = []
    for row in range(8):
        try:
            if data[row][col] == ' ':
                continue
            stack.append(data[row][col])
        except IndexError:
            continue
    stacks.append(list(reversed(stack)))

#part1
# for instruction in data[10:]:
#     instruction_split = instruction.split(' ')
#     x, y, z = int(instruction_split[1]), int(instruction_split[3]) - 1, int(instruction_split[5]) -1

#     moving = []
#     for _ in range(x):
#         moving.append(stacks[y].pop())
    
#     stacks[z] = stacks[z] + moving

#part2
for instruction in data[10:]:
    instruction_split = instruction.split(' ')
    x, y, z = int(instruction_split[1]), int(instruction_split[3]) - 1, int(instruction_split[5]) -1

    moving = []
    for _ in range(x):
        moving.append(stacks[y].pop())
    
    stacks[z] = stacks[z] + moving[::-1]

for s in stacks:
    print(s[-1], end='')




