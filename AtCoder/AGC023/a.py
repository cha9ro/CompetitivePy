N = int(input())
A = [0] * N
As = input().split(' ')
for i in range(N):
    A[i] = int(As[i])

score = [0] * N
pairList = []

for i in range(N):
    if i in pairList[1]:
        ind = pairList[1].index(i)
        a = pairList[ind][0]
        score[i] = score[a] - 1
    else:    
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum == 0:
                score[i] += 1
                pairList.append([i, j])