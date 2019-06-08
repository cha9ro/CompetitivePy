line = input().split(' ')
a = int(line[0])
b = int(line[1])
print(max(a+b, a-b, a*b))