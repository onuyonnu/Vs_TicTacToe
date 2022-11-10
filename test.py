list = [['1','2','3'], ['4','5','6']]

for line in list:
    print(line)
    for spot in range(len(line)):
        if line[spot] != 1:
            line[spot] = 1
print(list)
