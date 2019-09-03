N = int(input())
line = input().split(' ')
A = map(int, line)

denominator = 0
for a in A:
    denominator += 1/a

print(1/denominator)