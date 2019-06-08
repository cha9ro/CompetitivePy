N = int(input())
a = []
b = []
c = []

line = input().split(' ')
for i in range(N):
    a.append(int(line[i]))
line = input().split(' ')
for i in range(N):
    b.append(line[i])

for i in range(N):
    for j in range(N):
        c.append(a[i] + b[j])
