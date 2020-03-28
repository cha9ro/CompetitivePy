N = int(input())
lineA = input().split()
lineB = input().split()
lineC = input().split()
A = [0] * N
B = [0] * N
C = [0] * (N-1)
for i in range(N):
    if i<N-1:
        A[i] = int(lineA[i])
        B[i] = int(lineB[i])
        C[i] = int(lineC[i])
    else:
        A[i] = int(lineA[i])
        B[i] = int(lineB[i])

ans = sum(B)
for i in range(0, N-1):
    if A[i+1] == A[i] + 1:
        ans += C[A[i]-1]
print(ans)