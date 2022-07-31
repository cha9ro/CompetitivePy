result = []


def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        result.insert(0, 'B')
        f(n/2)
    elif n % 2 == 1:
        result.insert(0, 'A')
        f(n-1)


N = int(input())
f(N)
for r in result:
    print(r, end='')
print()
