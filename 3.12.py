import string
item_sum = 0
with open("input_3.txt") as file:
    for line in file:
        line = line.strip("\n")
        left, right = line[:len(line)//2], line[len(line)//2:]
        intersection = set(left).intersection(set(right))
        for l in list(intersection):
            item_sum += string.ascii_letters.index(l) + 1

print(item_sum)

# part2
input = []

with open("input_3.txt") as file:
    for line in file:
        input.append(line.strip("\n"))

points = 0
n = 0
for i in input:
    intersection_2 = set(input[n]).intersection(set(input[n+1])).intersection(set(input[n+2]))
    for l in list(intersection_2):
        points += string.ascii_letters.index(l) + 1
    n += 3
    if n == (len(input)):
        break

print(points)
