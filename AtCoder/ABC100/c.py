N = int(input())
line = input().split(' ')
A = [int(element) for element in line]

output = 0
for a in A:
    # print('a:', a)
    while a % 2 == 0 and a != 0:
        output += 1
        a = a // 2
        # print(a)
print('output:', output)