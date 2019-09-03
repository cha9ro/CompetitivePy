def nextNodeIndex(node):
    nextNode = 1
    for n in range(2, N + 1):
        if 0 < node[n] and node[n] < node(nextNode):
            nextNode = n
    if node[nextNode] <= 0:
        return -1
    else:
        return nextNode


def makeDirNode(node, emit, i, j):
    # directional node i -> j
    node[i] -= 1
    node[j] -= 1
    emit[i] += 1

N, M = map(int, input().split(' '))
A = [0 for i in range(M)]
B = [0 for i in range(M)]
for m in range(M):
    A[m], B[m] = map(int, input().split(' '))

v = [[False for i in range(N + 1)] for j in range(N + 1)]
for m in range(M):
    v[A[m]][B[m]] = True
    v[B[m]][A[m]] = True
node = [0 for i in range(N + 1)]
for n in range(1, N + 1):
    node[n] = sum(v[n])
emit = [0 for i in range(N + 1)]

while sum(node) > 0:
    i = nextNodeIndex(node)
    for j in range(1, N + 1):
        while node[i] > 0:
            if emit[i] % 2 == 0:
                makeDirNode(node, emit, i, j)
            else:
                makeDirNode(node, emit, j, i)

if sum(emit) % 2 == 0:
    print('yes')
else:
    print('no')
