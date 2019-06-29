def update(groupList, a, b):
    isAdded = False
    for group in groupList:
        if a in group and b not in group:
            group.append(b)
            isAdded = True
            break
        elif a not in group and b in group:
            group.append(a)
            isAdded = True
            break
        elif a in group and b in group:
            isAdded = True
            break
    if not isAdded:
        groupList.append([a, b])


def isConnected(groupList, a, b):
    for group in groupList:
        if (a in group and b in group) or a == b:
            return True
    return False


def main():
    line = input().split(' ')
    N = int(line[0])
    Q = int(line[1])

    groupList = []
    P = [0 for i in range(Q)]
    A = [0 for i in range(Q)]
    B = [0 for i in range(Q)]
    for q in range(Q):
        line = input().split(' ')
        P[q] = int(line[0])
        A[q] = int(line[1])
        B[q] = int(line[2])

    for q in range(Q):
        p = P[q]
        a = A[q]
        b = B[q]
        if p == 0:
            update(groupList, a, b)
        else:
            if isConnected(groupList, a, b):
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    main()
