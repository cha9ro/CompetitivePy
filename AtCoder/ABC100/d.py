line = input().split(' ')
N = int(line[0])
M = int(line[1])
x = []
y = []
z = []
total = []
for i in range(N):
    line = input().split(' ')
    x.append(int(line[0]))
    y.append(int(line[1]))
    z.append(int(line[2]))
    total.append(x[i] + y[i] + z[i])

total.sort()
output = 0
for i in range(M-1, -1, -1):
    output += total[i]

print(output)