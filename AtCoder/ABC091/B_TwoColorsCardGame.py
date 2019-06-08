N = int(input())
blue = []
for i in range(N):
    blue.append(input())

M = int(input())
red = []
for i in range(M):
    red.append(input())

count = {}
for s in blue:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
for t in red:
    if t in count:
        count[t] -= 1
    else:
        count[t] = -1

values = list(count.values())
keys = list(count.keys())
maxCount = max(values)
if maxCount > 0:
    print ( maxCount)
else:
    print (0)
