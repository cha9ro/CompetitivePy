line = input().split(' ')
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

if abs(a - c) <= d:
    print ('Yes')
elif abs(a - b) <= d and abs(b - c) <= d:
    print ('Yes')
else:
    print ('No')