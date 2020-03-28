N, X, Y = map(int, input().split(' '))
distance = [0] * N - 1
for i in range(N-1):
  for j in range(1, N):
    if i >= Y or j <= X:
      distance[j - i - 1] += 1
    elif i <= X and j >= Y:
      distance[j - Y + X - i - 1] += 1
    else:
      distance[j-Y + X-i - 1] += 1

for d in distance:
  print(d)