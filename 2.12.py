#part1
game = []

with open("input_2.txt") as file:
    for line in file:
        bad_elf, my_elf = line.rstrip().split(" ")
        round = {"bad_elf": bad_elf, "my_elf": my_elf}
        game.append(round)

score = 0
for round in game:
    if round["my_elf"] == "X":
        score += 1
    elif round["my_elf"] == "Y":
        score += 2
    elif round["my_elf"] == "Z":
        score += 3


for round in game:
    if (round["my_elf"] == "X" and round["bad_elf"] == "C") or (round["my_elf"] == "Z" and round["bad_elf"] == "B") or (round["my_elf"] == "Y" and round["bad_elf"] == "A"):
        score += 6
    elif (round["my_elf"] == "X" and round["bad_elf"] == "A") or (round["my_elf"] == "Z" and round["bad_elf"] == "C") or (round["my_elf"] == "Y" and round["bad_elf"] == "B"):
        score += 3
    elif (round["my_elf"] == "Z" and round["bad_elf"] == "Z") or (round["my_elf"] == "X" and round["bad_elf"] == "B") or (round["my_elf"] == "Y" and round["bad_elf"] == "C"):
        score += 0
        
print(score)

#part2

game2 = []
with open("input_2.txt") as file:
    for line in file:
        bad_elf, score = line.rstrip().split(" ")
        round = {"bad_elf": bad_elf, "score": score}
        game2.append(round)

score2 = 0
for round in game2:
    if round["score"] == "X":
        score2 += 0
    elif round["score"] == "Y":
        score2 += 3
    elif round["score"] == "Z":
        score2 += 6

for round in game2:
    if (round["score"] == "Z" and round["bad_elf"] == "C") or (round["score"] == "Y" and round["bad_elf"] == "A") or (round["score"] == "X" and round["bad_elf"] == "B"):
        score2 += 1
    elif (round["score"] == "Z" and round["bad_elf"] == "A") or (round["score"] == "Y" and round["bad_elf"] == "B") or (round["score"] == "X" and round["bad_elf"] == "C"):
        score2 += 2
    elif (round["score"] == "Z" and round["bad_elf"] == "B") or (round["score"] == "Y" and round["bad_elf"] == "C") or (round["score"] == "X" and round["bad_elf"] == "A"):
        score2 += 3
        
print(score2)



