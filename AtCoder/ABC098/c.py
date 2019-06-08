
n = int(input())
s = input()

w2e = [0] * n
e2w = [0] * n

for i in range(n):
    if i == 0:
        if s[i] == 'W':
            w2e[i] = 1
    else:
        if s[i] == 'W':
            w2e[i] = w2e[i-1] + 1
        else:
            w2e[i] = w2e[i-1]

for i in reversed(range(n)):
    j = n - i - 1
    if j == 0:
        if s[i] == 'E':
            e2w[j] = 1
    else:
        if s[i] == 'E':
            e2w[j] = e2w[j-1] + 1
        else:
            e2w[j] = e2w[j-1]

out = n
for i in range(n):
    if i == 0:
        temp = e2w[n-1]
    elif i == n-1:
        temp = w2e[n-1]
    else:
        temp = w2e[i-1] + e2w[n-i-1]
    if temp < out:
            out = temp

print (out)


# print(w2e)
# print(e2w)