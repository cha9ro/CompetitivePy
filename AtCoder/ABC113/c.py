line = input().split(' ')
N = int(line[0])
M = int(line[1])
P = [0] * N
data = [] * M
for i in range(M):
    line = input().split(' ')
    p = int(line[0])
    y = int(line[1])
    data[i] = [p, y]
data = sorted(data, lambda x: x[1])