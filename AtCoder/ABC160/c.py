K, N = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
a.sort()

d = []
for i in range(N):
  if i == N-1:
    d.append(a[0] + K - a[N-1])
  else:
    d.append(a[i+1] - a[i])

maxDistance = max(d)
startIndex = d.index(maxDistance)
ans = 0
for i in range(N-1):
  ans += d[startIndex - i-1]

print(ans)