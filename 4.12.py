contain = 0
overlaped = 0

with open("input_4.txt") as file:
    for line in file:
        first_section, second_section = line.strip('/n').split(',')
        x1, x2 = [int(element) for element in first_section.split('-')]
        y1, y2 = [int(element) for element in second_section.split('-')]

        if (x1 <= y1 and y2 <= x2) or (y1 <= x1 and x2 <= y2):
            contain += 1
        
        if y2 >= x2 >= y1 or x2 >= y2 >= x1:
            overlaped += 1

print(contain)
print(overlaped)


