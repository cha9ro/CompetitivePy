from math import sqrt

N = int(input())

a = [''] * N
b = [''] * N
for i in range(N):
    line = input()
    line = line.split(' ')
    a[i] = int(line[0])
    b[i] = int(line[1])

c = [''] * N
d = [''] * N
for i in range(N):
    line = input()
    line = line.split(' ')
    c[i] = int(line[0])
    d[i] = int(line[1])

count = 0
cUsed = [False] * N
dUsed = [False] * N
for i in range(N):
    distance = [10*N] * N
    for j in range(N):
        if cUsed[j] == False and dUsed[j] == False:
            if a[i] < c[j] and b[i] < d[j]:
                distance[j] = sqrt((c[j] - a[i])**2 + (d[j] - b[i])**2)
    if min(distance)<10*N:
        # print(i, j, min(distance))
        cUsed[distance.index(min(distance))] = True
        dUsed[distance.index(min(distance))] = True
        count += 1

print (count)
