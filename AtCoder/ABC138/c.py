N = int(input())
line = input().split(' ')
v = [0] * N
for n in range(N):
    v[n] = int(line[n])

v.sort()

newV = v[0]
for i in range(1, len(v)):
    newV = (newV + v[i])/2

print(newV)