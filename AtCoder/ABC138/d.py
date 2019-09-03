N, Q = map(int, input().split())

p = [0] * (Q + 1)
x = [0] * (Q + 1)

counter = [0] * (N+1)
node = [[False] * (N+1)] * (N+1)

for i in range(N):
    a, b = map(int, input().split())
    node[a][b] = True

for i in range(Q):
    p, x = map(int, input().split())
    children = getChildren(p)
    for child in children:
        counter[child] += x

for n in range(1, N + 1):
    print(counter[n], end=' ')

def getChildren(index, node):
    '''
    return children array of node[index]
    '''
    children = [index]
    queue = [index]
    while (len(queue) > 0):
        child = queue.pop()
        nodeLine = []
        for n in node[index]:
            nodeLine.append(n)