file = open("input_25.txt").readlines()

dec_number = 0
for line in file:
    SNAUF = line.rstrip()[::-1]
    for index, s in enumerate(SNAUF):
        DECIMAL = 0
        if s == "2" or s == "1" or s == "0":
            DECIMAL += int(s)*5**(index)
        elif s == "=":
            DECIMAL += (-2)*5**(index)
        elif s == "-":
            DECIMAL += (-1)*5**(index)
    dec_number += DECIMAL
print(dec_number)

snauf_number = []
n = 0
while n >= 0:
    y = 5**n
    if dec_number > y:
        n += 1
        continue
    else:
        if y > dec_number and abs(y - dec_number) < dec_number:
            snauf_number.append("1")
            number = dec_number - y
            break
        else:
            snauf_number.append("2")
            number = dec_number - (2*5**(n-1))
            n = n-1
            break

while n > 0:
    x = 5**(n-1)
    d_1 = number + 2*x
    d_2 = number + x
    d_3 = number
    d_4 = number - x
    d_5 = number - 2*x
    list = [abs(d_1), abs(d_2), abs(d_3), abs(d_4), abs(d_5)]
    if min(list) == abs(d_1):
        snauf_number.append("=")
        n -= 1
        number = d_1
    elif min(list) == abs(d_2):
        snauf_number.append("-")
        n -= 1
        number = d_2
    elif min(list) == abs(d_3):
        snauf_number.append("0")
        n -= 1
        number = d_3
    elif min(list) == abs(d_4):
        snauf_number.append("1")
        n -= 1
        number = d_4
    elif min(list) == abs(d_5):
        snauf_number.append("2")
        n -= 1
        number = d_5

print(snauf_number)


