input = open("input_6.txt").read()

for index, char in enumerate(input[:-4]):
    if len(set(input[index:index+4])) == 4:
        print(index + 4)
        break


for index, char in enumerate(input[:-14]):
    if len(set(input[index:index+14])) == 14:
        print(index + 14)
        break
