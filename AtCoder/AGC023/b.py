def isGood(s, t):
    for i in range(N):
        for j in range(N):
            if s[i][j] != t[j][i]:
                return False
    return True

N = int(input())
s = [['' for i in range(N)]for i in range(N)]
t = [['' for i in range(N)]for i in range(N)]
for i in range(N):
    line = input()
    for j in range(N):
        s[i][j] = line[j]

count = 0
for A in range(N):
    for B in range(N):
        for i in range(N):
            for j in range(N):
                t[(i+A)%N][(j+B)%N] = s[i][j]
        if isGood(s, t):
            count += 1

print (count)