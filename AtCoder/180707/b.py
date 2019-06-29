S = input()
w = int(input())

for i, c in enumerate(S):
    if i % w == 0:
        print(c, end='')
