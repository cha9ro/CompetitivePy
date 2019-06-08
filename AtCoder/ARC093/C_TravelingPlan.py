import copy
n = int(input())
line = input().split(' ')
a = [int(element) for element in line]
cost = [0] * n

originalCost = 0
cur = 0
for i in range(n):
    originalCost += abs(a[i] - cur)
originalCost += abs(cur)

cur = 0
for i in range(n):
    if i == n-1:
        next = 0
    else:
        next = a[i+1]
    if (cur < a[i] and a[i] < next) or 