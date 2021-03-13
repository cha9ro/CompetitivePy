N = int(input())
K = (len(str(N)) - 1) // 3
ans = 0
for k in range(1, K + 1):
  if k < K:
    ans += 999 * pow(10, 3 * k) * k
  else:
    ans += (N % pow(10, 3 * k) + 1) * k

print(ans)