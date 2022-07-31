N = int(input())
S = ['' for n in range(N)]
T = ['' for n in range(N)]
for n in range(N):
    S[n], T[n] = input().split(' ')

for i in range(N-1):
    for j in range(i+1, N):
        if S[i] == S[j] and T[i] == T[j]:
            print('Yes')
            exit()
print('No')
