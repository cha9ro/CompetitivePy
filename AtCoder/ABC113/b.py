N = int(input())
T, A = input().split(' ')
T = int(T)
A = int(A)
line = input().split(' ')

minScore = abs(A-(T-int(line[0]) * 0.006))
minIndex = 1
for i in range(N):
    h = int(line[i])
    temp = abs(A-(T - h * 0.006))
    if temp < minScore:
        minScore = temp
        minIndex = i + 1

print (minIndex)
