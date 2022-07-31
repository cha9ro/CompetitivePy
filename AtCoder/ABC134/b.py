N = int(input())
s = input()

swapped = [s for i in range(1, N//2)]
for k in range(1, N//2):
    for i in range(0, k):
        temp = swapped[k][i]
        swapped[k][i] = swapped[k][2*k - i]
        swapped[k][2*k - i] = temp

print(swapped)
