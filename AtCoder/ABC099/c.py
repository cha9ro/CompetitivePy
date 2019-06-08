def func(n, k):
    i6 = 1
    i9 = 1
    while(i6*6 <= n):
        i6*=6
    while(i9*9 <= n):
        i9*=9
    n6 = n - i6
    n9 = n - i9
    # print(n, i6, i9)
    if n < 6:
        return k+n
    elif n6 == 0 or n9 == 0:
        return k+1
    elif n % 9 != 0 and n % 6 == 0:
        return func(n6, k+1)
    elif n % 9 == 0 and n % 6 != 0:
        return func(n9, k+1)
    else:
        return func(min(n6, n9), k+1)

N = int(input())
print (func(N, 0))
