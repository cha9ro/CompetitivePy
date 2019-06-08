line = input()
line = line.split(' ')
a, b, item = [int(line[0]), int(line[1]), int(line[2])]
if a+b >= item:
    print('Yes')
else:
    print('No')
