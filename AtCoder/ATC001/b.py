def main():
    line = input().split(' ')
    N = int(line[0])
    Q = int(line[1])

    graph = [[False for i in range(N)]for i in range(N)]
    p = [0 for i in range(Q)]
    a = [0 for i in range(Q)]
    b = [0 for i in range(Q)]
    for q in range(Q):
        line = input().split(' ')
        p[q] = int(line[0])
        a[q] = int(line[1])
        b[q] = int(line[2])

    for q in range(Q):
        if p[q] == 0:
            graph[a[q]][b[q]] = True
            graph[b[q]][a[q]] = True
        else:
            if isConnected(graph, a[q], b[q]):
                print('Yes')
            else:
                print('No')


def isConnected(graph, start, goal):
    N = len(graph)
    isVisited = [False for i in range(N)]
    stack = []
    stack.append(start)
    isVisited[start] = True
    while len(stack) > 0:
        node = stack.pop()
        if node == goal:
            return True
        else:
            for i in range(N):
                if graph[node][i] and (not isVisited[i]):
                    stack.append(i)
                    isVisited[i] = True
    return False


if __name__ == '__main__':
    main()
