import math

def comb(n, k):
    return math.factorial(k)*math.factorial(n-k)/math.factorial(n)

line = input().split(' ')
n = int(line[0])
m = int(line[1])
d = int(line[2])
score = 0

for k in range(1, m):
    score += comb(m-1, k)

average = score/math.pow(n, m)
print(average)
