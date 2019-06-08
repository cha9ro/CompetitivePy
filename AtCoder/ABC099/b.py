line = input().split(' ')
a = int(line[0])
b = int(line[1])
n = b - a
h = int(n*(n+1)/2)
print(h-b)