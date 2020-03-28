N = int(input())
line = input().split()
B = [0] * (N-1)
for i in range(N-1):
    B[i] = int(line[i])

ans = 0
for i in range(N):
    if i == 0:
        ans += B[i]
    elif i == N-1:
        ans += B[i-1]
    else:
        ans += min(B[i], B[i-1])
print(ans)